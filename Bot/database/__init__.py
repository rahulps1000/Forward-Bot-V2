from pymongo import MongoClient
from Bot.config import Config

DB_URL = Config.DB_URI
CLUSTER = Config.SESSION_NAME

class Mongo:
    cluster = MongoClient(DB_URL)
    db = cluster[CLUSTER]