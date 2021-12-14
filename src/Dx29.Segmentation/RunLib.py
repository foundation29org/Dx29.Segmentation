import json

from Lib import DocSegmentation

DOCUMENT = 'Document1'

'''
    Read Document
'''
with open(F'_input/{DOCUMENT}.txt', 'r', encoding='UTF-8') as fp:
    txt = fp.read()

'''
    Split Document Segments
'''
seg = DocSegmentation('es')
doc = seg.process(txt)

js = json.dumps(doc, indent=2)
with open(F'_output/{DOCUMENT}.json', 'w') as fp:
    fp.write(js)

