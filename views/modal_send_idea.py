class ModalSendIdea:
    @staticmethod
    def get_view():
        return {
            "type": "modal",
            "callback_id": "set_idea_info",
            "title": {"type": "plain_text", "text": "Приемная идей"},
            "submit": {"type": "plain_text", "text": "Отправить идею!"},
            "close": {
                "type": "plain_text",
                "text": "Закрыть",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Дружочек, привет🙂\nЯ - бот, который собирает идеи от команды!\nУ тебя есть идеи как улучшить процесс работы🤔, а может ты знаешь как сделать продукт круче🔝, или ты понимаешь, что мы где-то сильно косячим и не знаешь кому про это сказать🙈?\nЧего ждешь?\n Пиши скорее мне, помоги команде Jump стать лучше❤️"
                    }
                },
                {
                    "type": "section",
                    "block_id": "idea_type",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Выбери тему: "
                    },
                    "accessory": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Тема",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "💼 Продукт",
                                    "emoji": True
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "🎭 Корп. культура",
                                    "emoji": True
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "🛠 Рабочий процесс",
                                    "emoji": True
                                },
                                "value": "value-2"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "🏵 Другое",
                                    "emoji": True
                                },
                                "value": "value-3"
                            }
                        ],
                        "action_id": "static_select-action"
                    }
                },
                {
                    "type": "input",
                    "block_id": "idea_msg",
                    "label": {
                        "type": "plain_text",
                        "text": "Напиши сюда свои идеи!"
                    },
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "dreamy_input",
                        "multiline": True
                    }
                }
            ]
        }