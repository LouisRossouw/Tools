import os


def compress_clip(source_file, output, resolution):

    get_resolution = os.system(f'ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {source_file}')

    os.system(f'ffmpeg -i {source_file} -vf scale={resolution} {output}')


def categorize(source_file_ext):

    if source_file_ext == '.JPG':
        dest_dir = 'images'
    elif source_file_ext == '.MP4':
        dest_dir = 'movies'
    else:
        dest_dir = 'unknown'

    return dest_dir


if __name__ == '__main__':
    pass