import yaml
import logging
from configure import Configuration, ConfigurationError
from cerberus import Validator

logger = logging.getLogger(__name__)

class DEConfigValidator(Validator):
    def _validate_definedinput(self, defined, field, value):
        pass


def validate(config_path):
    try:
        config = Configuration.configure(config_path)
    except ConfigurationError as ce:
        logger.exception(ce)
    try:
        with open('config.schema.yaml', 'r') as f:
            schema = yaml.load(f)
    except:
        
    schema = yaml.load('')
    v = DEConfigValidator