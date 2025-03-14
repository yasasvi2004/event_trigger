from flask import Flask
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
import logging
from dotenv import load_dotenv
from .extensions import db, scheduler  # Import db and scheduler from extensions.py
import os
import sys

# Initialize migrate
migrate = Migrate()
load_dotenv()

def create_app():
    # Create the Flask app
    app = Flask(__name__, static_folder='static')

    # Load configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    scheduler.init_app(app)

    # Configure logging for the scheduler
    logging.basicConfig(
        level=logging.DEBUG,  # Set logging level to DEBUG
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]  # Log to stdout
    )

    # Start the scheduler
    try:
        scheduler.start()
        logging.info("Scheduler started successfully.")
    except Exception as e:
        logging.error(f"Failed to start scheduler: {e}")

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Configure Swagger UI
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Event Trigger Platform"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app