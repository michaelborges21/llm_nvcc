from dotenv import load_dotenv
from pathlib import Path

import os

# Se o .env estiver no mesmo diretório do notebook:
# load_dotenv()


# Se estiver em outro local:
# from pathlib import Path

load_dotenv(dotenv_path=Path('../.env'))

api_key = os.getenv("HUGGING_API_TOKEN")
# print("API_KEY: ", api_key)