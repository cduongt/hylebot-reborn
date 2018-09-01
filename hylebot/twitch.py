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
        message = event.arguments[0].split(" ", 2)
        if (irc.strings.lower(event.source.nick) in self.mods):
            self.do_command_mod(message)
        else:
            self.do_command(message)

    def do_command_mod(self, message):
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
            self.do_command(message)

    def do_command(self, message):
        command = message[0]

        if command.startswith("!"):
            if self.db.get(command):
                self.connection.privmsg(self.channel, self.db.get(command))

                
        