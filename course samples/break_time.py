import time
import webbrowser

total_breaks = 3

print("Program has started at %s" % time.ctime())
while total_breaks > 0:
    time.sleep(2 * 60 * 60)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    total_breaks -= 1
