from argparse import ArgumentParser
from json import loads, dumps
from tempfile import gettempdir
from os import path, remove


save_file = path.join(gettempdir(), 'storage.data')


def get_data():
    if not path.exists(save_file):
        return {}

    with open(save_file, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return loads(raw_data)

        return {}


def put(key, value):
    data = get_data()

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    print(save_file)
    with open(save_file, 'w') as f:
        f.write(dumps(data))


def get(key):
    data = get_data()

    return data.get(key)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        remove(save_file)
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')