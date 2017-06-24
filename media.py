import webbrowser


class Movie():
    """This class will provide a way display movie details."""

# this function specifies data needed for each movie listing
    def __init__(
        self,
        movie_title,
        movie_genre,
        movie_storyline,
        poster_image,
        trailer_youtube
    ):
        self.title = movie_title
        self.genre = movie_genre
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# this functions plays movie trailer from youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

