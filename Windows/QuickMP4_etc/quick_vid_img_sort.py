import os
import shutil

# This tool you copy and paster into a messy directory and it will sort .jpgs
# and .mp4 into seperate directories.

quickmp4_path_directory = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(quickmp4_path_directory)

images = quickmp4_path_directory + '\\images'
videos = quickmp4_path_directory + '\\videos'

def move_file(source, destination):
    """ creates dir based ond moves files """

    if os.path.exists(images) != True:
        os.mkdir(images)
    else:
        print('images dir exists')
    if os.path.exists(videos) != True:
        os.mkdir(videos)
    else:
        print('video dir exists')    

    shutil.move(source, destination)


for f in files:

    file_split = os.path.splitext(f'{quickmp4_path_directory}\{f}')
    name_split = os.path.splitext(f)
    source_file_name = name_split[0]
    source_file_path = file_split[0]
    source_file_ext = file_split[1]

    source = source_file_path + source_file_ext

    video_format = ['.MP4', '.mp4', '.mov', '.3gp', '.flv']
    image_format = ['.JPG', '.jpg', '.png', '.gif', '.jpeg']

    for video_f in video_format:
        if source_file_ext == video_f:
            move_file(source, videos)
        else:
            pass
    for image_f in image_format:        
        if source_file_ext == image_f:
            move_file(source, images)
        else:
            pass