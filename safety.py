import shutil 
import os
def check_system_requirements(list):
    missing = []
    for t in list :
        if not shutil.which(t) :
            missing.append(t)
    if not missing :
        return {"safe" : True , "missing" : missing} 
    else : 
        return {"safe" : False , "missing" : missing}

def scan_directory(location,structure):
    if not os.path.exists(location):
        return {"safe" : True , "conflicts" : []}
    else :
        existing_file = os.listdir(location)
        if existing_file:
            return {"safe" : False , "conflicts" : existing_file}
        else : 
            return {"safe" : True , "conflicts" : []}
