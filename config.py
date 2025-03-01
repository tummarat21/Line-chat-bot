import os
from dotenv import load_dotenv

# โหลดตัวแปรจากไฟล์ .env
load_dotenv()

# ตั้งค่าคีย์จาก .env
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN", "TOKEN_NOT_FOUND")
LINE_SECRET = os.getenv("LINE_SECRET", "SECRET_NOT_FOUND")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "OPENAI_KEY_NOT_FOUND")

