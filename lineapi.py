from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('NA2ths2Q5rK5iqaje9r1jhEGtnXaMbym6CRgyG4bUzGjwYaZ47zsw62KnQ3VvgCS7TEa/YQ6MT1ksL4ZRFt8AnCUm9Sz/HBNlmHmjJ/Aj
w6Hh9KElD7DR7SNv73zeqOkfYxZ+cN8Ag/F+ReUUVoJRgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('https://quiet-gorge-23097.herokuapp.com')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
