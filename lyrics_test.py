from lyricsgenius import Genius

genius = Genius(token)
res = genius.search_song("Red Hot Chili Peppers", "Under the Bridge")

print(res.lyrics)
