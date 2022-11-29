class ScheduledView:
    @staticmethod
    def get_view():
        return {
            "type": "modal",
            "callback_id": "set_scheduled",
            "submit": {
                "type": "plain_text",
                "text": "Создать расписание"
            },
            "close": {
                "type": "plain_text",
                "text": "Закрыть",
                "emoji": True
            },
            "title": {
                "type": "plain_text",
                "text": "Устновка расписания",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "block_id": "scheduled_msg_notif",
                    "label": {
                        "type": "plain_text",
                        "text": "Какое уведомление рассылать?",
                        "emoji": True
                    },
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True
                    },
                    "optional": False
                },
                {
                    "type": "input",
                    "block_id": "scheduled_msg_text",
                    "label": {
                        "type": "plain_text",
                        "text": "Какое сообщение рассылать?",
                        "emoji": True
                    },
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True
                    },
                    "optional": False
                },
                {
                    "type": "input",
                    "block_id": "scheduled_time",
                    "element": {
                        "type": "datetimepicker",
                        "action_id": "datetimepicker-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Когда делать рассылку?",
                        "emoji": True
                    }
                },
                {
                    "type": "section",
                    "block_id": "members",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Выбери кому отправлять\n(если не указать, отправится всем!)"
                    },
                    "accessory": {
                        "type": "multi_conversations_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select conversations",
                            "emoji": True
                        },
                        "action_id": "multi_conversations_select-action"
                    }
                }
            ]
        }
