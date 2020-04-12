# basic-pyro-bot
This is a basic layer for building bots by using Pyrogram. No, really, that's just it.

## WARNING!
This repository includes a configuration file with standard API ID and API hash, extracted from the official Telegram app for Android. Their use is intended only for bots: **NEVER, EVER, EVER, EVER, EVER, EVER, EVER USE THEM FOR A USER ACCOUNT, IT WILL BE IMMEDIATELY TERMINATED. BE VERY CAREFUL!**

However, you can create your own pair from [my.telegram.org](my.telegram.org) and insert it in the `config.ini` file.

## Dependencies
Required:
- `python3.7`

Optional, but recommended:
- `python3.7-dev` (Linux)
- `gcc/clang` (Linux) or `Visual C++ 2015 Build Tools` (Windows, available [here](http://landinghub.visualstudio.com/visual-cpp-build-tools))

## Installation
Run this command from command-line:
```bash
$ python3.7 -m pip install --user -r requirements.txt
```

## TgCrypto
By default, Pyrogram will use the PyAES library for crypto, but it's quite slow. However, the speed can be dramatically boosted up by TgCrypto, a high-performance, easy-to-install Telegram Crypto Library specifically written in C for Pyrogram. Although not necessary, installation is strongly advised.

Install optional depencencies first, then run the following command:
```bash
$ python3.7 -m pip install --user --upgrade tgcrypto
```

## Running
Just run this:
```bash
$ python3.7 bot.py
```