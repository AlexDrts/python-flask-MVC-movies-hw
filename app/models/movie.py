from dataclasses import dataclass
from typing import List

@dataclass
class Movie:
    id: int
    title: str
    director: str
    year: int
    watched: bool = False

class MovieModel:
    def __init__(self):
        self._movies: List[Movie] = []
        self._next_id = 1

    def add_movie(self, title: str, director: str, year: int) -> bool:
        title = title.strip()
        director = director.strip()
        if not title or not director:
            return False
        self._movies.append(Movie(id=self._next_id, title=title, director=director, year=year))
        self._next_id += 1
        return True

    def get_all_movies(self) -> List[Movie]:
        return self._movies.copy()

    def mark_watched(self, movie_id: int) -> bool:
        for movie in self._movies:
            if movie.id == movie_id:
                movie.watched = True
                return True
        return False

    def delete_movie(self, movie_id: int) -> bool:
        self._movies = [m for m in self._movies if m.id != movie_id]
        return True