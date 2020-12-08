from lyricsgenius import Genius

genius = Genius(token)
res = genius.search_song("Under the Bridge", "Red Hot Chili Peppers")

print(res.lyrics)
