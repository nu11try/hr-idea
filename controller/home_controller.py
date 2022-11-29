from controller import ModalViewController


class HomeController:
    @staticmethod
    def open_home(client, event, logger):
        try:
            ModalViewController().open_home_view(client, event, logger)
        except Exception as e:
            logger.error(f"Ошибка при создании view главной страницы: {e}")
