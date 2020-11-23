import base64
import json
import sys


def main():
    try:
        obj = json.load(sys.stdin)
    except ValueError:
        return
    for k, v in obj.get('data', {}).items():
        obj['data'][k] = base64.b64decode(v.encode()).decode()

    print(json.dumps(obj, indent=4))


if __name__ == '__main__':
    main()

