import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('5022003712', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
