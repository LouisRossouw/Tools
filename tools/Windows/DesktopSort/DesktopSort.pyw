import os
import shutil
import yaml
import scripts.sort as sort


# Relative paths to Desktop
Desktop = os.path.join(os.environ["HOMEPATH"], 'Desktop')
files = os.listdir(Desktop)

# Open config
config_path = os.path.abspath(__file__)
config = yaml.safe_load(open(f'{os.path.dirname(config_path)}\\config.yaml', 'r'))

# from config
main_dir_name = config['main_dir_name']
main_dir_path = config['main_dir_path']
unsorted_dir_name = config['unsorted_dir_name']
directories = config['directories']

main_path = f'{main_dir_path}\{main_dir_name}'

# Create main directory and sub directories based on config.yaml

# Main dir
if os.path.exists(main_path) != True:
    print('does not exists')
    os.mkdir(main_path)
else:
    print(f'{main_dir_name} directory exists')

# Sub dir
for key in directories:
    if os.path.exists(f'{main_path}\{key}') != True:
        print('does not exists')
        os.mkdir(f'{main_path}\{key}')
    else:
        print (f'{key} directory exists')

print ('---------------------------')

# Desktop sort - getting files from desktop loop
for f in files:

    file_split = os.path.splitext(f'{Desktop}\{f}')
    name_split = os.path.splitext(f)
    src_name = name_split[0]
    src_file_path = file_split[0]
    src_file_ext = file_split[1]


    # print (f'{src_file_name} - {src_file_ext}')

    # sort function
    sort.sort_files(src_name, src_file_path, 
                    src_file_ext, directories, main_path, unsorted_dir_name)

