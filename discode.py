from __future__ import print_function

import argparse
import json
import select
import sys
import webbrowser

try:
    from urllib.request import urlopen as _urlopen, Request as _Request
except ImportError:
    from urllib2 import urlopen as _urlopen, Request as _Request

PY2 = sys.version_info[0] == 2


def _parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type=argparse.FileType('rb'), nargs="*",
                        default=[])
    parser.add_argument('-n', '--no-open', action='store_true')
    parser.add_argument('-H', '--host', default="http://www.discode.co")
    parsed = parser.parse_args(args)

    if len(args) == 0:
        parser.print_help()

    return parsed


def _post_paste(data, args, urlopen=_urlopen, Request=_Request):
    if not PY2 and isinstance(data, str):
        data = str.encode(data)
    req = Request(args.host, data, headers={
        "Content-Type": "application/json",
    })
    res = urlopen(req)

    res_data = res.read()
    if not PY2 and isinstance(res_data, bytes):
        res_data = res_data.decode("utf-8")

    res_json = json.loads(res_data)

    if not args.no_open:
        url = "{}{}".format(args.host, res_json['paste'])
        print("Read for discussion at: {}".format(url))
        webbrowser.open_new(url)


def _read_stdin():
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        return sys.stdin.read()


def main():

    args = _parse_args(sys.argv[1:])

    if not args.files:
        stdin = _read_stdin()
        if stdin:
            _post_paste(stdin, args.host, args.no_open)

    for f in args.files:
        data = f.read()
        _post_paste(data, args.host, args.no_open)


if __name__ == "__main__":
    main()
