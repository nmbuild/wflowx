from typing import Dict
from ci_converter.parsers.base import Parser
from ci_converter.generators.base import Generator

PARSERS: Dict[str, Parser] = {}
GENERATORS: Dict[str, Generator] = {}

def register_parser(key: str, parser: Parser):
    PARSERS[key] = parser

def get_parser(key: str) -> Parser:
    return PARSERS[key]

def register_generator(key: str, gen: Generator):
    GENERATORS[key] = gen

def get_generator(key: str) -> Generator:
    return GENERATORS[key]