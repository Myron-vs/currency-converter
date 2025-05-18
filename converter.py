import os
import requests
from dotenv import load_dotenv

load_dotenv()
def convert_currency(amount, from_currency, to_currency):
  url = f"https://v6.exchangerate-api.com/v6/{os.getenv('API_KEY')}/pair/{from_currency}/{to_currency}/{amount}"
  response = requests.get(url)
  data=response.json()
  return data
