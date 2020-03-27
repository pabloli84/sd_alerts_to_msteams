# Send Google Cloud Monitoiring (former Stackdriver) Alerts to MS Teams
[![Build Status](https://travis-ci.org/pabloli84/sd_alerts_to_msteams.svg?branch=master)](https://travis-ci.org/pabloli84/sd_alerts_to_msteams)

This app allows to redirect messages from Google Monitoring Alerts to MS Teams channel via channel connector webhok.

You need specify following variables

| Variable name | Description |
|:--------------|-------------|
| MS_TEAMS_WEBHOOK | MS Teams connector webhook |
| SD2TEAMS_MODE | Operational mode, default Dev, for production use Prod |

# How to encrypt MS_TEAMS_WEBHOOK variable for Cloud Build

```bash
echo -n https://outlook.office.com/webhook/<...> /<...>/<...> | gcloud kms encrypt \
 --ciphertext-file=- \
 --plaintext-file=- \
 --location=us-central1 \
 --keyring=sd2teams-secrets \
 --key=sd2teams-secrets | base64
```

Then put provided value to _cloudbuild.yaml_ into _secertetEnv_ in _secrets_ section.