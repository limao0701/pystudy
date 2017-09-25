import xml.etree.ElementTree as ET
from  datetime import date
import os
import time
from shutil import copyfile
import watch_xml_files
import change_xml_file
import sys

folder_name=sys.argv[1]
wach_folder=watch_xml_files.watch_xml_files(folder_name)
changed_files=wach_folder.monitor_files()
new_files=[]
for f in changed_files:
    if not wach_folder.is_file_in(f):
        new_files.append(f)
for f in new_files:
    parser=ET.parse(folder_name+f)
    testset=parser.find('test_set')
    new_folder=''
    print testset.tag
    if not len(testset):
        new_folder=f.split('.')[0]
        print testset
    
    else:new_folder=testset.attrib['name']
    folder=os.listdir(folder_name)
    if new_folder not in folder:
        os.mkdir(folder_name+new_folder)
        copyfile(folder_name+"mainConfigFile.xml",folder_name+new_folder+"/mainConfigFile.xml")
        copyfile(folder_name+"devicemap.xml",folder_name+new_folder+"/devicemap.xml")
        copyfile(folder_name+"testbed.xml",folder_name+new_folder+"/testbed.xml")
        copyfile(folder_name+"testSet.xml",folder_name+new_folder+"/testSet.xml")
        copyfile(folder_name+f,folder_name+new_folder+"/"+f)
        change_xml_file.change_mainconfig("./automatos/"+new_folder)
        change_xml_file.change_testSet(path="./automatos/"+new_folder,testset_file=f)
        today=date.today()
        now=time.asctime().split()[3].replace(':',"-")
        mydir=today.isoformat()+"_"+now
        os.mkdir(folder_name+new_folder+"/"+mydir)
        print mydir
        









