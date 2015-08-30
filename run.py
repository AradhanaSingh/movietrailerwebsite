from moviedatabase import get_movies
import fresh_tomatoes

# get list of movies from movie databse
movie_list = get_movies()
# calls open_movies_page method given in freshtomatoes.py file
fresh_tomatoes.open_movies_page(movie_list)
