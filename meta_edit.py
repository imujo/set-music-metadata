import eyed3
import os

def getDir():
    songs_path = input('Enter the full directory of the folder with the songs:  ')
    images_path = input('Enter the full directory of the folder with the images:  ')
    return songs_path, images_path

def artistToImageName(a_n):
    return a_n.replace(' ', '')+'.jpg'


def main():
    # get dirs
    songs_path, images_path = getDir()

    # for song in folder
    for song in os.listdir(songs_path):

        # remove extension
        song_no_extension = os.path.splitext(song)[0]
        # split name
        if len(song.split('-')) == 3:
            song_name, artist_name, genre = [s.strip() for s in [splited.strip() for splited in song_no_extension.split('-')]]


            # load files
            song_file = eyed3.load(os.path.join(songs_path, song))
            image_file = open(os.path.join(images_path, artistToImageName(artist_name)), 'rb').read()

            if song_file.tag is not None:
                # set title
                song_file.tag.title = song_name

                # set artist
                song_file.tag.artist = artist_name

                # set image
                song_file.tag.images.set(1, image_file, 'image/jpg')

                # set genre
                song_file.tag.genre = genre

                # save
                song_file.tag.save()

                # rename
                old_dir = os.path.join(songs_path, song)
                new_dir = os.path.join(songs_path, '{} - {}.mp3'.format(song_name, artist_name))
                os.rename(old_dir, new_dir)
            else:
                print('Format error. Please go to song properties, add a random tag and restart the program. File: "{}"'.format(song))
        else:
            print('Wrong naming scheame. File: "{}"'.format(song))




if __name__ == '__main__':
    main()