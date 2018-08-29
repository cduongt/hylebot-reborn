class Message:
    def __init__(self, time, sender, content, server, channel):
        self._time = time
        self._sender = sender
        self._content = content
        self._server = server
        self._channel = channel
    
    @property
    def time(self):
        return self._time

    @property
    def sender(self):
        return self._sender
    
    @property
    def content(self):
        return self._content
    
    @property
    def server(self):
        return self._server

    @property
    def channel(self):
        return self._channel