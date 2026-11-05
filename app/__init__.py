from flask import Flask
from app.controllers.movie_controller import MovieController

def create_app():
    app = Flask(__name__, template_folder='views/templates')
    app.secret_key = 'super-secret-key-for-flash'

    controller = MovieController()

    @app.route('/', methods=['GET'])
    def index():
        return controller.index()

    @app.route('/movies', methods=['POST'])
    def store():
        return controller.store()

    @app.route('/movies/<int:movie_id>/watched', methods=['POST'])
    def mark_watched(movie_id):
        return controller.mark_watched(movie_id)

    @app.route('/movies/<int:movie_id>/delete', methods=['POST'])
    def delete(movie_id):
        return controller.delete(movie_id)

    return app