import hylebot.twitch
import irc.bot
import sys
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
        self.database = Database(config['DATABASE']['HOST'], config['DATABASE']['PORT'], config['DATABASE']['DB'])

    def connect(self):
        if self.server_type == "Twitch":
            bot = hylebot.twitch.TwitchBot(self.host, self.port, self.nickname, self.channels, self.token, self.database)
            bot.start()
    
        if self.server_type == "Discord":
            return 0