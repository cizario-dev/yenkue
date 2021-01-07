from flask import Flask


def create_app():
    """Create a Flask application using the app factory pattern."""

    app = Flask(__name__)
    app.config['SERVER_NAME'] = 'yankue.local'

    """Register blueprints."""
    from .errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from .oauth import bp as oauth_bp
    app.register_blueprint(oauth_bp, subdomain='oauth')

    from .home import bp as home_bp
    app.register_blueprint(home_bp)
    
    return app
