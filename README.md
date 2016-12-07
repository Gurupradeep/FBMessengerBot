# FBMessengerBot

A simple bot which echoes back the message which you have typed in your facebook page.

# Tools used 
#### Django
#### ngrok
#### facebook graph api

Ngrok that sets up secure tunnels to our localhost i.e. Ngrok gives web accessible URLs and tunnels all traffic from that URL to our localhost. Facebook webhooks sends payload to that url and it will be handled by the bot

# Installing Ngrok
Go to [Ngrok's download page](https://ngrok.com/), download the zip file, unzip. 

Setting up Ngrok:

    ./ngrok http 8000

# Quick start

Run the following commands. You will need Python 3 setup

    git clone https://github.com/Gurupradeep/FBMessengerBot.git
    cd bot
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py runserver

Edit the `VERIFY_TOKEN` variable in `https://github.com/Gurupradeep/FBMessengerBot/blob/master/bot/fb_bot/views.py` to include the Verify token.
It is set to `2318934571` as default that is used in the tutorial. This can be any token as long as it matches the one you tell Facebook.

Once you have your webhook setup, get your Page Access Token. Then set the `PAGE_ACCESS_TOKEN` variable in the file `https://github.com/Gurupradeep/FBMessengerBot/blob/master/bot/fb_bot/views.py` to your page access token. 
