import os, glob, datetime, time, shutil

startup_logo = """
███╗   ███╗███████╗ ██████╗  █████╗     ██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗ 
████╗ ████║██╔════╝██╔════╝ ██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
██╔████╔██║█████╗  ██║  ███╗███████║    ██████╔╝███████║   ██║   ██║     ███████║█████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║    ██╔══██╗██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║    ██████╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║
╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                      By Edgar A."""

class MenuOne:

    def prunepurge(filepath):

        try:
            file_epoch_time = os.path.getmtime(filepath)
            date_format = "%m/%d/%Y"
            epoch = datetime.datetime(1970, 1, 1)

            deadline = input('Enter cut-off date for older folders/files to be deleted (Ex: M/D/YEAR): ')
            print(f'\nFolders/Files older than {deadline} will be purged. Are you sure you want to continue?')
            print('[ 1 ] Yes')
            print('[ 2 ] No')

            option = int(input())
            if option == 1:

                cutoff = ((datetime.datetime.strptime(deadline, date_format) - epoch).total_seconds())
                i = 0
                files = os.listdir(filepath)

                for each in files:
                    if file_epoch_time <= cutoff:

                        current_file_path = (filepath + "\\" + str(each))

                        if os.path.isdir(current_file_path) == True:
                            shutil.rmtree(current_file_path)
                            i += 1

                        elif os.path.isfile(current_file_path) == True:
                            os.remove(current_file_path)
                            i += 1
                        else:
                            pass
                    else:
                        pass

                print(f'\n{i} folders/files purged.\n')

            if option == 2:
                print('\nOperation Canceled.')
                pass
        except:
            Home.error()

    def nukedir(dirpath, warning=True):

        try:
            if warning == True or warning == False:
                print('\nAre you sure you want to delete the specificed path items?:', dirpath)
                print('[ 1 ] Yes')
                print('[ 2 ] No')
                answer = int(input())

                if answer == 1:

                    print(dirpath)
                    shutil.rmtree(dirpath)

                    print('\nThanos snapped:', dirpath)

                elif answer == 2:
                    print('\nOperation Canceled.')
                    return False
                else:
                    print('\nInvalid input given.')
        except:
            Home.error()

    def typedelete(filepath):

        try:
            file_ext = input('\nEnter the file extension (Ex: txt):')

            i = 0
            full_path = str(filepath + '\*.' + file_ext)
            files = glob.glob(full_path)
            for each in files:
                os.remove(each)
                i += 1

            print(f'\n{i} files with .{file_ext} removed.\n')
        except:
            Home.error()

    def menu1():

        current_path = None
        while True:
            try:
                print('\n------------------')
                print('[ Purge Files ]')
                
                print('Current Path:', current_path)

                print('\n[ 1 ] Delete files older than date specified (All folders/files that meet age condition)')
                print('[ 2 ] Delete specific file types (All files with specified extension)')
                print('[ 3 ] Add/Change working directory')
                print('[ 9 ] Nuke directory (Deletes all contents of path folder & the folder)')
                print('[ 0 ] Back')
                print('------------------')

                option = int(input())

                if option == 1:
                    MenuOne.prunepurge(current_path)
                elif option == 2:
                    MenuOne.typedelete(current_path)
                elif option == 3:
                    current_path = input('\nEnter the directory path you want to work inside: ')
                elif option == 9:
                    MenuOne.nukedir(current_path, warning=True)
                elif option == 0:
                    break
                else:
                    Home.error()
            except:
                Home.error()

class MenuTwo:
    pass

class Home:

    def error():
        print('\n--[ Path error: Path could not exist or files being deleted without proper permissions. ]--\n')

    def main_menu():

        print('\n------------------')
        print('[ Main Menu ]')
        print('------------------')
        print('[ 1 ] Purge files')
        print('[ 2 ] Coming Soon')
        print('[ 3 ] Exit')
        print('------------------\n')

        option = int(input())

        if option == 1:
            MenuOne.menu1()
        elif option == 2:
            pass
        elif option == 3:
            return False
        else:
            Home.error()

if __name__ == "__main__":

    print(startup_logo)
    print('Welcome to Mega Batcher. Select a command to start. All commands are case-sensitive.')

    while True:
        if Home.main_menu() == False:
            exit()