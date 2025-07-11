import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")