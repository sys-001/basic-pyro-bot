#!/usr/bin/env python3.7

import signal
from pyrogram import Client, Filters
import utils

app = Client('spyro')  # I hope you get it, heh

manager = utils.DatabaseManager(utils.db)

authorized_chats = manager.get_admins() + manager.get_authorized_chats()


# noinspection PyUnusedLocal
def signal_handler(handled_signal, frame):
    print('Stopping client...')
    try:
        app.stop()
    except ConnectionError:
        pass
    print('Stopped.')
    exit(0)


@app.on_message()
def on_any(client, message):
    manager.save_chat(message['chat']['id'])
    manager.save_user(message['from']['id'])
    message.continue_propagation()


@app.on_message(Filters.command(['start', 'help'], ['/', '!', '.']) & Filters.chat(authorized_chats))
def on_command(client, message):
    print(message)


@app.on_callback_query()
def on_callback_query(client, callback_query):
    print(callback_query)


@app.on_message(~Filters.chat(authorized_chats) & (Filters.group | Filters.channel))
def on_unauthorized(client, message):
    print(f'Leaving chat {message["chat"]["title"]} [{message["chat"]["id"]} - {message["chat"]["username"]}]')
    app.leave_chat(message['chat']['id'])


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

app.run()
