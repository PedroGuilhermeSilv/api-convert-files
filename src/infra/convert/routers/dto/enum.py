from enum import Enum


class TypeInput(str, Enum):
    csv = 'csv'
    xlsx = 'xlsx'
    json = 'json'

class TypeOutput(str, Enum):
    csv = 'csv'
    xlsx = 'xlsx'
    json = 'json'

class AllTypes(str, Enum):
    csv = 'csv'
    xlsx = 'xlsx'
    json = 'json'