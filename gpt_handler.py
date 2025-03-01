import openai
from config import OPENAI_API_KEY

# ตั้งค่า API Key
openai.api_key = OPENAI_API_KEY

def get_gpt_response(user_message):
    """ใช้ GPT-4 สร้างข้อความตอบกลับ"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

