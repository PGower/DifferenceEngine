from yapsy.IPlugin import IPlugin


class IInputPlugin(IPlugin):
    def __init__(self, db):
        self.db = db

    def load(self):
        pass

    def indexes(self):
        pass


class IProcessingPlugin(IPlugin):
    def __init__(self, source_db, destination_db):
        self.source_db = source_db
        self.destination_db = destination_db

    def process(self):
        pass


class IOutputPlugin(IPlugin):
    def __init__(self, db):
        self.db = db

    def generate(self, old_data, new_data, action):
        pass


class DBWrapper(object):
    def __init__(self, collection, db, )

class DifferenceEngine(object):
    def __init__(self, config):
        self.config = config
        