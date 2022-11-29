class ChannelView:
    @staticmethod
    def get_view(idea_type, idea_msg):
        return [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "🔥Пришла новая идея!🔥"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Процесс:* {idea_type}',
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'*Идея:* {idea_msg}',
                }
            },
            {
                "type": "divider"
            }
        ]
