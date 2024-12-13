from app import create_app
from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

# Create Flask app
app = create_app()

# Swagger UI configuration
SWAGGER_URL = '/api-docs'  # URL for accessing Swagger UI
API_URL = '/swagger/swagger.yaml'  # Path to your Swagger YAML file

# Set up Swagger UI blueprint
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Route to serve Swagger files
@app.route('/swagger/<path:filename>')
def swagger_static(filename):
    # Serve files from src/swagger
    return send_from_directory(os.path.join(os.getcwd(), 'src/swagger'), filename)

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
