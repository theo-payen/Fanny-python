#!/usr/bin/python
from logging import LOGGING
import psutil,datetime,os

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

    def get_disque_size(self):
        Partition = "/"
        total = os.statvfs(Partition).f_frsize * os.statvfs(Partition).f_blocks
        used = os.statvfs(Partition).f_frsize * (os.statvfs(Partition).f_blocks - os.statvfs(Partition).f_bfree)
        free = os.statvfs(Partition).f_frsize * os.statvfs(Partition).f_bfree
        total = total / 1024 / 1024
        used = used / 1024 / 1024
        free = free / 1024 / 1024
        percent_used = (used / total) * 100
        self.logging.info("Get disque size "+"total" + "," + str(total) + "," + "used" + "," +str(used) + "," + "free" + "," + str(free) + "," + "percent_used" + "," + str(percent_used))
        return "total" + "," + str(total) + "," + "used" + "," +str(used) + "," + "free" + "," + str(free) + "," + "percent_used" + "," + str(percent_used)

    def get_date(self):
        date = datetime.datetime.now()
        date = date.strftime("%d-%m-%Y_%H:%M:%S")
        self.logging.info("Get date "+date)
        return date



if __name__ == '__main__':
    print ("veillez importer le script")
    TOOLS = TOOLS()
    print (TOOLS.get_process())
else:
    print ("Le script tools a été importer avec succès")
