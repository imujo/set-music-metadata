import eyed3
import os

song_path = 'C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music\Ali pamtim još - Hanka Paldum - Narodne.mp3'

song = eyed3.load(song_path)

# song.tag.remove('C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music\Hanka Paldum - Ali pamtim još.mp3')
# song.tag.save()

name = [path.strip() for path in song_path.split('\\')][-1].split('.')[0].split('-')

# set title
song.tag.title = name[0].strip()
print(song.tag.title)

# set artist
song.tag.artist = name[1].strip()
print(song.tag.artist)

# set image
image = open('C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music\{}.jpg'.format(name[1].replace(' ', '')), 'rb').read()
song.tag.images.set(1, image, 'image/jpg')

# set genre
song.tag.genre = name[2].strip()
print(song.tag.genre)

# set name
# os.rename(song_path, os.path.join('C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music', '{}-{}'.format(name[0], name[1]+'.mp3')))

# save
song.tag.save()