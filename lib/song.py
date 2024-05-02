class Song:
    
    count = 0
    genres = set()
    artists = set()
    artist_count ={}
    genre_count = {}
    # add_to_artist = []
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.genre = genre
        self.artist = artist
        Song.count += 1
        # Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
       
    @classmethod 
    def add_to_genres(cls, genre):
        # if self.genre not in Song.genres:
            Song.genres.add(genre)
    
    @classmethod        
    def add_to_artists(cls, artist):
        Song.artists.add(artist)
     
    @classmethod       
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre)== None:
            cls.genre_count.update({genre: 1})
        else:
            cls.genre_count[genre]+=1
     
    @classmethod               
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist)== None:
            cls.artist_count.update({artist: 1})
        else:
            cls.artist_count[artist]+=1     
            
            
thriller = Song("Thriller", "Michael Jackson", "Pop")       
# print (thriller.artist)
breakpoint()