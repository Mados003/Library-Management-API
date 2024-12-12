from app import create_app
from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = create_app()

SWAGGER_URL = '/api-docs'
API_URL = '/swagger/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger/<path:filename>')
def swagger_static(filename):
    return send_from_directory(os.path.join(os.getcwd(), 'src/swagger'), filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
