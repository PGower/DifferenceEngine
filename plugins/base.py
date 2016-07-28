class DEPlugin(object):
    pass


class InputPlugin(DEPlugin):
    def load(self):
        raise NotImplemented("The load method must be implemented by all Input plugins")

    def indexes(self):
        raise NotImplemented("The indexes method must be implemented by all Input plugins")

    def schema(self):
        raise NotImplemented("The schema method must be implemented by all Input plugins")


class OutputPlugin(DEPlugin):
    def output(self, data):
        raise NotImplemented("The output method must be implemented by all Output plugins")


class MutatorPlugin(DEPlugin):
    def mutate(self, configuration, data_sources):
        raise NotImplemented("The mutate method must be implemented by all Mutate plugins")
