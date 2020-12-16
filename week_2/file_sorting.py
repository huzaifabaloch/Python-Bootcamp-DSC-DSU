import os


def display_files(files):
    print('\n ==================================================')
    print(' The format is (FILE NAME, FILE TYPE, FILE SIZE)')
    print(' ==================================================')
    print('\n')
    for key, file in enumerate(files):
        print(' ', key+1, file)


def ask_user_directory():
    folder_path = input("\n Enter your directory path: ")
    if not os.path.isdir(folder_path):
        print(" No such directory exists on your system")
        return

    return folder_path
        

def your_directory(path):
    """
        This is responsible to show all the files in descending order in a particular directory given path.
        Here I've separated (file name , file type and file size) in a tuple and then sorted.
    """

    # Listing all files, excluding folders
    files = os.listdir(path)
    
    # Ignoring temporary files.
    files = [file for file in files if not file.startswith('~')]

    # To get the names for each file (checking if the selected file is not a folder)
    file_names = [ file[::-1][file[::-1].find('.')+1:][::-1] for file in files if os.path.isfile(path+'\\'+file)]

    # To get the extension from each file  (checking if the selected file is not a folder)
    file_extentions = [ file[::-1][:file[::-1].find('.')][::-1] for file in files if os.path.isfile(path+'\\'+file) ]

    # To get the size of each file   (checking if the selected file is not a folder)
    file_sizes = [ os.stat(path+"\\"+file).st_size for file in files if os.path.isfile(path+'\\'+file) ]

    # finally zipping files (name, type, size) in a list of tuples.
    files_info = [ (name, extenstion, size) for name, extenstion, size in zip(file_names, file_extentions, file_sizes) ]


    # Here I've used sorted function with a function inside that will sort according to third index that is size of
    # file and reverse=True will sort them in descending order.
    files_info = sorted(files_info, key=lambda x: x[2], reverse=True)

    return files_info, path


def show_menu():

    menu = {
    1: "Show my files from a specific directory",
    2: "Remove a file from a specific directory",
    3: "Exit"
    }

    # Displaying menu
    print("\n ==== My Directory ====\n")
    for key, value in menu.items():
        print(' ', str(key) + ': ' + value)

    user_input = int(input('\n Please select: '))


    # For displaying files in a particular directory
    if user_input == 1:
        path = ask_user_directory()
        if path:
            display_files(your_directory(path)[0])

    # For displaying files in a particular directory with option to select any file to be deleted.
    elif user_input == 2:
        path = ask_user_directory()
        if path:
            files, path = your_directory(path)
            display_files(files)

        file_to_remove = int(input("\n Select a file to remove, this cannot be undo...: "))

        selected_file = path+'\\'+files[file_to_remove-1][0]+'.'+files[file_to_remove-1][1]
        
        choice = int(input(f'\n Remove file "{files[file_to_remove-1][0]}" ?   [1 | 0] : '))

        if choice == 1:
            os.remove(selected_file)
            print(f' File "{files[file_to_remove-1][0]}" removed successfully! ')

    # App exit
    else:
        exit()


if __name__ == '__main__':
    
    while True:
        # START
        show_menu()

