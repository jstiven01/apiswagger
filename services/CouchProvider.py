import requests
import couchdb
import os
import flask


ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'pass'
COUCHDB_URL = 'http://'+ADMIN_USERNAME+':'+ADMIN_PASSWORD+'@'+os.environ['SERVER_URL']

couch = couchdb.Server(COUCHDB_URL)

class CouchProvider(object):
    '''
    CRUD Functions on DB 
    '''

    def create_product(self,payload):
        db = couch['products']
        if payload['_id'] in db:
            return {"error":"Found product with existing ID"}, 409
        else:
            db.save(payload)
            return payload,201

    def read_product(self, prod_id) -> str:
        db = couch['products']
        if(prod_id in db):
            product = db[prod_id]
            return product, 200
        else:
            return {"error": "Product not found"}, 400
