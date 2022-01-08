def tracklist(**tracks):
    for artist, albums in tracks.items():
        print(artist)
        for title, track in albums.items():
            print(f"ALBUM: {title} TRACK: {track}")
