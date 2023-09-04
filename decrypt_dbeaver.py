#!/usr/bin/env python3

# Original source: https://gist.github.com/felipou/50b60309f99b70b1e28f6d22da5d8e61
# https://stackoverflow.com/questions/39928401/recover-db-password-stored-in-my-dbeaver-connection

import sys
import os
import json
from Crypto.Cipher import AES
from prettytable import PrettyTable, SINGLE_BORDER

default_paths = [
        '~/Library/DBeaverData/workspace6/General/.dbeaver/',
        '~/.local/share/DBeaverData/workspace6/General/.dbeaver/',
        '~/.local/share/.DBeaverData/workspace6/General/.dbeaver/',
        '~/AppData/Roaming/DBeaverData/workspace6/General/.dbeaver/'
        ]

if len(sys.argv) < 2:
    for path in default_paths:
        dirpath = os.path.expanduser(path)
        if os.path.exists(dirpath):
            break
else:
    dirpath = sys.argv[1]

print('Extracting credentials from: ' + dirpath)

PASSWORD_DECRYPTION_KEY = bytes([186, 187, 74, 159, 119, 74, 184, 83, 201, 108, 45, 101, 61, 254, 84, 74])

with open(os.path.join(dirpath, 'data-sources.json'), 'r', encoding='utf-8') as f:
    datasource_config = json.load(f)

with open(os.path.join(dirpath, 'credentials-config.json'), 'rb') as f:
    data = f.read()
    decryptor = AES.new(PASSWORD_DECRYPTION_KEY, AES.MODE_CBC, data[:16])
    padded_output = decryptor.decrypt(data[16:])
    output = padded_output.rstrip(padded_output[-1:])
    credentials_config = json.loads(output)

o = PrettyTable()
o.align = 'l'
o.set_style(SINGLE_BORDER)
o.field_names = ['driver', 'name', 'user', 'password', 'url']
for connection in datasource_config['connections']:
    conf = datasource_config['connections'][connection]
    try:
        cred = credentials_config[connection]['#connection']
        user = cred['user']
        password = cred['password']
    except KeyError:
        user = ''
        password = ''
    o.add_row([conf['driver'], conf['name'], user, password, conf['configuration']['url']])

print(o)
