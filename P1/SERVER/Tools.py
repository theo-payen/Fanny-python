#!/usr/bin/python
from logging import Logging

class TOOLS():
	def __init__(self) :
		self.FILE_LOG = "Folder_log/tools.log"
		self.logging = Logging(self.FILE_LOG)
		pass


if __name__ == '__main__':
	print ("veillez importer le script")
else:
	print ("Le script tools a été importer avec succès")