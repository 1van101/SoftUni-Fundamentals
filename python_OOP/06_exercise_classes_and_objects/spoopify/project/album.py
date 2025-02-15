from song import Song

class Album:
    def __init__(self, name, *songs: Song):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        try:
            song_to_be_removed = [x for x in self.songs if x.name == song_name][0]
            self.songs.remove(song_to_be_removed)
            return f"Removed song {song_name} from album {self.name}."
        except IndexError:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs_info = ""
        for song in self.songs:
            songs_info += f"== {song.get_info()}\n"
        return f"Album {self.name}\n" \
               f"{songs_info}"


