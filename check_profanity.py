import os


def read_text():
    actual_path = os.path.dirname(os.path.abspath(__file__))
    file = r"%s\resources\movie_quotes.txt" % actual_path
    quotes = open(file)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()
