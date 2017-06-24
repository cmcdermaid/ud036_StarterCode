"""Details of movies are stored here and used to displayed on web page"""
import fresh_tomatoes
import media

harry_potter = media.Movie("Harry Potter",
                           "The story of the boy who lived.",
                           "Fantasy",
                           "http://bit.ly/2tGL1iz",
                           "https://youtu.be/lAxgztbYDbs")

star_wars = media.Movie("Star Wars: Episode V - The Empire Strikes Back.",
                        "Empire vs The Resistance",
                        "Sci-Fi",
                        "http://bit.ly/2tGDT5L",
                        "https://youtu.be/JNwNXF9Y6kY")

say_anything = media.Movie("Say Anything...",
                           "I gave her my heart, and she gave me a pen.",
                           "Rom-Com",
                           "http://bit.ly/2tGPou4",
                           "https://youtu.be/DeuZ7YPag1I")

up = media.Movie("Up",
                 "An old man, some ballons and his house.",
                 "Animated",
                 "http://bit.ly/2s7RscC",
                 "https://youtu.be/qas5lWp7_R0")

kiss_the_girls = media.Movie("Kiss the Girls",
                             "Creepy guy steals girls.",
                             "Thriller",
                             "http://bit.ly/2tGxHL1",
                             "https://youtu.be/JiHGk64-eNE")

mad_max = media.Movie("Mad Max: Fury Road",
                      "The ultimate feminist - for the win.",
                      "Action",
                      "http://bit.ly/1KRncpR",
                      "https://youtu.be/b_4nzm9ICuo")

# list of movies to display on web page
movies = [harry_potter, say_anything, up, star_wars, kiss_the_girls, mad_max]

# opens html web page
fresh_tomatoes.open_movies_page(movies)

