from ezistore.core import *

ROOT_LOG = 'ezi-store'

def init_log(filename='/var/log/ezistore'):
    LOG = logging.getLogger(ROOT_LOG)
    LOG.setLevel(logging.DEBUG)

    handler_file = logging.FileHandler(filename=filename)
    handler_file.setLevel(logging.DEBUG)

    handler_stream = logging.StreamHandler()
    handler_stream.setLevel(logging.INFO)

    formatter_file = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler_file.setFormatter(formatter_file)

    formatter_stream = logging.Formatter('%(message)s')
    handler_stream.setFormatter(formatter_stream)

    LOG.addHandler(handler_file)
    LOG.addHandler(handler_stream)

if __name__ == '__main__':
    ezistored()
