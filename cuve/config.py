from typing import Type, Dict

import yaml
import marshmallow as ma

#
# Config schemas
#

class DatabaseSection(ma.Schema):
    host = ma.fields.String(required=True)
    port = ma.fields.Integer(default=5432)

    user = ma.fields.String(required=True)
    password = ma.fields.String()
    database = ma.fields.String(required=True)

    minsize = ma.fields.Integer(default=10)
    maxsize = ma.fields.Integer(default=100)


class ConfigSchema(ma.Schema):
    database = ma.fields.Nested(DatabaseSection, required=True)


#
# Config loader
#


class ImproperlyConfigured(Exception):
    pass


def load_config(schema_cls: Type[ma.Schema], path: str) -> Dict:
    """
    Return YAML file as a Python dict validated against marshmallow schema

    >>> load_config()['database']
    {'db': 'top100', 'host': 'localhost', 'user': 'test'}

    :param path: str (path to YAML config file)
    :return: dict
    """
    with open(path, 'r') as ymlfile:
        unvalidated_config = yaml.load(ymlfile)

    if unvalidated_config is None:
        raise ImproperlyConfigured('Missing configuration')

    schema = schema_cls(strict=True)

    try:
        # validated config
        return schema.load(unvalidated_config).data
    except ma.ValidationError as exc:
        raise ImproperlyConfigured(str(exc))
