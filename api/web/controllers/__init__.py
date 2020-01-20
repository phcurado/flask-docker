def init_app(app):
    from .error_handler import error_handler
    from .user_controller import user_controller

    app.register_blueprint(error_handler)
    app.register_blueprint(user_controller)
