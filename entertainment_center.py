import fresh_tomatoes
import media

toy_story = media.Movie(
    "https://upload.wikimedia.org/wikipedia/commons/d/db/Patern_test.jpg",
    "Some Storyline",
    "Una Pelicula mas",
    "https://www.youtube.com/watch?v=hC8CH0Z3L54")

fresh_tomatoes.open_movies_page([toy_story])
