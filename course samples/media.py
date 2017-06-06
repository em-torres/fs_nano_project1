import webbrowser


class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, duration, poster_image, storyline, title, trailer_youtube):
        Video.__init__(self, title, duration)
        self.poster_image_url = poster_image
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Movie):
    def __init__(self, duration, episode, title, season, tv_station):
        Video.__init__(self, title, duration)
        self.episode = episode
        self.season = season
        self.tv_station = tv_station
        pass


class TmdbApiConnection:
    def __init__(self):
        self.browse = webbrowser.open('https://api.themoviedb.org/3/movie/latest?api_key=732919f76697dcf56e13cf7ee937118a&language=en-US')
        # self.latest = tmdb.Movies.latest()




    pass
