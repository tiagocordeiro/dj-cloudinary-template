# Exemplo simples de uso do Cloudinary com Django

[![Updates](https://pyup.io/repos/github/tiagocordeiro/dj-cloudinary-template/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/dj-cloudinary-template/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/dj-cloudinary-template/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/dj-cloudinary-template/)


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/tiagocordeiro/dj-cloudinary-template.git
cd dj-cloudinary-template
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```


### Crie uma conta na Cloudinary
E adicione as informações (API Key etc) ao .env
