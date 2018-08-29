import irc.bot
import hylebot.osu
import hylebot.message

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, host, port, nickname, channel, token, database):
        irc.bot.SingleServerIRCBot.__init__(self, [(host, port, token)], nickname, nickname)
        self.channel = channel
        self.nickname = nickname
        self.db = database

    def on_welcome(self, connection, event):
        print(event)
        connection.join(self.channel)

    def on_privmsg(self, connection, event):
        print(event)

    def on_join(self, connection, event):
        print(event)
    
    def on_pubmsg(self, connection, event):
        print(event)
                
        