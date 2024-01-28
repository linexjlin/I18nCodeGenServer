# I18nCodeGenServer

Auto Generate i18n resource


## How to Use?

1. Crate a project id like 'ce405725-a840-468d-a57f-0bb95cbfbcfb'

1. Download the fist coding language codes for examle python via link `https://i18n.linkown.com/ce405725-a840-468d-a57f-0bb95cbfbcfb?file=languages.py&languages=en,de,fr,az` en,de,fr,az is the languages. We got:
![](https://ipfs.ee/ipfs/QmT27sLSS5pDMaHzoN6PqEXMthijApwShn44G7ezEnHF82/18cad445-056b-4711-b24f-5bc5b693f7f6.png)

1. Put the downloaded file to your project. 
![](https://ipfs.ee/ipfs/QmQJHuhdPjFMn7W6wJYoG3qatAuciDf4GfC1YhjbHLPVat/a10fd56c-d3ef-45fd-877a-8d13d8263c77.png)

1. Replace call UText funcion in every UI string. When you run the software, you will find that the interface language of your software has not changed. Don't worry, during the running program, all the texts to be translated will be sent to the server.
![](https://ipfs.ee/ipfs/QmVLLHRpk5MbFPkftRSsZnANjLxUpcSAmWXfduU7CShTPz/b688a2c8-e4bf-4dbe-9da7-4669b7787168.png)

1. Download again, this time you will get a updated version that all text are translated. Set ULANG enviroment to other like `de` to check the effect.
![](https://ipfs.ee/ipfs/QmWXGgLB1oyBjQH9f4z8QJJqtUNtqXxp2opBuUZbexsafw/5912bedd-832e-4772-b892-d183b985858c.png)

Detail document check [here](./API.md)

## Run With Your Own Server

`uvicorn api:app --reload --port 1850 --host 0.0.0.0 --workers 1`
