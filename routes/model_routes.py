from flask import Blueprint, jsonify
from models import db, ModelInfo

model_bp = Blueprint('model_bp', __name__)

@model_bp.route('/api/models', methods=['GET'])
def get_models():
    models = ModelInfo.query.all()
    model_list = [{"id": model.id, "name": model.name, "version": model.version} for model in models]
    return jsonify(model_list)

