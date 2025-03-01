import os
from fastapi import FastAPI, Request, HTTPException
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from config import LINE_ACCESS_TOKEN, LINE_SECRET
import openai

app = FastAPI()

# LINE API
line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
parser = WebhookParser(LINE_SECRET)

@app.get("/")
def home():
    return {"message": "LINE Chatbot is running on Railway!"}

@app.post("/webhook")
async def webhook(request: Request):
    """รับ Webhook จาก LINE"""
    signature = request.headers.get("X-Line-Signature")
    if not signature:
        raise HTTPException(status_code=400, detail="Missing X-Line-Signature header")

    body = await request.body()
    try:
        events = parser.parse(body.decode("utf-8"), signature)
        for event in events:
            if isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
                user_message = event.message.text
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": user_message}]
                )
                reply_text = response["choices"][0]["message"]["content"]
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
        return {"status": "success"}
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

