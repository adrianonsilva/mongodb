import pymongo
import pandas as pd
from pymongo import MongoClient
import datetime

# Registro de exemplo
record = {"name": "Joaquim Jose da Silva Xavier",
        "country": "Brazil",
        "scores": [1, 2, 0, 1, 1, 4, 2, 0, 1],
        "age": 40,
        "date": datetime.datetime.utcnow()}

# conexao local db = dbteste | collection = players
client = MongoClient("localhost", 27017, maxPoolSize=50)
db = client.dbteste
collection = db.players

# adicionar registro
player_id = collection.insert_one(record).inserted_id
print(player_id)

# de mongodb para pandas df 
data = pd.DataFrame(list(collection.find()))

# imprimir 5 primeiras linhas
print(data.head())

