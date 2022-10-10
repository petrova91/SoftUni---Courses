def add_songs(*args):
    result = ""
    songs_collection = {}
    for title, lyrics in args:
        if title not in songs_collection:
            songs_collection[title] = lyrics
        else:
            if lyrics:
                songs_collection[title].extend(lyrics)
    for song_title, song_lyrics in songs_collection.items():
        result += f"- {song_title}" + "\n"
        for line in song_lyrics:
            result += line + "\n"
    return result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))





