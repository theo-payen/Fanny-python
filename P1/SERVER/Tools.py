#!/usr/bin/python
from logging import LOGGING
import psutil

class TOOLS():
	def __init__(self) :
		self.FILE_LOG = "Folder_log/tools.log"
		self.logging = LOGGING(self.FILE_LOG)

	def get_cpu(self):
		CPU = str(psutil.cpu_percent())
		self.logging.info("Get CPU tools " + CPU )
		return CPU

	def get_memory(self):
		memoir = psutil.virtual_memory()
		memoir_percent = str(memoir.percent)
		self.logging.info("Get memory tools " + memoir_percent )		
		return memoir_percent

	def get_process(self):
		self.logging.info("Get all process tools ")
		tableau_process = []
		for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
			tableau_process.append(proc.info)
		return tableau_process



if __name__ == '__main__':
	print ("veillez importer le script")
	TOOLS = TOOLS()
	print (TOOLS.get_cpu())
	print (TOOLS.get_memory())
	print (TOOLS.get_process())
else:
	print ("Le script tools a été importer avec succès")