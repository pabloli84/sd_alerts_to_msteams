# Send Google Cloud Monitoiring (former Stackdriver) Alerts to MS Teams
[![Build Status](https://travis-ci.org/pabloli84/sd_alerts_to_msteams.svg?branch=master)](https://travis-ci.org/pabloli84/sd_alerts_to_msteams)

This app allows to redirect messages from Google Monitoring Alerts to MS Teams channel via channel connector webhok.

You need specify following variables

| Variable name | Description |
|:--------------|-------------|
| MS_TEAMS_WEBHOOK | MS Teams connector webhook |
| SD2TEAMS_MODE | Operational mode, default Dev, for production use Prod |