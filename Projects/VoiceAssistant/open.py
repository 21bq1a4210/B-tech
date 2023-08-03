import os
def search_exe_files(search_path):
    '''
    The function is used to find the all apps in the search dir
    :param search_path: Directory path
    :return: list of apps
    '''
    exe_files = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower().endswith(".exe") or file.lower().endswith('.lnk'):
                exe_files.append(os.path.join(root, file))
    return exe_files

def open_exe_file_from_shortcut(shortcut_path):
    '''
    Open the given app
    :param shortcut_path: Exact path of the app
    :return:  statu message of the opening
    '''
    try:
        # Use the 'start' command on Windows to open the target of the shortcut
        os.system(f'start "" "{shortcut_path}"')
        return f"Opened {shortcut_path} successfully."
    except Exception as e:
        return f"Failed to open {shortcut_path}. Error: {e}"

def file(file_name):
    '''
    Finding the requested app need to be open whether exists in the giving directory or not
    :param file_name: application need to be opened
    :return: status that describes about app is opened or not
    '''
    # Replace 'C:\\search\\path' with the directory where you want to start the search
    search_directory = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
    found_exe_files = search_exe_files(search_directory)
    print(file_name)
    for path in found_exe_files:
        if file_name.capitalize() in path:
            open_exe_file_from_shortcut(path)
            return f"Opening {file_name}"
    else:
        return "Application not found"

if __name__ == "__main__":
    x = file('brave')
    print(x)