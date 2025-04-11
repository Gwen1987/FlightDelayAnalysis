from dotenv import load_dotenv        # pip install dotenv
import os

load_dotenv()

config = { }

def load_faa():
  if os.environ.get('FAA_API_KEY', None) is None:
    raise 'FAA_API_KEY does not exist.'
  config['FAA_API_KEY'] = os.environ.get('FAA_API_KEY')

def load_mongo():
  if os.environ.get('DB_PASS', None) is None:
    raise 'DB_PASS does not exist.'

  if os.environ.get('MONGO_DB_PASS', None) is None:
    raise 'MONGO_DB_PASS does not exist.'

  config['MONGO_DB_PASS'] = os.environ.get('MONGO_DB_PASS')
  config['MONGO_DB_USER'] = os.environ.get('MONGO_DB_USER')
  config['DB_PASS'] = os.environ.get('DB_PASS')



load_faa()
load_mongo()

