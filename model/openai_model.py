import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv()


def create_client():
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    return client
