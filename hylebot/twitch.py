import irc.bot
import irc.strings
import time
from hylebot.osu import OsuApi
from hylebot.twitchapi import TwitchApi
from hylebot.message import Message

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, host, port, nickname, channel, token, database, mods):
        irc.bot.SingleServerIRCBot.__init__(self, [(host, port, token)], nickname, nickname)
        self.channel = channel
        self.nickname = nickname
        self.db = database
        self.mods = mods

    def on_welcome(self, connection, event):
        print(event)
        connection.join(self.channel)

    def on_privmsg(self, connection, event):
        print(event)

    def on_join(self, connection, event):
        print(event)
    
    def on_pubmsg(self, connection, event):
        print(event)

        if event.arguments[0].startswith("!"):
            message = event.arguments[0].split(" ", 2)
            if (irc.strings.lower(event.source.nick) in self.mods):
                self.do_command_mod(event, message)
            else:
                self.do_command(event, message)

        osu_api = OsuApi()
        converted_message = self.convert_message(event)
        result = osu_api.process_message(converted_message)
        if result:
            self.connection.privmsg(self.channel, result)

    def do_command_mod(self, event, message):
        command = message[0]
        
        if command == "!add" and len(message) > 2:
            if self.db.get(message[1]):
                self.connection.privmsg(self.channel, "Command " + message[1] + " is updated.")
            else:
                self.connection.privmsg(self.channel, "Command " + message[1] + " is added.")
            self.db.set(message[1], message[2])
        elif command == "!delete" and len(message) > 1:
            self.connection.privmsg(self.channel, "Command " + message[1] + " is deleted.")
            self.db.delete(message[1])
        else:
            self.do_command(event, message)

    def do_command(self, event, message):
        command = message[0]

        if command.startswith("!"):
            if command == "!osurank":
                osu_api = OsuApi()
                self.connection.privmsg(self.channel, osu_api.user_rank())
            if command == "!followage":
                twitch_api = TwitchApi()
                self.connection.privmsg(self.channel, twitch_api.get_follow_age(event.source.nick))
            if self.db.get(command):
                self.connection.privmsg(self.channel, self.db.get(command))

    def convert_message(self, event):
        return Message(time.time(), event.source.nick, event.arguments[0], "Twitch", self.channel)
        

                
        
