from lyricsgenius import Genius
# token goes here
genius = Genius(token)
res = genius.search_song("Red Hot Chili Peppers", "Under the Bridge")

print(res.lyrics)
