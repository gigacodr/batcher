import os, glob, time, shutil; from datetime import datetime

# If you get indentation errors check near the underlined lines to make sure that the editor can properly read indentations.
# Some editors and this Python version do not like a mix of single spaces and tabs.

class Menu:

	## SET THE PURGE DEADLINE ## LEAVE EMPTY TO ASK FOR DATE AT RUNTIME ##
	user_set_date = "4-5-2022"
	## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

	startup_logo = "PyBatch - By Edgar A."

	def error():
		print('\n--[ Comment out the try and except keywords to debug properly. ]--\n')

	def prunepurge():

		try:
			if Menu.user_set_date == None:
				Menu.user_set_date = input('Enter cut-off date for folders older than specified date to be purged [Ex: 12-1-2020]: ')

			date_format = "%m-%d-%Y"
			ts = time.mktime(datetime.timetuple(datetime.strptime(Menu.user_set_date, date_format)))

			folders_deleted = 0
			files_deleted = 0

			parent_folder = os.getcwd()
			folder_items = os.listdir(parent_folder)
			# print(parent_folder)

			for item in folder_items:

				item_path = (parent_folder + '\\' + item)
				file_epoch_time = os.path.getmtime(item_path)

				if file_epoch_time <= ts:

					# if os.path.isfile(current_file_path): # uncomment this block to include file purging.

						# if file != "main.py" or file != "purge.bat":
							# os.remove(current_file_path)
							# files_deleted += 1

					if os.path.isdir(item_path):

						if item != "main.py" or item != "purge.bat":

							shutil.rmtree(item_path)

							# check if it was properly deleted
							if os.path.isdir(item_path) == False:
								folders_deleted += 1
							
							elif os.path.isdir(item_path) == True:
								print("Couldn't purge:", item_path)

			print('\n' + str(folders_deleted) + ' folders purged.')
			#print('\n' + str(files_deleted) + ' files purged.')
		except:
			Menu.error()

if __name__ == "__main__":

	print(Menu.startup_logo)

	if Menu.prunepurge() == False:
		exit()