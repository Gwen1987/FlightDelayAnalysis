from utils import config

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = f"mongodb+srv://FlightUsers:{config['MONGO_DB_PASS']}@flightcluster.nq9yvyo.mongodb.net/?retryWrites=true&w=majority&appName=FlightCluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)