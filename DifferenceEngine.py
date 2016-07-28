import argparse
from os import path

from configure import Configuration

from codernity.database import Database

import logging
logger = logging.getLogger(__name__)


class DBWrapper(object):
    def __init__(self, collection, db):
        pass


class DifferenceEngine(object):
    def __init__(self, options, config):
        self.options = options
        self.config = config
        self.logger = logging.getLogger(__name__)

    def _init_database(self, options, config):
        '''Initialize the database object, creating it and the indexes if necessary'''
        db = Database(options['db-path'])
        if db.exists():
            db.open()
        else:
            db.create()
        self.db = db
        self._init_indexes(self.db, config)

    def _init_indexes(self, db, config):
        '''Given an open database and the loaded config check that the database contains indexes as defined in the config'''
        # Existing DB Indexes
        details = db.get_db_details()
        indexes = details['indexes']
        # Proposed New Indexes
        required_indexes = []
        for k, v in config['common']['input'].items():
            try:
                required_indexes.append(v['index'])
            except KeyError:
                self.logger.exception("DB ")






        

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
    db_group.add_argument('-edb', '--empty-db', action="store_true", help="Delete all entries from the _id index. Leaves indexes intact. WARNING: Be careful with this.")
    db_group.add_argument('-db', '--db-path', action="store", type=lambda p: path.abspath(p), help="Where to store the internal db. If a file already exists at this path it will be used otherwise a new db file will be created.")
    db_group.add_argument('-did', '--drop-indexes', action="store_true", help="Delete all indexes from the internal db. Implies --empty-db as well. WARNING: Will delete all data.")
    return parser


def validate_configuration(options):
    # must have 3 sections common



if __name__ == '__main__':
    parser = build_argument_parser()
    options = parser.parse_args()
    config = Configuration.from_file(options.config)
    