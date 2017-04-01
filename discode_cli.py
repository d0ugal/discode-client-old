from __future__ import print_function

import argparse
import json
import sys
import select
import webbrowser

try:
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request
except ImportError:
    from urllib import urlencode
    from urllib2 import urlopen, Request

PY2 = sys.version_info[0] == 2


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type=argparse.FileType('rb'), nargs="*",
                        default=[])
    parser.add_argument('-n', '--no-open', action='store_true')
    parser.add_argument('-H', '--host', default="http://www.discode.co")
    args = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help()

    return args


def _post_paste(data, args):
    if not PY2 and isinstance(data, str):
        data = str.encode(data)
    req = Request(args.host, data, headers={
        "Content-Type": "application/json",
    })
    res = urlopen(req)

    res_data = json.loads(res.read())

    if not args.no_open:
        url = "{}{}".format(args.host, res_data['paste'])
        print("Read for discussion at: {}".format(url))
        webbrowser.open_new(url)

def _read_stdin():
    if select.select([sys.stdin,],[],[],0.0)[0]:
        return sys.stdin.read()


def main():

    args = _parse_args()

    if not args.files:
        stdin = _read_stdin()
        if stdin:
            _post_paste(stdin, args)

    for f in args.files:
        data = f.read()
        _post_paste(data, args)


if __name__ == "__main__":
    main()
