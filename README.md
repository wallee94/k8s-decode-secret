# Kubernetes decode secret

Quick script to update keys in a secret object from a k8s cluster.

## Usage

The script uses python to read the JSON and decode the base64 values.

Run the `secrets` script. It will request any new keys and print the shell command with
values escaped:

```bash
>> ./secrets sec-name
Write new secret key-value (leave empty to finish): allowed_hosts=*
Write new secret key-value (leave empty to finish):

kubectl delete secret sec-name && kubectl create secret generic sec-name \
  --from-literal=celery_broker_url=amqp://user:pp455w0rd@rabbitmq:5672//
  --from-literal=allowed_hosts='*'
```
