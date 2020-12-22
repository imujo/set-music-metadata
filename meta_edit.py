import eyed3
import os

# ask user for path to songs & images
songs_path = 'C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music\songs'
images_path = 'C:\\Users\ivomu\Documents\Dev\PROGRAMIRANJE\Python\Music\images'


for song in os.listdir(songs_path):
    song_no_extension = os.path.splitext(song)[0]
    name_components = [s.strip() for s in [splited.strip() for splited in song_no_extension.split('-')]]


    # load files
    song_file = eyed3.load(os.path.join(songs_path, song))
    image_file = open(os.path.join(images_path, name_components[1].replace(' ', '')+'.jpg'), 'rb').read()

    # set title
    song_file.tag.title = name_components[0]

    # set artist
    song_file.tag.artist = name_components[1]

    # set image
    song_file.tag.images.set(1, image_file, 'image/jpg')

    # set genre
    song_file.tag.genre = name_components[2]

    # save
    song_file.tag.save()

    # rename
    old_dir = os.path.join(songs_path, song)
    new_dir = os.path.join(songs_path, '{} - {}.mp3'.format(name_components[0], name_components[1]))
    os.rename(old_dir, new_dir)