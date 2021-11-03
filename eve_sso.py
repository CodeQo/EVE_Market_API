import ast
import mock
import time
import requests
from my_fix import my_update
from esipy import EsiSecurity, EsiClient, EsiApp
from esipy.cache import FileCache
from esipy.utils import generate_code_verifier
from configparser import ConfigParser


def esi_sec(configfile):
    cache = FileCache(path=configfile['general']['cache_path'])
    header = {'User-Agent': configfile['eve']['user-agent']}
    esi_security = EsiSecurity(
        redirect_uri='https://oauth.pstmn.io/v1/callback',
        client_id=configfile['eve']['client_id'],
        code_verifier=generate_code_verifier(),
        headers=header,
        sso_endpoints=cache.get('sso_endpoint', None),
        jwks_key=cache.get('jwks', None)
    )
    return esi_security


def create_auth(esisec_obj, configfile):
    eve_sso_auth_url = esisec_obj.get_auth_uri(
        state=configfile['eve']['state'],
        scopes=ast.literal_eval(configfile['eve']['scopes'])
    )
    print('Created authorization URL:')
    print(eve_sso_auth_url)
    copycode = input('Enter the copied code from callback URL: ')
    token = esisec_obj.auth(copycode)
    configfile['token']['token'] = str(token)
    jwk = esisec_obj.verify()
    configfile['token']['jwk'] = str(jwk)
    configfile.write(open('eve_app.ini', 'w'))


def update_access(esisec, configfile):
    jwk = ast.literal_eval(configfile['token']['jwk'])
    expiry = jwk['exp']
    if expiry > (time.time()-1):
        esisec.refresh()


def update_sso_cache(configfile):
    cache = FileCache(path=configfile['general']['cache_path'])
    discovery_url = configfile['eve']['discovery_url']

    # get the SSO endpoints data
    res = requests.get(discovery_url)
    res.raise_for_status()
    sso_endpoints = res.json()
    # get the JWKS. JWKS url is in the SSO discovery response
    jwks_url = sso_endpoints['jwks_uri']
    res = requests.get(jwks_url)
    res.raise_for_status()
    jwks = res.json()
    # Caching data
    cache.set('sso_endpoints', sso_endpoints, 86400)
    cache.set('jwks', jwks, 86400)


eve_config = ConfigParser()
eve_config.read('eve_app.ini')
#time.time()

@mock.patch('time.time()')
def test_method():
    print('in')

test_method()
print(time.time())
#update_sso_cache(eve_config)
#esi_sec(eve_config)

"""""
print(eve_sso_auth_url)
print('Enter the copied access token here:')
copycode = input()
tokens = esi_security.auth(copycode)
print(tokens)
api_info = esi_security.verify()
print(api_info)

input('Any Key')


# and to see the data behind, let's print it

print('update token')
esi_security.update_token(tokens)

print('Refresh')
tokens = esi_security.refresh()

print(tokens)
print('Create Client')
client = EsiClient(security=esi_security,
                   headers={'User-Agent':'adsd'})
print('Create App')
app = EsiApp().get_latest_swagger
print('Create op')
op = app.op['get_characters_character_id_wallet'](
     character_id=api_info['sub'].split(':')[-1]
 )
print('op')
print(op)
print('Wallet request')
wallet = client.request(op)
print('wallet print')
print(wallet.data)
"""
