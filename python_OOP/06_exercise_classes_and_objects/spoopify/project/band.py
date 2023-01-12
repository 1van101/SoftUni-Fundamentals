from album import Album

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
        #if any(x.name == album.name for x in self.albums) <- which one is better?
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        try:
            album_to_be_removed = [x for x in self.albums if album_name == x.name][0]
            if album_to_be_removed.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album_to_be_removed)
            return f"Album {album_name} has been removed."
        except IndexError:
            return f"Album {album_name} is not found."

    def details(self):
        album_details = ""
        for album in self.albums:
            album_details += f"{album.details()}\n"
        return f"Band {self.name}\n{album_details}"


