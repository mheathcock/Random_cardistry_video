
#code adapted from: https://www.youtube.com/watch?v=vuaApmJW6Yo

import os
import random
import webbrowser
try:
    from pytube import Playlist
except ModuleNotFoundError:
    os.system('pip install pytube')
    from pytube import Playlist

"""
Function to go through urls in a playlist and add them an array
"""
def get_playlist(playlist):
    urls = []
    video_url = Playlist(playlist)

    for url in video_url:
        urls.append(url)

    return urls

#input playlist here
playlist = 'https://www.youtube.com/playlist?list=PLi5DZ-mvHJd_HyFL81BROnfY7UxiQEqbF'
links = get_playlist(playlist) #uses the get_playlist function to save to links var

"""
saves urls to a text file
"""
with open('plurls.txt', 'w') as f:
    for url in links:
        f.write(url + '\n')

"""
read url function
"""
def readurl():
    with open('plurls.txt', 'r') as file:
        saved_urls = [line.strip() for line in file]
    return saved_urls

"""
uses random choice to pick a random url
"""
def random_video(saved_urls):
    if saved_urls:
        return random.choice(saved_urls)
    else:
        return None

cardistry_video = readurl()

chosen_url = random_video(cardistry_video)

"""
opens url in web browser
"""
if chosen_url:
    webbrowser.open(chosen_url)
else:
    print("No YouTube URLs found in the file.")