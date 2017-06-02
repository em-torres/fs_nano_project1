import os
from requests import get as http_get


def read_text():
    actual_path = os.path.dirname(os.path.abspath(__file__))
    file = r"%s\resources\movie_quotes.txt" % actual_path
    quotes = open(file)
    contents_of_file = quotes.read()
    quotes.close()
    return contents_of_file


def check_profanity(text_to_check):
    connection = http_get('http://lovewww.wdylike.appspot.com/?q={0}'.format(text_to_check))
    return connection.text

assert check_profanity(read_text()) == 'false', "This contains a Profanity X-("
