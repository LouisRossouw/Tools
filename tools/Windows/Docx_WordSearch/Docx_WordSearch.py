import os
import winshell
from docx import Document
from win32com.client import Dispatch

search_word = []
user_input = ''

quickmp4_path_directory = os.path.dirname(os.path.abspath(__file__))
docReturn_dir = quickmp4_path_directory + '\\DocReturn'
filez = os.listdir(quickmp4_path_directory)



def move_file(docReturn_dir):
    """ creates dir based ond moves files """

    if os.path.exists(docReturn_dir) != True:
        os.mkdir(docReturn_dir)
    else:
        pass


def shortcut(name, destination_dir, filename):
    """ creates a shortcut of the found dir """

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(destination_dir + '\\' + name + '.lnk') # must have .lnk for ext
    shortcut.Targetpath = filename
    shortcut.WorkingDirectory = destination_dir
    shortcut.save() 



# user input loop
while user_input != '/':
    user_input = input(f'\nType in search words, or type / to run {search_word} : ')
    if user_input != '/':
        search_word.append(user_input)


if bool(search_word) == False:
    print('\nno search words entered guy')
    input()
    exit()


print('\n----------------')
print('\n')

paths_list = []

# crawl all directories that the script lives in
for root, dirs, files in os.walk(quickmp4_path_directory, topdown=True):
    for name in files:
        paths_list.append(os.path.join(root, name))
    for name in dirs:
        paths_list.append(os.path.join(root, name))



report_notFound = []
report_found = []


# split file names to find the .extension
for f in paths_list:
    
    file_split = os.path.splitext(f)
    name_split = os.path.splitext(f)
    source_file_name = name_split[0]
    source_file_path = file_split[0]
    source_file_ext = file_split[1]
    file_name = os.path.basename(f)
    name = os.path.splitext(file_name)[0]

    source_path = source_file_path + source_file_ext
    
    # end_space = '                  '
    # print (f'\rReading files : {name[:20]} ... {source_file_ext}', end=end_space, flush=True)

    if source_file_ext == '.docx': 
        try:
            doc = Document(source_path)

            for para in doc.paragraphs:
                document_text = para.text

                # this if statement only runs if it has found ALL the words given
                if all(x in document_text for x in search_word):
                    
                    print (f'** found all the words in : {file_name}')
                    print(f'\nCreating shortcut files in {docReturn_dir}')
                    move_file(docReturn_dir)
                    
                    shortcut(name=name,
                            destination_dir=docReturn_dir,
                            filename=source_path
                            )

                # else find the singular word in current documents
                else:
                    for word in search_word:                    
                        if word in document_text:
                            report_found.append(word)
                            print (f'found the word " {word} " in : {file_name}')
                            
                        elif word not in document_text:
                            report_notFound.append(word)

        except:
            print(f'Error: cant read the {name}{source_file_ext} -  it needs to be 2007 - 2019 word docx document, dur ')               
    else:
        pass


list1 = set(report_found)
list2 = set(report_notFound)

missing = list(sorted(list2 - list1))

print('\n----------------')

if bool(report_found) != False:
    print (f'\nFound {set(report_found)}')
    print (f'\ncould not find {set(missing)}')
else:
    pass
    
print('\n----------------')

print('\nsearch complete')
input()





