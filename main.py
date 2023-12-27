import secrets
from sys import argv

print(secrets.token_hex(int(argv[1])))