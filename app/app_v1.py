import apprise

apobj = apprise.Apprise()

apobj.add('https://outlook.office.com/webhook/cc7ebf15-406f-41fa-854b-3118d93269d5@b41b72d0-4e9f-4c26-8a69-f949f367c91d/IncomingWebhook/0d952473eae54096b181c9be954be9b0/ab285e23-f1a7-4f33-aafa-51d1a532e43f')

attachment = apprise.AppriseAttachment()
attachment.add('https://i.redd.it/my2t4d2fx0u31.jpg?name=FlyingToMars.jpg')

apobj.notify(
    body='[Google alert](https://console.cloud.google.com/monitoring/alerting/incidents/0.lkkpyne8uznk?project=toryburch-nextgen)',
    title='This is test',
    attach=attachment
)

