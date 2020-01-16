def get_page(headers):
    return int(headers.get('page'))
def get_per_page(headers):
    return int(headers.get('per_page'))