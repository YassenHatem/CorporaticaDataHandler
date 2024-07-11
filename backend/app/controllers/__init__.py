from .tabular_controller import tabular_controller
from .images_controller import images_controller
from .text_controller import text_controller

def init_routes(app):
    app.register_blueprint(tabular_controller, url_prefix='/tabular')
    app.register_blueprint(images_controller, url_prefix='/images')
    app.register_blueprint(text_controller, url_prefix='/text')
