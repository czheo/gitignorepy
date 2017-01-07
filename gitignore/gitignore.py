import argparse
import requests
import requests_cache
import os
requests_cache.install_cache(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/cache'), expire_after=60*60)


def fetch(keyword):
    lst = get_list(keyword)
    exact_match = [x for x in lst if x['name'].lower() == keyword.lower()]
    if len(exact_match) > 0:
        print(requests.get(exact_match[0]['download_url']).text, end='')
    elif len(lst) == 0:
        print('Template not found:', keyword)
    elif len(lst) == 1:
        print(requests.get(lst[0]['download_url']).text, end='')
    else:
        print('Ambiguous keyword:', keyword)
        _print_list(lst)


def get_list(keyword):
    l1 = _fetch_list('https://api.github.com/repos/github/gitignore/contents/')
    l2 = _fetch_list('https://api.github.com/repos/github/gitignore/contents/Global')
    return [x for x in sorted(l1 + l2, key=lambda x: x['name']) if keyword.lower() in x['name'].lower()]


def _fetch_list(url):
    lst = requests.get(url).json()
    return [x for x in lst if x['type'] == 'file' and not x['name'].startswith('.')]


def _print_list(lst):
    for x in lst:
        print('-', x['name'].replace('.gitignore', ''))
    print('Found %d template' % len(lst) + ('s.' if len(lst) > 1 else '.'))

def main():
    parser = argparse.ArgumentParser(prog='gitignore',
                                     description='fetch gitignore from Github.com')
    subparsers = parser.add_subparsers(dest='command')
    # fetch
    parser_fetch = subparsers.add_parser('fetch', help='fetch a gitignore file')
    parser_fetch.add_argument('keyword')
    # list
    parser_list = subparsers.add_parser('list', help='list available gitignore files')
    parser_list.add_argument('keyword', default='', nargs='?')

    args = parser.parse_args()
    if args.command:
        if args.command == 'fetch':
            fetch(args.keyword)
        elif args.command == 'list':
            _print_list(get_list(args.keyword))
    else:
        parser.print_help()
