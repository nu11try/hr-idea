from slack_sdk.errors import SlackApiError

from views import HomeView, ModalSendIdea, ScheduledView, MessageView
from views.channel_view import ChannelView

users_store = []


def get_users(users_array):
    for user in users_array:
        users_store.append(user["id"])


class ModalViewController:
    @staticmethod
    def handle_get_idea_in_view(ack, body, client, logger):
        ack()
        logger.info(body)
        value = body['view']['state']['values']
        type_idea = value['idea_type']['static_select-action']['selected_option']['text']['text']
        msg_idea = value['idea_msg']['dreamy_input']['value']

        try:
            result = client.chat_postMessage(
                channel='C04CA22JQUV',
                blocks=ChannelView().get_view(type_idea, msg_idea),
                text='Пришла новая идея!',
            )
            logger.info(result)

        except SlackApiError as e:
            logger.error("Ошибка при установки расписания: {}".format(e))


    @staticmethod
    def handle_get_scheduled_in_view(ack, body, client, logger):
        value = body['view']['state']['values']
        scheduled_msg = ''
        scheduled_notif = ''
        schedule_timestamp = value['scheduled_time']['datetimepicker-action']['selected_date_time']
        members = []

        for key, val in value['scheduled_msg_text'].items():
            scheduled_msg = val['value']

        for key, val in value['scheduled_msg_notif'].items():
            scheduled_notif = val['value']

        for key, val in value['members'].items():
            members = val['selected_conversations']

        if len(members) == 0:
            try:
                get_users(client.users_list()['members'])
                members = users_store
            except SlackApiError as e:
                logger.error("Ошибка при получении списка пользователей: {}".format(e))

        for el in members:
            try:
                result = client.chat_scheduleMessage(
                    channel=el,
                    blocks=MessageView().get_message_temp(scheduled_msg),
                    text=scheduled_notif,
                    post_at=schedule_timestamp
                )
                logger.info(result)

            except SlackApiError as e:
                logger.error("Ошибка при установки расписания: {}".format(e))

        logger.info(body)

    # Обработчик выбора типа идеи
    @staticmethod
    def handle_select_type_idea(ack, body, logger):
        ack()
        logger.info(body)

    # Открытие модалки на запись идеи
    @staticmethod
    def open_send_idea_view(ask, body, client):
        ask()
        client.views_open(
            trigger_id=body["trigger_id"],
            view=ModalSendIdea().get_view()
        )

    # Отображение текста на начальном экране
    @staticmethod
    def open_home_view(client, event, logger):
        client.views_publish(
            user_id=event["user"],
            view=HomeView().get_view()
        )

    # Открытие модалки на установки
    @staticmethod
    def open_scheduled_view(ask, body, client):
        ask()
        client.views_open(
            trigger_id=body["trigger_id"],
            view=ScheduledView().get_view()
        )
