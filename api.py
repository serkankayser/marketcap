from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('API_KEY')


def api():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

  parameters = {
      'limit': '10',
      'convert':'RON'
  }

  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
  return data