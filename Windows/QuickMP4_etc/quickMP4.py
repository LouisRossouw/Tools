import os
from time import sleep

# This tool you copy and paste into a directory and it will convert all available 
# videos in the directory to the desired resolution.
# Need ffmpeg installed in path env to work https://ffmpeg.org

custom_res = input('Do you want a custom resolution? y/n :')

if custom_res == 'y':
    input_res = input('select resolution ie: 480p, 720p, 1080p, or custard : ')
    res_9x16 = input('16x9 or 9x16 ? :') 
else:
    input_res = False

if input_res == '480p':
    width = '680'
    height = '480'
elif input_res == '720p':
    width = '1280'
    height = '720'
elif input_res == '1080p':
    width = '1920'
    height = '1080'
elif input_res == 'custard':
    width = input('width ? : ')
    height = input('height ? : ')
elif input_res == False:
    width = '680'
    height = '480'
else:
    width = '680'
    height = '480'
   
quickmp4_path_directory = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(quickmp4_path_directory)

formats = '.mp4'

resolution = width + ':' + height
resolution9x16 = height + ':' + width

compress_dir = quickmp4_path_directory + '\\compressed'

def compress():

    if os.path.exists(compress_dir) != True:
        os.mkdir(compress_dir)
        if custom_res == 'y':
            if res_9x16 == '16x9':
                os.system(f'ffmpeg -i {source_file} -vf scale={resolution} {output}')
            elif res_9x16 == '9x16':
                os.system(f'ffmpeg -i {source_file} -vf scale={resolution9x16} {output}')
            else:
                print('no input for aspect ratio')
        else:
            os.system(f'ffmpeg -i {source_file} -vf scale={resolution} {output}')            

    else:
        if custom_res == 'y':
            if res_9x16 == '16x9':
                os.system(f'ffmpeg -i {source_file} -vf scale={resolution} {output}')
            elif res_9x16 == '9x16':
                os.system(f'ffmpeg -i {source_file} -vf scale={resolution9x16} {output}')      
            else:
                print('no input for aspect ratio')
        else:
            os.system(f'ffmpeg -i {source_file} -vf scale={resolution} {output}')
        

for f in files:

    file_split = os.path.splitext(f'{quickmp4_path_directory}\{f}')
    name_split = os.path.splitext(f)
    source_file_name = name_split[0]
    source_file_path = file_split[0]
    source_file_ext = file_split[1]

    source_file = '"' + source_file_path + source_file_ext + '"'
    output = '"' + compress_dir + '\\' + source_file_name + formats + '"'

    format_list = ['.MP4', '.mp4', '.avi', '.mkv', '.mov']

    for form in format_list:

        if source_file_ext == form:
            print ('i compress')
            compress()
        else:
            pass



