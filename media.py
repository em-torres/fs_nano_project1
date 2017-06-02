import webbrowser


class Movie:
    def __init__(self, poster_image, storyline, title, trailer_youtube):
        self.poster_image_url = poster_image
        self.storyline = storyline
        self.title = title
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)