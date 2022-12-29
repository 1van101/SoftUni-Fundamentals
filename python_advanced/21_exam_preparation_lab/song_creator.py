def add_songs(*args):
    songs = {}
    result = ""

    for name, lyric in args:
        try:
            songs[name].extend(lyric)
        except KeyError:
            songs[name] = lyric

    for title, lyrics in songs.items():
        result += f"- {title}\n"
        if lyrics:
            result += "\n".join(lyrics) + "\n"

    return result



