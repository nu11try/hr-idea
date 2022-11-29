from controller import ModalViewController


class ShortcutController:
    @staticmethod
    def open_modal_send_idea(ack, body, client):
        ack()
        ModalViewController().open_send_idea_view(ack, body, client)

    @staticmethod
    def open_modal_set_scheduled(ack, body, client):
        ack()
        ModalViewController().open_scheduled_view(ack, body, client)
