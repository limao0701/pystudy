import shutil
import os
import time
import threading
class watch_xml_files:
    def __init__(self,dir_path):
        #add try catch
        self.path=dir_path
        self.xmls=[]
        files=os.listdir(dir_path)
        for f in files:
            if f.split('.')[-1]=='xml':
                self.xmls.append(f)
    def add_file(self,file_name):
        if file_name in self.xmls:
            return
        else:
            files=os.listdir(dir_path)
            if file_name in files:
                slef.xmls.append(file_name)
                return
            
    def remove_file(self,file_name):
        if file_name in self.xmls:
            self.xmls.remove(file_name)

    def is_file_in(self,file_name):
        if file_name in self.xmls:
            return True
        else: return False

    def monitor_files(self):
        file_lists=[]
        while(True):
            all_files=os.listdir(self.path)
            for f in all_files:
                if f.split('.')[-1]=='xml' and f not in self.xmls:
                    file_lists.append(f)
            for f in self.xmls:
                if f not in all_files:
                    file_lists.append(f)
            if file_lists:break
            time.sleep(1)
            continue
        print "file changed in folder "+self.path +"\n"
        print file_lists
        return file_lists

def test(path):
    pass
    
if __name__=='__main__':
    local=wath_xml_files('./')
    #threading.Thread()
    local.monitor_files()
    


    
