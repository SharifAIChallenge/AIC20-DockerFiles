import os

old_get = os.environ.get

def new_get(key, *args, **kwargs):
	value = old_get(key, *args, **kwargs)
	if key == 'AICHostPort':
		return int(value)
	else:
		return value

os.environ.get = new_get

import Controller