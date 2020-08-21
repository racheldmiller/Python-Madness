
# needs to be a data structure
# use a list or a dictionary ... list seems intuitive since it's a list of songs... BUT we need to store information of the name of the playlist and the creator.
# SO USE A DICTIONARY. Songs will go into a list.

# In songs, we need TITLES, ARTISTS, ALBUM NAME, DURATION. All keys inside of a dictionary.
# Each song itself is a dictionary instead of a list, and the order they're in the list will dictate the order that they're in the playlist.

playlist = {'title':
            'patagonia bus',
            'creator': 'rachel',
            'songs': [
                {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
                {'title': 'song2', 'artist': [
                    'kitty', 'djcat'], 'duration': 5.25},
                {'title': 'song3', 'artist': ['ratt'], 'duration': 2.0},
            ]}

# Testing that songs list out.
# for song in playlist['songs']:
#     print(song['title'])

# Determine how long your playlist is

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)
