import os
import shutil
import yaml


def sort_files(src_name, src_file_path, 
                src_file_ext, directories, main_path, unsorted_dir_name
                ):
    """" compares extensions and sorts it into its relevant directory """
     
    # if file is a directory:
    if os.path.isdir(src_file_path):
        print (f"yes it is {src_file_path}")
    # if not a directory:    
    else:
        for key in directories:

            length = len(directories[key])

            for i in range(length):
                ext = (directories[key][i-1])

                

                if src_file_ext == ext:
                    print (ext + ' - ' + src_file_ext)
                    try:
                        shutil.move(f'{src_file_path}{src_file_ext}', f'{main_path}\\{key}')
                    except shutil.Error:
                        # Loop and try all the version numbers until it breaks the loop
                        i = 0
                        while True:
                            i += 1
                            try:                            
                                os.rename(f'{src_file_path}{src_file_ext}', f'{main_path}\\{key}\\{src_name}_{i}{src_file_ext}')
                                break
                            except FileExistsError:
                                pass

                elif src_file_ext != ext:
                    print (ext + ' - ' + src_file_ext)
                    unsorted_dir = f'{main_path}\\{unsorted_dir_name}'
                    
                    # # make a directory for unsorted files
                    #try:                        
                        
                    if os.path.exists(unsorted_dir) != True:
                        print(f'{unsorted_dir_name} does not exists')
                        os.mkdir(unsorted_dir)
                    else:
                        print(f'{unsorted_dir_name} directory exists')

                        try:
                            shutil.move(f'{src_file_path}{src_file_ext}', unsorted_dir)
                        except shutil.Error:
                            print ('it exists')

                    # except shutil.Error:
                    #     print ('yes')
                    #     # Loop and try all the version numbers until it breaks the loop
                    #     i = 0
                    #     while True:
                    #         i += 1
                    #         try:                            
                    #             os.rename(f'{src_file_path}{src_file_ext}', f'{unsorted_dir}\\{src_name}_{i}{src_file_ext}')
                    #             break
                    #         except FileExistsError:
                    #             pass

                else:
                    pass
                    








if __name__ == '__main__':
    src_file_name = 'test_name'
    src_file_path = 'dir\test_path'
    src_file_ext = '.mp4'

    main_path = 'C:\\Users\\Louis\\Desktop\\Louis Folder\\GitHub_Projects\\Tools\\tools\\Windows\\DesktopSort\\test_desktop\\DesktopSort'

    directories = {
              'Movies': [
                      '.mp4',
                      '.mov',
                      '.aac'
                      ],
                      
              'Dump': [
                    '.max',
                    '.lnk',
                    ],

              'Document': [
                    '.pdf',
                    '.txt',
                    ],
              }
        
    sort_files(src_file_name, src_file_path, src_file_ext, directories, main_path)