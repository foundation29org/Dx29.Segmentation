import json
import time
import requests

from Lib import DocSegmentation

DOCKER = False

ENDPOINT = "http://localhost:8080/api/v1"

DOCUMENT = 'Document2'

'''
    Post request
'''
def post_request(path, json, headers=None):
    url = F'{ENDPOINT}/{path}'
    headers = headers or {}
    headers['Content-Type'] = 'application/json'
    response = requests.post(url, json=json, headers=headers)
    if response.ok:
        return response.json()
    else:
        raise Exception(str(response))

'''
    Split Document Segments
'''
def do_segmentation(txt):
    doc = {'Text': txt}
    segs = post_request('document/segmentation?lan=es', doc)
    jso = json.dumps(segs, indent=2, sort_keys=True)
    print(jso)
    with open(F'_output/web-{DOCUMENT}-segs.json', 'w') as fp:
        fp.write(jso)
    return segs

'''
    MAIN
'''
def run():
    with open(F'_input/{DOCUMENT}.txt', 'r', encoding='UTF-8') as fp:
        text = fp.read()
    segs = do_segmentation(text)

if __name__ == '__main__':
    if DOCKER:
        run()
    else:
        import threading
        from app import main
        threading.Thread(target=run).start()
        main()
