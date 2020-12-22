import eyed3
import os

song_path = 'C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music\Ali pamtim još - Hanka Paldum - Narodne.mp3'

song = eyed3.load(song_path)
# image = open('C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music\HankaPaldum.jpg', 'rb').read()
# song.tag.remove('C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music\Hanka Paldum - Ali pamtim još.mp3')
# song.tag.save()

name = [path.strip() for path in song_path.split('\\')][-1]

print(name)