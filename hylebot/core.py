import hylebot.twitch

class HyleMessage:
    def __init__(self, time, sender, content, server, channel):
        self.time = time
        self.sender = sender
        self.content = content
        self.server = server
        self.channel = channel
    
    def getTime(self):
        return self.time

    def getSender(self):
        return self.sender
    
    def getContent(self):
        return self.content
    
    def getServer(self):
        return self.server

    def getChannel(self):
        return self.channel

class HyleServer:
    def __init__(self, server_type, server, port, name, channels, token):
        self.server_type = server_type
        self.server = server
        self.port = port
        self.name = name
        self.channels = channels
        self.token = token

    def connect(self):
        if self.server_type == "twitch":
            twitch = hylebot.twitch.HyleTwitchBot(self.server, self.port, self.name, self.channels[0], self.token)
            twitch.start()
            return 0
        if self.server_type == "discord":
            return 0