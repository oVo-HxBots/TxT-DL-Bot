import re, os, time
import datetime

class Config:
    BOT_TOKEN = environ.get('BOT_TOKEN')
    API_HASH = environ.get('API_HASH')
    API_ID = int(environ.get('API_ID'))
    OWNER_ID = int(environ.get('OWNER_ID')) #Admin UserId
    DB_URI = environ.get('DB_URI') #May Be In Future.
    
