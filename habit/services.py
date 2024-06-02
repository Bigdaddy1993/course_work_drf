import os
import requests
from dotenv import load_dotenv

load_dotenv()


class TgBot:
    token = os.getenv("TOKEN_TG")
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    def send_habit(self, text, chat_id):
        """Отправки сообщений пользователю в телеграм"""
        requests.post(
            url=f"{self.url}{self.token}/sendMessage",
            data={"chat_id": chat_id, "text": text},
        )
