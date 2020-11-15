import pymongo
import pandas as pd
from pymongo import MongoClient

client = MongoClient("192.168.1.100", 27017, maxPoolSize=50)
db = client.dbteste

collection = db.pais
data = pd.DataFrame(list(collection.find()))

print(data.head())

