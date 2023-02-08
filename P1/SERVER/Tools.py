#!/usr/bin/python
from logging import LOGGING
import psutil

class TOOLS():
	def __init__(self) :
		self.FILE_LOG = "Folder_log/tools.log"
		self.logging = LOGGING(self.FILE_LOG)
		pass

	def get_cpu(self):
		return psutil.cpu_percent()

	def get_memory(self):
		memoir = psutil.virtual_memory()
		return memoir.percent




if __name__ == '__main__':
	print ("veillez importer le script")
else:
	print ("Le script tools a été importer avec succès")