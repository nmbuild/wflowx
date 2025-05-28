PARSERS = {}
GENERATORS = {}

def register_parser(name, cls):
    PARSERS[name] = cls()

def register_generator(name, cls):
    GENERATORS[name] = cls()

def get_parser(name): return PARSERS[name]
def get_generator(name): return GENERATORS[name]
