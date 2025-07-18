# TLS configuration instructions

To enable tls globally please set `ingress.tls.enabled=true` in `values.yaml`

## Let’s Encrypt setup

If you want to configure [letsencrypt](https://letsencrypt.org/)
certification, you need to:

1. Set `ingress.tls.source="letsEncrypt"` in `values.yaml`
2. Create namespace for cert-manager

```bash
kubectl create namespace cert-manager
```

1. Add repository and update repos list

```bash
  helm repo add jetstack https://charts.jetstack.io
  helm repo update
```

1. Install cert-manager release

```bash
  helm install \
    cert-manager jetstack/cert-manager \
    --namespace cert-manager \
    --version v1.15.3 \
    --set crds.enabled=true
```

1. After that, `waldur` release is ready for installation.

## Your own certificate

In case, when you want to use own certificate, you need to:

1. Set `ingress.tls.source="secret"` in `values.yaml`
2. Set `ingress.tls.secretsDir` variable to directory
    with your `tls.crt` and `tls.key` files. By default it is set to `tls`
3. After that, `waldur` release is ready for installation
