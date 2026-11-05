from flask import render_template, request, redirect, url_for, flash

from app.models.movie import MovieModel

class MovieController:
    def __init__(self):
        self.model = MovieModel()

    def index(self):
        movies = self.model.get_all_movies()
        return render_template('movies/index.html', movies=movies)

    def store(self):
        title = request.form.get('title', '').strip()
        director = request.form.get('director', '').strip()
        year = request.form.get('year', type=int)

        if not title or not director or year is None:
            flash('Заповніть усі поля!', 'error')
            return redirect(url_for('index'))

        if self.model.add_movie(title, director, year):
            flash('Фільм додано!', 'success')
        else:
            flash('Не вдалося додати фільм', 'error')

        return redirect(url_for('index'))

    def mark_watched(self, movie_id: int):
        if self.model.mark_watched(movie_id):
            flash('Фільм позначено як переглянутий!', 'success')
        else:
            flash('Фільм не знайдено', 'error')
        return redirect(url_for('index'))

    def delete(self, movie_id: int):
        self.model.delete_movie(movie_id)
        flash('Фільм видалено!', 'success')
        return redirect(url_for('index'))