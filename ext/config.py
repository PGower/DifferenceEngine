import yaml
import logging
from configure import Configuration, ConfigurationError

logger = logging.getLogger(__name__)

def validate_config(config_path):
    try:
        config = Configuration.from_file(config_path)
        except ConfigurationError as

