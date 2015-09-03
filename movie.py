# Movie class is template for movies to be stored for Movie Trailer website
class Movie:
    # constructor takes three arguments, title, poster_url and youtube_link
    def __init__(self, title, poster_url, youtube_link):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_link


