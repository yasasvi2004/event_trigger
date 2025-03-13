from flask import Flask
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
import logging
from .extensions import db, scheduler  # Import db and scheduler from extensions.py

# Initialize migrate
migrate = Migrate()

def create_app():
    # Create the Flask app
    app = Flask(__name__, static_folder='static')

    # Load configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://event_trigger_db_user:QZDwB0qVV33h0QPvHR11KbED7zIWfiBT@dpg-cv96ip52ng1s73d0mfcg-a.oregon-postgres.render.com/event_trigger_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    scheduler.init_app(app)

    # Configure logging for the scheduler
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)

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