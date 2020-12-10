from time import sleep

song_by = 'Trever Daniel'
song = 'Falling'

lyrics = """  My last made me feel like I would never try again
            But when I saw you, I felt something I never felt
            Come closer, give you all my love
            If you treat me right, baby, I'll give you everything
            My last made me feel like I would never try again
            But when I saw you, I felt something I never felt
            Come closer, give you all my love
            If you treat me right, baby, I'll give you everything """


lyrics_split = lyrics.split('\n')

# Stripping extra spaces on both sides
lyrics_updated = [line.strip() for line in lyrics_split]


print(f'\nSong: {song}')
print(f'Song By: {song_by}')
for line in lyrics_updated:    
    print('\n\n')
    print('\t\t', line)
    sleep(1)

