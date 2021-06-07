from time import sleep
from urllib.request import urlopen
# import http
err = True
while err:
    try:
        response_raw = urlopen(
            '').read().decode('utf-8')
        err = False
        print('\007')
    except Exception:
        import traceback
        print("got error "+traceback.format_exc())
        sleep(10)
        err = True
