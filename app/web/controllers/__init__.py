def init_app(app):
    from .user import user_controller
    app.register_blueprint(user_controller)
