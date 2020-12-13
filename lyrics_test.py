from lyricsgenius import Genius
# token goes here
# still need to get the token

genius = Genius(token)
res = genius.search_song("Red Hot Chili Peppers", "Under the Bridge")

print(res.lyrics)
