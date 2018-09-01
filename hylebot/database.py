import redis

class Database():
    def __init__(self, host, port, db):
        self._database = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)
    
    def set(self, key, value):
        self._database.set(key, value)

    def get(self, key):
        return self._database.get(key)

    def delete(self, key):
        self._database.delete(key)