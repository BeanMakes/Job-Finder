from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import certifi



import config

class Database:

    def __init__(self):
        pass
    
    def openConnection(self):
        try:
            # MongoClient('mongodb://username:password@hostnameOrReplicaset/?tls=True') replica by your own Service URI
            uri = "mongodb+srv://{}:{}@cluster0.ogm1qsr.mongodb.net/?retryWrites=true&w=majority".format(config.DB_USERNAME,config.DB_PASSWORD)
            ca = certifi.where()

            self.client = MongoClient(uri,tlsCAFile=ca)
            self.client.admin.command('ping')
            
        except Exception as e:
            print("Could not connect to MongoDB")
            print(e)

    def exist_DB(self, nameCompany:str):
        pass

    def get_data(self,colname):
        mydb = self.client[config.DB_NAME]
        mycol = mydb[colname]
        print(mycol)
        result = []
        for x in mycol.find():
            result.append(x)
        return result
    
    def insert_data(self,colname,data):

        ## Add check validation check in here


        db = self.client[config.DB_NAME]

        col = db[colname]

        x = col.insert_many(data)

        print(x.inserted_ids)