class Song:
    def __init__(self, title, performer, album, year):
      self.title = title
      self.performer = performer
      self.album = album
      self.year = year

    def __str__(self):
        return f"""
"Title": {self.title} 
"Performer: {self.performer} 
"Album": {self.album}
"Year": {self.year}"""

# object creation
song1 = Song("One kiss", "Dua Lipa", "xxx", 2019)
song2 = Song("Out the way", "Yeat", "yyy", 2022)

## object usage
print(song1)
print(song2)