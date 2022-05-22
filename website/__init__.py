from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "192b9bdd2b9a393ec15f71bbf5dc987d54727823bcbf"
    app.config["MAX_CONTENT_LENGTH"] = (16 * 1024 * 1024)
    
    from .views import views
    from .predict import create_model
    app.register_blueprint(views, url_prefix='/')
    
    return app