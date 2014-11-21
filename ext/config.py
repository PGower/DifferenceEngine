import yaml
import logging
from configure import Configuration, ConfigurationError
from cerberus import Validator

logger = logging.getLogger(__name__)

class DEConfigValidator(Validator):
    def _validate_defined(self, defined, field, value):
        pass


