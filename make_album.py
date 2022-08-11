def make_album(artist,album,released):
		album_name = {
			'album_name': album,
			'artist': artist,
			'release_date': released,
			'track_list': {

			}
		}
		made_album = f"{album.title()}, released in {released}, is an album by {artist.title()}"
		return made_album


after_laughter_tracks = {
	'hard times': '3:02',
	'told you so': '3:09',
	'fake happy': '3:56',
	'pool': '3:53',
	'caught in the middle': '3:34',
	'no friend': '3:24',
	'rose-colored boy': '3:33',
	'forgiveness': '3:40',
	'26': '3:42',
	'grudges': '3:07',
	'idle worship': '3:18',
	'tell me how': '4:20',
}
paramore = make_album('paramore','after laughter',2017)
print(paramore)
for i, (k, v) in enumerate(after_laughter_tracks.items()):
	print(f"{i :<1}. {k :<25}{v}")
	

tool = make_album('tool','lateralus',2001)
print(tool)