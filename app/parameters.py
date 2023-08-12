from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
USERNAME = os.getenv("USERNAME_DB")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
PORT = os.getenv("PORT")