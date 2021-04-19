import base64
import json
import shlex
import sys
from subprocess import Popen, PIPE


def main():
    name = sys.argv[1]
    with Popen(["kubectl", "get", "secrets", name, "-o=json"], stdout=PIPE) as pc:
        current = json.load(pc.stdout)

    objs = [
        (k, base64.b64decode(v.encode()).decode())
        for k, v in current.get('data', {}).items()
    ]
    inp = input('Write new secret key-value (leave empty to finish): ')
    while inp:
        k, v = inp.split('=', 1)
        objs.append((k, v))
        inp = input('Write new secret key-value (leave empty to finish): ')

    cmd = f"kubectl create secret generic {current['metadata']['name']} \\\n"
    values = [
        f"  --from-literal={k}={shlex.quote(v)} "
        for k, v in objs
    ]
    cmd += '\\\n'.join(values)
    print(cmd)


if __name__ == '__main__':
    main()

