import json

from flask import request, make_response, jsonify
from flask_restplus import Resource

from .api import API

from Lib import DocSegmentation

segm_en = DocSegmentation('en')
segm_es = DocSegmentation('es')

def get_doc_segmentation(lan='en'):
    if lan.lower() == 'es': return segm_es
    return segm_en

'''
    Version
'''
@API.route('/about/version')
class version(Resource):
    def get(self):
        return 'v1.0.0'

'''
    Segmentation
'''
@API.route('/document/segmentation')
class post_segmentation(Resource):
    def post(self):
        doc = request.json
        if 'Text' in doc:
            text = doc['Text']
            lang = request.args.get('lan') or 'en'
            segm = get_doc_segmentation(lang)
            return segm.process(text)
        else:
            return 'Missing "Text" property.', 400
