import pymongo
import pandas as pd
from pymongo import MongoClient
import datetime

# conexao local db = dbteste | collection = players
client = MongoClient("localhost", 27017, maxPoolSize=50)
db = client.dbteste
collection = db.players

############################## INSERIR UM REGISTRO #####################################
print("INSERIR UM REGISTRO")

record = {"name": "Joaquim Jose da Silva Xavier",
        "country": "Brazil",
        "scores": [1, 2, 0, 1, 1, 4, 2, 0, 1],
        "age": 40,
        "date": datetime.datetime.utcnow()}

# verifica se o registro nao existe e adiciona registro
if(collection.count_documents({"name": "Joaquim Jose da Silva Xavier"}) < 1):
        player_id = collection.insert_one(record).inserted_id
        print("id:", player_id)

# de mongodb para pandas df 
data = pd.DataFrame(list(collection.find()))

# imprimir 5 primeiras linhas
print(data.head())

############################# INSERIR VARIOS REGISTROS ###################################
print("\nINSERIR VARIOS REGISTROS")

more_players = [{"name": "John Hampden",
                "country": "England",
                "scores": [3, 0, 1, 0, 0, 3, 0, 2, 1],
                "age": 48,
                "date": datetime.datetime.utcnow()},
                {"name": "John Woolman",
                "country": "United States of America",
                "scores": [0, 2, 0, 1, 5, 2, 2, 0, 0],
                "age": 51,
                "date": datetime.datetime.utcnow()}]

# verifica se os registro nao existem e adiciona os registros
flag_one = collection.count_documents({"name": "John Hampden"}) < 1
flag_two = collection.count_documents({"name": "John Woolman"}) < 1

if(flag_one & flag_two):
        result = collection.insert_many(more_players)
        print("ids:", result.inserted_ids)

# de mongodb para pandas df 
data = pd.DataFrame(list(collection.find()))

# imprimir 5 primeiras linhas
print(data.head())

############################# EXCLUIR UM REGISTRO ###################################
print("\nEXCLUIR UM REGISTRO")
myquery = { "name": "Joaquim Jose da Silva Xavier"}
collection.delete_one(myquery)

# de mongodb para pandas df 
data = pd.DataFrame(list(collection.find()))

# imprimir 5 primeiras linhas
print(data.head())

############################# EXCLUIR VARIOS REGISTROS ###################################
print("\nEXCLUIR VARIOS REGISTROS")
collection.delete_many({})

# de mongodb para pandas df 
data = pd.DataFrame(list(collection.find()))

# imprimir 5 primeiras linhas e a quantidade de registros no db
print(data.head())
print(collection.count_documents({}))