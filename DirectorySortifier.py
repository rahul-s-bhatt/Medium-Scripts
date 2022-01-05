from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import re
import shutil

regexSearch = "Util.py$" 	# replace your regex here

class MyHandler(FileSystemEventHandler):

	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
			if(re.search(regexSearch, filename)):								
				src = folder_to_track + "\\" + filename
				new_destination = folder_destination + "\\" + filename
				shutil.move(src, new_destination)

folder_to_track = ""		# Source
folder_destination = "" 	# Destination

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
	while True:
		time.sleep(2)
except KeyboardInterrupt:
	observer.stop()

observer.join()