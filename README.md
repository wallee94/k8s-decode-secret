# Kubernetes list secrets

Quick script to retrieve decoded secret object from a k8s cluster.

## Usage

The script uses python to read the JSON and decode the base64 values.

You can retrieve and decode a secret using:

```bash
./secrets <secret-name>
```
