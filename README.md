# freedom-network-bot
Telegram bot for providing VPN based on [OutlineVPN](https://getoutline.org/)

### [t.me/freedom_network_bot](https://t.me/freedom_network_bot)

## Features

* Self-hosted OutlineVPN
* No logs
* Complete anonymity

# How to run

## Quickstart: Pooling & SQLite

The fastest way to run the bot is to run it in pooling mode using SQLite database without all Celery workers for background jobs. This should be enough for quickstart:

``` bash
git clone https://github.com/p3ngu19z/freedom-network-bot
cd freedom-network-bot
```

Create virtual environment (optional)
``` bash
python3 -m venv dtb_venv
source dtb_venv/bin/activate
```

Install all requirements:
```
pip install -r requirements.txt
```

Create `.env` file in root directory and copy-paste this:
``` bash 
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
TELEGRAM_TOKEN=<ENTER YOUR TELEGRAM TOKEN HERE>
```

Run migrations to setup SQLite database:
``` bash
python manage.py migrate
```

Create superuser to get access to admin panel:
``` bash
python manage.py createsuperuser
```

Run bot in pooling mode:
``` bash
python run_pooling.py 
```

If you want to open Django admin panel which will be located on http://localhost:8000/tgadmin/:
``` bash
python manage.py runserver
```
