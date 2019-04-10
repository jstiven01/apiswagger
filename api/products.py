from services.CouchProvider import CouchProvider

def create_product(data_provider: CouchProvider, productPayload) -> str:
    return data_provider.create_product(productPayload)

def read_product(data_provider: CouchProvider, prod_id) -> str:
    return data_provider.read_product(prod_id)