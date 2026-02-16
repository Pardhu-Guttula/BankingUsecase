# Epic Title: User Authentication and Security

from backend.authentication.controllers.auth_controller import auth_blueprint
from backend.authentication.controllers.mfa_controller import mfa_blueprint
from flask_jwt_extended import jwt_refresh_token_required, create_access_token, get_jwt_identity, get_raw_jwt
from flask import Blueprint, jsonify

session_blueprint = Blueprint('session', __name__)

@session_blueprint.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user_id)
    return jsonify(access_token=new_access_token), 200

def register_auth_routes(app, db_instance, mfa_service_instance):
    global db, mfa_service
    db = db_instance
    mfa_service = mfa_service_instance
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
    app.register_blueprint(mfa_blueprint, url_prefix='/api/auth/mfa')
    app.register_blueprint(session_blueprint, url_prefix='/api/session')