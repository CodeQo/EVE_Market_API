import ast
import configparser

from dotenv import load_dotenv
from ast import literal_eval
from dblib import connect
from dotenv import get_cli_string
import xlwings
from configparser import ConfigParser
import os
import requests

load_dotenv()

# This file is not used in dev. eve_sso.py current development
config_eve_app = configparser.ConfigParser()
config_eve_app.read_file(open('eve_app.ini'))

token = "{'mock'}"
token_dict = {'mock'}
token_strip = requests.get('token').json()
print(token_strip['access_token'])
config_eve_app.set('token', 'token', str(token_dict))

old_refresh_token = config_eve_app.get('token', 'token')
old = ast.literal_eval((old_refresh_token))
print(old)
print(type(old))

config_eve_app.write(open('eve_app.ini', 'w'))
"""""
# Database
conn = connect()
cur = conn.cursor()

# Select which program to run
print('Select an option: \n'
      '1) \n'
      '2) \n'
      '3)')
choice = input()
if choice == '1':
    print("First option")
elif choice == '2':
    print("Second option")
elif choice == '3':
    print("Third option")
else:
    print("Selection aborted")

# Main program

# End program
print('Press any key to close db')
input()
conn.close()
"""




