import xml.etree.ElementTree as ET
import os
def change_mainconfig(path,file_name="mainConfigFile.xml",log="",device_mapping_file="devicemap.xml",test_set_file="testSet.xml",testbed_file="testBedInfo.xml"):
    if file_name not in os.listdir(path):
        print "not found file: "+file_name+" in "+path
        return False
    else:
        if os.name=='nt':
            path=path+'\\'
        else:path=path+'/'
        main_config=ET.parse(path+file_name)
        root=main_config.getroot()      
        for child in root:
            if child.tag=='local_base_log_path':
                print "Alter local base log path"
                child.text=path+log
            if child.tag=='device_mapping_file':
                print "Alter devicemapping path"
                child.text=path+device_mapping_file
            if child.tag=='test_set_file':
                print "Alter testset  path"
                child.text=path+test_set_file
            if child.tag=='testbed_file':
                print "Alter testbed path"
                #child.set('text',"C:\\Users\\lin21\\Documents\\recovery\\python\\"+mydir+"\\testBedInfo.xml")
                #set used for set arrtibute
                child.text=path+testbed_file
        main_config.write(path+file_name)
    return True

def change_testSet(path,testset_file,file_name="testSet.xml"):
    if file_name not in os.listdir(path):
        print "not found file: "+file_name+" in "+path
        return False
    else:
        if os.name=='nt':
            path=path+'\\'
        else:path=path+'/'
        testset=ET.parse(path+file_name)
        root=testset.getroot()
        test_set=root.find('test_set')
        test_groups=test_set.find('test_groups')
        test_group=test_groups.findall('test_group')
        for t_g in test_group:
            print t_g.tag
            print "This test_group would be deleted:"+t_g.tag
            test_groups.remove(t_g)              
        sub_elem="<test_group type="+'\"'+"parallel"+'\"'+"><test name="+'\"'+testset_file.split('.')[0]+'\"'+" type="+'\"cct\">'+"<location>"+path+testset_file+"</location>"+"</test>"+"</test_group>"
        print sub_elem
        test_groups.append(ET.fromstring(sub_elem))
        testset.write(path+file_name)
        return True






                          
