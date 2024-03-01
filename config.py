import re, os, time
import datetime

class Config:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    API_HASH = os.environ.get('API_HASH')
    API_ID = int(os.environ.get('API_ID'))
    OWNER_ID = int(os.environ.get('OWNER_ID')) #Admin UserId
    DB_URI = os.environ.get('DB_URI') #May Be In Future.
    
