import argparse
from os import path
from configure import Configuration


class DBWrapper(object):
    def __init__(self, collection, db):
        pass


class DifferenceEngine(object):
    def __init__(self, options, config):
        self.config = config
        

def build_argument_parser():
    parser = argparse.ArgumentParser(description="DifferenceEngine, a framework for generating actions based on changes in a datasource")
    parser.add_argument('-c', '--config', action="store", type=str, default="./config.yaml", help="Path to the configuration file to use. Defaults to ./config.yaml")
    parser.add_argument('-v', '--verbose', action="store_true", help="Produce verbose output during processing.")
    parser.add_argument('-d', '--debug', action="store_true", help="Produce debug level output during processing. This will generate huge amounts of text.")
    plugin_group = parser.add_argument_group("Plugins")
    plugin_group.add_argument('-skm', '--skip-mutators', action="store_true", help="Skip and do not process all mutator plugins")
    plugin_group.add_argument('-sko', '--skip-output', action="store_true", help="Skip and do not process all output plugins")
    plugin_group.add_argument('-ski', '--skip-input', action="append", type=str, default=[], help="Skip any plugins with matching names.")
    db_group = parser.add_argument_group("Interal DB")
    db_group.add_argument('-edb', '--empty-db', action="store_true", help="Empty the internal DB of all entries. WARNING: Be careful with this.")
    db_group.add_argument('-db', '--db-path', action="store", type=str, help="Where to store the internal db. If a file already exists at this path it will be used otherwise a new db file will be created.")
    return parser

if __name__ == '__main__':
    parser = build_argument_parser()
    options = parser.parse_args()
    config = Configuration.from_file(options.config)
    