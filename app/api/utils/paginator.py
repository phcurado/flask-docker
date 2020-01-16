import sys
class Paginator:
    DEFAULT_PAGE = 1
    DEFAULT_PER_PAGE = 10
    @staticmethod
    def paginate(record, page = DEFAULT_PAGE, per_page = DEFAULT_PER_PAGE):
        record_query = record.query.paginate(page, per_page, False)
        return {
            'data': record_query.items,
            'page': page,
            'per_page': per_page,
            'total_results': record_query.total
        }

