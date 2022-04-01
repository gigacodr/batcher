import os, glob, datetime, time, shutil

startup_logo = """Mega Batcher - By Edgar A."""

class MenuOne:

    def prunepurge(directories):

        try:
            date_format = "%m/%d/%Y"
            epoch = datetime.datetime(1970, 1, 1)

            deadline = input('Enter cut-off date for older folders/files to be deleted (Ex: M/D/YEAR): ')
            print(f'\nFolders/Files older than {deadline} will be purged. Are you sure you want to continue?')
            print('[ 1 ] Yes')
            print('[ 2 ] No')
            option = int(input())

            folders = 0
            reg_file = 0
            cutoff = ((datetime.datetime.strptime(deadline, date_format) - epoch).total_seconds())

            if option == 1:
                for directory in directories:

                    files = os.listdir(directory)
                    file_epoch_time = os.path.getmtime(directory)

                    for file in files:

                        current_file_path = (directory + "\\" + str(file))
                        if file_epoch_time <= cutoff:

                            if os.path.isfile(current_file_path):

                                os.remove(current_file_path)
                                reg_file += 1

                            elif os.path.isdir(current_file_path):

                                shutil.rmtree(current_file_path)
                                folders += 1
                            else:
                                print('File not found:', current_file_path)
                        else:
                            pass

                print(f'\n{folders} folders purged.')
                print(f'{reg_file} files purged.')

            if option == 2:
                print('\nOperation Canceled.')
                pass
        except:
            Home.error()

    def nukedir(directories, warning=True):

        try:
            print('\nAre you sure you want to delete the specificed path items?:')
            print('[ 1 ] Yes')
            print('[ 2 ] No')
            answer = int(input())

            for directory in directories:
                if warning == True:

                    if answer == 1:
                        pass

                    elif answer == 2:
                        print('\nOperation Canceled.')
                        return False
                    else:
                        print('\nInvalid input given.')
                        return False

                shutil.rmtree(directory)
                print('\nThanos snapped:', directory)
        except:
            Home.error()

    def typedelete(directories):

        try:
            i = 0
            file_ext = input('\nEnter the file extension (Ex: txt):')

            for directory in directories:

                full_path = str(directory + '\*.' + file_ext)
                files = glob.glob(full_path)
                
                for file in files:
                    os.remove(file)
                    i += 1

            print(f'\n{i} files with .{file_ext} removed.\n')
        except:
            Home.error()

    def getPath(paths):
        
        try:
            i = 0
            while True:
                print('\nEnter directory path(s) you would like to work inside:\n(One path per line, Enter 0 on new line after done entering): ')
                current_path = input('\n')

                if current_path != '0':
                    paths.append(current_path)
                    i += 1

                elif current_path == '0':

                    if i == 0:
                        Home.error()

                    elif i >= 1:
                        return paths

                elif current_path == None:
                    Home.error()
        except:
            Home.error()

    def menu1():

        current_paths = None
        paths = []

        while True:
            try:
                print('\n------------------')
                print('[ Purge Files ]')
                
                print('________________')
                print('Current Path(s): ')
                if current_paths != None:
                    for each_path in current_paths:
                        print(each_path)
                else:
                    print(current_paths)
                print('________________')

                print('\n[ 1 ] Delete files older than date specified (All folders/files that meet age condition)')
                print('[ 2 ] Delete specific file types (All files with specified extension)')
                print('[ 3 ] Add/Change working directory')
                print('[ 9 ] Nuke directory (Deletes all contents of path folder & the folder)')
                print('[ 0 ] Back')
                print('------------------')

                option = int(input())

                if option == 1:
                    MenuOne.prunepurge(current_paths)
                elif option == 2:
                    MenuOne.typedelete(current_paths)
                elif option == 3:
                    current_paths = MenuOne.getPath(paths)
                elif option == 9:
                    MenuOne.nukedir(current_paths, warning=True)
                elif option == 0:
                    break
                else:
                    Home.error()
            except:
                Home.error()

class MenuTwo:

	def prunepurge():

		try:
			date_format = "%m/%d/%Y"
			epoch = datetime.datetime(1970, 1, 1)
			deadline = input('Enter cut-off date for older folders/files to be deleted (Ex: M/D/YEAR): ')

			folders = 0
			reg_file = 0
			cutoff = ((datetime.datetime.strptime(deadline, date_format) - epoch).total_seconds())

			directory = os.getcwd()

			files = os.listdir(directory)
			file_epoch_time = os.path.getmtime(directory)

			for file in files:

				current_file_path = (directory + "\\" + str(file))
				if file_epoch_time <= cutoff:

					#if os.path.isfile(current_file_path):

						#os.remove(current_file_path)
						#reg_file += 1

					if os.path.isdir(current_file_path):
					
						if file != "main.py" or file != "start.bat":

							shutil.rmtree(current_file_path)
							folders += 1
						else:
							pass
					else:
						print('File not found:', current_file_path)
				else:
					pass

			print(f'\n{folders} folders purged.')
			print(f'{reg_file} files purged.')

		except:
			Home.error()

	def menu1():

        current_paths = None
        paths = []

        while True:
            try:
                print('\n------------------')
                print('[ Deleting all files within this directory... ]')

                MenuTwo.prunepurge()

				print('\n------------------')
            except:
                Home.error()

class Home:

    def error():
        print('\n--[ Path error: Path could not exist or files being deleted without proper permissions. ]--\n')

    def main_menu():

        print('\n------------------')
        print('[ Main Menu - Make sure the filename is "main.py" ]')
        print('------------------')
        print('[ 1 ] Purge files')
        print('[ 2 ] Neato Mode (Deletes all folders inside the current directory)')
        print('[ 3 ] Exit')
        print('------------------\n')

        option = int(input())

        if option == 1:
            MenuOne.menu1()
        elif option == 2:
            MenuTwo.menu1()
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