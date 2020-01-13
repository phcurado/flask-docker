

def init_app(app):
    from .user import set_user_controller
    set_user_controller(app)
    # app.register_blueprint(user_controller)
