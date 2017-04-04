import json
try:
    from StringIO import StringIO
except:
    from io import StringIO

import pytest

import discode


@pytest.fixture
def fake_files(tmpdir):
    f1 = tmpdir.join("file1")
    f1.write("File 1")
    f2 = tmpdir.join("file2")
    f2.write("File 2")
    return [str(f1), str(f2)]


@pytest.fixture
def args(tmpdir):
    return discode._parse_args(tmpdir)


@pytest.fixture
def urlopen():
    res = StringIO()
    res.write(json.dumps({"paste": "/id"}))
    res.seek(0)
    return lambda req: res


@pytest.fixture
def Request():
    class R(object):
        def __init__(self, host, data, headers=None):
            self.host = host
            self.data = data
            self.headers = headers
    return R


class TestParser:

    def test_cli_no_args(self):
        parsed = discode._parse_args([])
        assert parsed.files == []
        assert parsed.no_open is False
        assert parsed.host == "http://www.discode.co"

    def test_cli_files(self, fake_files):
        parsed = discode._parse_args([fake_files[0], fake_files[1]])
        assert [f.name for f in parsed.files] == fake_files
        assert parsed.no_open is False
        assert parsed.host == "http://www.discode.co"

    def test_cli_no_open(self, fake_files):
        parsed = discode._parse_args([fake_files[0], "--no-open"])
        assert [f.name for f in parsed.files] == [fake_files[0], ]
        assert parsed.no_open is True
        assert parsed.host == "http://www.discode.co"

    def test_cli_custom_host(self, fake_files):
        parsed = discode._parse_args([fake_files[1], "-H",
                                      "http://httpbin.org"])
        assert [f.name for f in parsed.files] == [fake_files[1], ]
        assert parsed.no_open is False
        assert parsed.host == "http://httpbin.org"


class TestPost:

    def test_post_paste(self, fake_files, urlopen, Request):
        parsed = discode._parse_args([fake_files[0]])
        data = "Contents"
        discode._post_paste(data, parsed, urlopen=urlopen, Request=Request)
