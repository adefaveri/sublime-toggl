class Cache():
    storage = {}

    @staticmethod
    def store(key, value):
        Cache.storage[key] = value

    @staticmethod
    def retrieve(key):
        if key in Cache.storage:
            return Cache.storage[key]
        else:
            return None

    @staticmethod
    def delete(key):
        if key in Cache.storage:
            del Cache.storage[key]
