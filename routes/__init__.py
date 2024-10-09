from .task_routes import task_bp
from .model_routes import model_bp
from .alarm_routes import alarm_bp

def init_app(app):
    app.register_blueprint(task_bp)
    app.register_blueprint(model_bp)
    app.register_blueprint(alarm_bp)

