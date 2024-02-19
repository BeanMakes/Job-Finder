from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import config

class Database:

    def __init__(self):
        pass
    
    def openConnection(self):
        try:
            # MongoClient('mongodb://username:password@hostnameOrReplicaset/?tls=True') replica by your own Service URI
            uri = "mongodb+srv://{}:{}@cluster0.ogm1qsr.mongodb.net/?retryWrites=true&w=majority".format(config.DB_USERNAME,config.DB_PASSWORD)
            self.client = MongoClient(uri)
            print("MongoDB cluster is reachable")
            print(self.client)

            
        except ConnectionFailure as e:
            print("Could not connect to MongoDB")
            print(e)

    def exist_DB(self, nameCompany:str):
        pass

    def insert_data(self,data):

        ## Add check validation check in here


        db = self.client["JobFinderdatabase"]

        col = db['companies']

        x = col.insert_many(data)

        print(x.inserted_ids)