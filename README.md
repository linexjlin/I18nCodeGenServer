# I18nCodeGenServer
Auto Generate i18n resource


## How to Use
1. Crate a project id like 'ce405723-a840-468d-a57f-0bb95cbfbcfb'
1. Download languages codes via link `https://i18n.linkown.com/ce405723-a840-468d-a57f-0bb95cbfbcfb?file=languages.py&languages=en,de,fr,az`
1. Put the downloaded file to your project. 

## Run Server

`uvicorn api:app --reload --port 1850 --host 0.0.0.0 --workers 1`
