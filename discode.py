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

VERSION = "0.0.9"

DESCRIPTION = """
Discode is a simple utility to let you have quick and easy discussions around
a bit of code. Part paste bin, part code review and super simple and easy to
use."""


def _parse_args(args):
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('files', type=argparse.FileType('rb'), nargs="*",
                        default=[])
    parser.add_argument('-n', '--no-open', action='store_true')
    parser.add_argument('-H', '--host', default="http://www.discode.co")
    parser.add_argument('--version', action='version',
                        version='%(prog)s ' + VERSION)
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
            _post_paste(stdin, args)

    for f in args.files:
        data = f.read()
        _post_paste(data, args)


if __name__ == "__main__":
    main()
