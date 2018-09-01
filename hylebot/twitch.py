import irc.bot
import irc.strings
import hylebot.osu
import hylebot.message

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
        if (irc.strings.lower(event.source.nick) in self.mods):
            self.do_command(event)

    def do_command(self, event):
        connection = self.connection
        message = event.arguments[0].split(" ", 2)
        command = message[0]
        
        if command == "!add" and len(message) > 2:
            if self.db.get(message[1]):
                connection.privmsg(self.channel, "Command " + message[1] + " is updated.")
            else:
                connection.privmsg(self.channel, "Command " + message[1] + " iss added.")
            self.db.set(message[1], message[2])
        elif command == "!delete" and len(message) > 1:
            connection.privmsg(self.channel, "Command " + message[1] + " is deleted.")
            self.db.delete(message[1])
        elif command.startswith("!"):
            if self.db.get(command):
                connection.privmsg(self.channel, self.db.get(command))

                
        