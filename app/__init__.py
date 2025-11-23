from flask import Flask
import os

def create_app():
    # Get the parent directory (project root)
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    app = Flask(__name__, 
                template_folder=os.path.join(basedir, 'templates'),
                static_folder=os.path.join(basedir, 'static'))
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app