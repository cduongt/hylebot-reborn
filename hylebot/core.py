import hylebot.twitch
import irc.bot
import sys
import os
from hylebot.config import config
from hylebot.database import Database

class Server:
    def __init__(self):
        self.server_type = config['CORE']['SERVER_TYPE']
        self.host = config['SERVER']['HOST']
        self.port = int(config['SERVER']['PORT'])
        self.nickname = config['SERVER']['NICKNAME']
        self.channels = config['SERVER']['CHANNELS']
        self.token = config['SERVER']['TOKEN']
        redis_host = os.environ.get('REDIS_HOST')
        redis_port = os.environ.get('REDIS_PORT')
        redis_db = os.environ.get('REDIS_DB')
        self.database = Database(redis_host, redis_port, redis_db)
        self.mods = [mod.lower() for mod in config['SERVER']['MODS'].split(",")]

    def connect(self):
        if self.server_type == "Twitch":
            bot = hylebot.twitch.TwitchBot(self.host, self.port, self.nickname, self.channels, self.token, self.database, self.mods)
            bot.start()
    
        if self.server_type == "Discord":
            return 0