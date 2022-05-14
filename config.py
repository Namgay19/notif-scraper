from configparser import ConfigParser
import pathlib

def config(section='postgresql'):
    # create a parser
    parser = ConfigParser()
    
    # read config file
    dir = str(pathlib.Path(__file__).parent.resolve())
    filename = dir + "/database.ini"
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
