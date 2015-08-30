# importing Movie class
from movie import Movie


def get_movies():
    # creating a list to store movie objects
    movie_list = list()
    # will be adding 6 movies in movie_list
    movie_object = Movie(
        "Toy Story",
        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    movie_list.append(movie_object)

    movie_object = Movie(
        "Avatar",
        (
            "http://imgs.abduzeedo.com/files/articles/Avatar/41546"
            "91039_e35717a862_o.jpg"),
        "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
    movie_list.append(movie_object)

    movie_object = Movie(
        "Descpicable Me",
        (
            "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable"
            "_Me_Poster.jpg"),
        "https://www.youtube.com/watch?v=nVwae09eSpo")
    movie_list.append(movie_object)

    movie_object = Movie(
        "Descpicable Me 2",
        (
            "http://hillviewchristian.com/wp-content/uploads/2014/06/despicabl"
            "e-me-2-wallpaper.jpg"),
        "https://www.youtube.com/watch?v=yM9sKpQOuEw")
    movie_list.append(movie_object)

    movie_object = Movie(
        "The Smurfs",
        (
            "https://upload.wikimedia.org/wikipedia/en/1/11/TheSmurfs"
            "2011Poster.jpg"),
        "https://www.youtube.com/watch?v=yhBpgqXwrt8")
    movie_list.append(movie_object)

    movie_object = Movie(
        "The Smurfs 2",
        "http://i.ytimg.com/vi/ww1ABFcueUk/maxresdefault.jpg",
        "https://www.youtube.com/watch?v=Kh1PTKTgCDk")
    movie_list.append(movie_object)
    return movie_list

# to check if movie list is getting populated correctly
# print get_movies()
