DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 10
def get_page(headers):
    page = headers.get('page')
    if page is not None:
        return int(page)
    else:
        return DEFAULT_PAGE

def get_per_page(headers):
    per_page = headers.get('per_page')
    if per_page is not None:
        return int(per_page)
    else:
        return DEFAULT_PER_PAGE