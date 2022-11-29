class MessageView:
    @staticmethod
    def get_message_temp(text):
        return [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{text}"
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
                            "text": "Нажми меня скорее! 🤩",
                            "emoji": True
                        }
                    }
                ]
            }
        ]
