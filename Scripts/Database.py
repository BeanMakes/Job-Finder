from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import config

class Database:

    def __init__(self):
        pass
    
    def openConnection(self):
        try:
            # MongoClient('mongodb://username:password@hostnameOrReplicaset/?tls=True') replica by your own Service URI
            uri = 'mongodb+srv://<{}>:<{}>@cluster0.ogm1qsr.mongodb.net/'.format(config.DB_USERNAME,config.DB_PASSWORD)
            connect = MongoClient(uri)
            print("MongoDB cluster is reachable")
            print(connect)
        except ConnectionFailure as e:
            print("Could not connect to MongoDB")
            print(e)
