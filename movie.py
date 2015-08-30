# Movie class is template for movies to be stored for Movie Trailer website
class Movie:
    # constructor takes three arguments, title, poster_url and youtube_link
    def __init__(self, title, poster_url, youtube_link):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_link

'''
#to check if objects of class are being correctly initialzed
if __name__=="__main__""
    movie1=Movie("movie1","movie1","movie1")
    print movie1.title
    print movie1.poster_image_url
'''
