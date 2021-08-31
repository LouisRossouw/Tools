import os
import shutil
from datetime import date
from Scripts.utils import compress_clip, categorize

# This tool copies all the files from DJI flash, into a new directory on the 
# Desktop and then converts all the videos into a lowres version with the 
# same naming, this helps to speed up editing with after affects

# Need ffmpeg installed in path env to work

today = date.today()


GoPro_Path = 'E:\\DCIM\\100MEDIA'
GoPro_files = os.listdir(GoPro_Path)

res_width = '1280'
res_height = '720'
output_format = '.mp4'

output_dir_name = 'DJI_compress'
output_main_path = f'C:\\Users\\Louis\\Desktop\\{output_dir_name}'
output_sub_path = f'\\DJI_{str(today)}'


# Check if main Dir exists
if os.path.exists(output_main_path) != True:
    print(f'{output_dir_name} does not exists')
    os.mkdir(output_main_path)
else:
    print(f'{output_dir_name} directory exists')
#####
if os.path.exists(output_main_path + output_sub_path) != True:
    print(f'sub does not exists')
    os.mkdir(output_main_path + output_sub_path)
else:
    print(f'Sub directory exists')


# copy and create
for f in GoPro_files:

    file_split = os.path.splitext(f'{GoPro_Path}\{f}')
    name_split = os.path.splitext(f)
    source_file_name = name_split[0]
    source_file_path = file_split[0]
    source_file_ext = file_split[1]

    source_file = source_file_path + source_file_ext

    destination_dir = categorize(source_file_ext)
    
    sub_path = output_main_path + output_sub_path

    # check if sub dirs movies / images exists
    if os.path.exists(sub_path + '\\' + destination_dir) != True:
        if destination_dir != 'unknown':
            os.mkdir(sub_path + '\\' + destination_dir)
            if destination_dir != 'images':
                os.mkdir(sub_path + '\\' + destination_dir + '\\hires')
                os.mkdir(sub_path + '\\' + destination_dir + '\\lowres')
        else:
            pass
    else:
        print(f'{destination_dir} directory exists')

    ##### ##### ##### ##### ##### ##### 

    if destination_dir == 'images':
        where_to = ''
    elif destination_dir == 'movies':
        where_to = '\\hires'
    else:
        pass

    if destination_dir != 'unknown':
        # Copy files to from drive to new directory
        shutil.copy(source_file, (sub_path + '\\' + destination_dir + where_to))
    else:
        pass

    if source_file_ext == '.MP4':
        # compress lowres clips
        output_path = (sub_path + '\\' + destination_dir + '\\lowres\\')

        output = output_path + source_file_name + output_format

        resolution = f'{res_width}:{res_height}'

        compress_clip(
                        source_file,
                        output,
                        resolution,
                    )
    else:
        pass
