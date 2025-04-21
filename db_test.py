from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://guest:guest@flightcluster.nq9yvyo.mongodb.net/?retryWrites=true&w=majority&appName=FlightCluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    db = client['flight_db']
    coll = db['flight_coll']
    for i, d in enumerate(coll.find({'OriginStateName': 'Colorado'})):
        print(d)
        if i == 5:
            break
except Exception as e:
    print(e)

