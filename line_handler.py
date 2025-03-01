from linebot import LineBotApi
from linebot.models import TextSendMessage
from config import LINE_ACCESS_TOKEN

line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)

def send_message_to_group(group_id, message):
    """ส่งข้อความไปยังกลุ่ม"""
    try:
        line_bot_api.push_message(group_id, TextSendMessage(text=message))
        return "✅ ส่งข้อความสำเร็จ"
    except Exception as e:
        return f"❌ LINE API Error: {str(e)}"

