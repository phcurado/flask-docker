from flask import jsonify, request


def set_user_routes(app):

    @app.route('/api/users', methods=['GET'])
    def get_users():
        return jsonify(hello='world!')

    @app.route('/api/users', methods=['POST'])
    def create_user():
        print(request)

    @app.route("/user/<name>")
    def get_user_name(name):
        return "Hello {}".format(name)