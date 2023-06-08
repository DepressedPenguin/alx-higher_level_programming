#!/usr/bin/python3
import dis
import hidden_4
if __name__ == "__main__":
    checkid = [checkid for checkid in dir(hidden_4)]
    save_names = sorted(checkid)
    for checkid in save_names:
        if not checkid.startswith('__'):
            print(checkid)
