import irc.bot

class HyleTwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, name, channel, token):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], name, name)
        self.channel = channel

    def on_welcome(self, c, e):
        print(e)
        c.join(self.channel)

    def on_privmsg(self, c, e):
        print(e)

    def on_pubmsg(self, c, e):
        print(e)