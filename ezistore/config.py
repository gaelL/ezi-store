import ConfigParser
import logging
from ezistore.tools import merge, InvalidMode

ROOT_LOG = 'ezi-store'

class Config(object):
    def __init__(self, filename):
        self._LOG = logging.getLogger("%s.%s" % (ROOT_LOG, self.__class__.__name__)) 
        self._filename = filename
        self._conf = ConfigParser.ConfigParser()
        self._conf.read(filename)

    def load(self, default_config = {}):
        configured = {}
        for name_section in self._conf.sections():
            configured[name_section] = dict(self._conf.items(name_section))
        merged_config = merge(default_config, configured)
        try:
            if (merged_config['global']['mode'] != 'client') and (merged_config['global']['mode'] != 'server'):
                self._LOG.error("Invalide mode in configuration : %s" % merged_config['global']['mode'])
                return None
#TODO: improve this part as id and fingerprint are the same for both public and secret key
            if merged_config['global']['mode'] == 'client':
                if (('server_public_key' not in merged_config['gpg'].keys()) or
                   ('client_secret_key' not in merged_config['gpg'].keys()) or
                   ('client_public_key' not in merged_config['gpg'].keys())):
                    self._LOG.error("error client gpg")
                    return None
            elif merged_config['global']['mode'] == 'server':
                if (('server_public_key' not in merged_config['gpg'].keys()) or
                   ('server_secret_key' not in merged_config['gpg'].keys()) or
                   ('client_public_key' not in merged_config['gpg'].keys())):
                    self._LOG.error("error server gpg")
                    return None
        except KeyError as err:
            self._LOG.error("Missing parameter in configuration: %s" % err)
            return None
        return merged_config
