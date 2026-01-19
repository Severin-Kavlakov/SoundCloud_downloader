import yt_dlp
import os
from datetime import datetime

date = str(datetime.now())[:10] # get current date in format YYYY-MM-DD ; first 10 characters

# create folder "YYYY-MM-DD_MUSIC" in parent dir and separate folders for each playlist
savePath: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{date}_MUSIC/%(playlist_title)s")

# Final format template to import into yt-dlp
# X_title.original-extension, X is Number of track in playlist
outputTemplate: str = os.path.join(savePath, "%(playlist_index)s_%(title)s.%(ext)s")

# Read urls.txt file , URLS are ON SEPARATE LINES
with open( "urls.txt", "r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) as urlsTxt:
    urlsList: list[str] = urlsTxt.read().splitlines()

def main():
    ydl_options: dict = {
        'outtmpl': {'default': outputTemplate},    #Import file formatting code in yt-dlp

        'format': 'bestaudio/best',                # best audio-only
        'continuedl': True,                        # continue download if connection breaks
        'ignoreerrors': False,                     # ignores errors
        'nopart': True,                            # download whole files
        '--no-overwrites': True,                   # don't overwrite existing files
    }
    #To do:
    # in every playlist folder: create a txt wit hall the downloaded tracks

    #for EACH PLAYLIST:
    # compare the availible tracks in the playlist url ; download only tracks which aren't in the txt


    with yt_dlp.YoutubeDL(ydl_options) as ydl: # apply Yt Dlp options and download
        ydl.download(urlsList)



if __name__ == '__main__': # if script is directly run: execute script
    main()
