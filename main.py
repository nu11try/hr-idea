import json
import logging

import os
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError

from controller import HomeController, ModalViewController, ShortcutController

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

logging.basicConfig(level=logging.DEBUG)

user_scheduled = None

app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    name='RoomIdea'
)


# HOME CONTROLLER
@app.event("app_home_opened")
def open_home(client, event, logger):
    """
    Функция показывает приветствие при открытие домашней страницы бота

    :param client: параметр библиотеки
    :param event: параметр библиотеки
    :param logger: параметр библиотеки
    :return: None
    """
    HomeController().open_home(client, event, logger)


# MODAL CONTROLLER
@app.action("static_select-action")
def handle_some_action(ack, body, logger):
    """
    Функция отвечает за выбор типа идеи

    :param ack: параметр библиотеки
    :param body: параметр библиотеки
    :param logger: параметр библиотеки
    :return: None
    """
    ModalViewController().handle_select_type_idea(ack, body, logger)


@app.view("set_idea_info")
def handle_view_events(ack, body, client, logger):
    """
    Функция отвечает за обработку отправки модального окна (формы) - парсит данные

    :param client: параметр библиотеки
    :param ack: параметр библиотеки
    :param body: параметр библиотеки
    :param logger: параметр библиотеки
    :return: None
    """
    ModalViewController().handle_get_idea_in_view(ack, body, client, logger)


@app.view("set_scheduled")
def handle_scheduled_view_events(ack, body, client, logger):
    ModalViewController().handle_get_scheduled_in_view(ack, body, client, logger)


@app.action("multi_conversations_select-action")
def handle_some_action(ack, body, logger):
    ack()
    logger.info(body)


@app.action("open_idea_view")
def open_idea_view_home(ack, body, client):
    """
    Функция отвечает за появление модального окна (формы) для отправки идеи

    :param ack: параметр библиотеки
    :param body: параметр библиотеки
    :param client: параметр библиотеки
    :return: None
    """
    ack()
    ModalViewController().open_send_idea_view(ack, body, client)


# SHORTCUT CONTROLLER
@app.shortcut("set_idea")
def open_modal(ack, body, client):
    """
    Функция обработки команды /idea

    :param ack: параметр библиотеки
    :param body: параметр библиотеки
    :param client: параметр библиотеки
    :return: None
    """
    ack()
    ShortcutController().open_modal_send_idea(ack, body, client)


@app.shortcut("set_scheduled")
def open_modal(ack, body, client):
    """
    Функция обработки команды /scheduled

    :param ack: параметр библиотеки
    :param body: параметр библиотеки
    :param client: параметр библиотеки
    :return: None
    """
    ack()
    user_id = body['user']['id']
    if user_id not in json.loads(os.getenv('ADMINS')):
        try:
            client.chat_postMessage(
                channel=user_id,
                text='Недостаточно прав для установки расписания! 😞'
            )
        except SlackApiError as e:
            print("Ошибка при отправке сообщения о недостаточных правах: {}".format(e))
    else:
        ShortcutController().open_modal_set_scheduled(ack, body, client)


def main():
    handler = SocketModeHandler(app, os.getenv('SLACK_APP_TOKEN'))
    handler.start()


if __name__ == '__main__':
    main()
