
def init_app(app):

    from .user import set_user_routes
    set_user_routes(app)
