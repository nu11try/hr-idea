class HomeView:
    @staticmethod
    def get_view():
        return {
            "type": "home",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Добро пожаловать на главную страницу _Приемная Идей_* :tada:"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Данный бот служит для сборка идей по улучшению процессов в компании!\nНе "
                                "стесняйся! Скорее отправь нам свою крутую идею!🙏\nP.S. это можно сделать "
                                "нажав кнопку ниже или отправить `/idea` в чат.\nУспехов!🥹"
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "action_id": "open_idea_view",
                            "text": {
                                "type": "plain_text",
                                "text": "Отправить идею!✌🏻",
                                "emoji": True
                            }
                        }
                    ]
                }
            ]
        }
