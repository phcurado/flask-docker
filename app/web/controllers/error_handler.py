from flask import Blueprint, jsonify, make_response

error_handler = Blueprint('errors', __name__)


@error_handler.app_errorhandler(400)
def handle_400(error):
    return make_response(jsonify({'error': error}), 400)

@error_handler.app_errorhandler(404)
def handle_404(error):
    return jsonify({'error': 'Not found'}), 404

