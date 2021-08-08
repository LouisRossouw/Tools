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

        while True:
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
                    else:
                        pass                    
            break


        print (ext + ' - ' + src_file_ext)
        unsorted_dir = f'{main_path}\\{unsorted_dir_name}'
        
        # make a directory for unsorted files
        if os.path.exists(unsorted_dir) != True:
            print(f'{unsorted_dir_name} does not exists')
            os.mkdir(unsorted_dir)
        else:
            print(f'{unsorted_dir_name} directory exists')

            try:
                shutil.move(f'{src_file_path}{src_file_ext}', unsorted_dir)
            except FileNotFoundError:
                print ('it exists')

            except shutil.Error:
                print ('yes')
                # Loop and try all the version numbers until it breaks the loop
                i = 0
                while True:
                    i += 1
                    try:                            
                        os.rename(f'{src_file_path}{src_file_ext}', f'{unsorted_dir}\\{src_name}_{i}{src_file_ext}')
                        break
                    except FileExistsError:
                        pass


                    
if __name__ == '__main__':
    pass