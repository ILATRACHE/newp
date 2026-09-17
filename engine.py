# from cli import collect_user_input
import subprocess
import os 
from cli import show_progress
from datetime import datetime
# def __init__(self,project_name,location,recipe_name,recipe_option,status):
#         self.project_name = project_name
#         self.location = location
#         self.recipe_name = recipe_name
#         self.recipe_option = recipe_option
#         self.status = status
def append_log(path , contenu):
    date = datetime.now()
    with open(path , "a" ,encoding="utf-8" ) as f:
            print(f"{date} : {contenu}",file=f )
def execute_setup(config , recipe):
    os.makedirs(config.location , exist_ok=True)
    date = datetime.now()
    newp = os.path.join(config.location,".newp") 
    os.makedirs(newp , exist_ok=True)
    set_up_log = os.path.join(newp ,'setup.log')
    with open(set_up_log , "w" ,encoding="utf-8" ) as f:
            print(f"Date : {date}",file=f )
            print(f"Project name : {config.project_name}",file=f )
            print(f"Rrecipe : {config.recipe_name}",file=f )
    append_log(set_up_log , f'folder {config.project_name} has been created ')
    r =recipe.get_structure() 

    if r["folder"] :
        for i in r['folder']:
            f =  os.path.join(config.location, i)
            os.makedirs(f,exist_ok=True)
            append_log(set_up_log , f'folder {i} has been created')
    if r['files'] :
        for i in r['files']:
                file_path=  os.path.join(config.location, i)
                with open(file_path, "w" , encoding="utf-8") as f:
                    f.write("")
                append_log(set_up_log , f'file {i} has been created')
    path = os.path.join(config.location, ".gitignore")
    with open(path , mode="w" , encoding="utf-8") as f :
        contenu = recipe.get_gitignore_rules()
        for i in contenu :
             f.write(i+"\n")
    append_log(set_up_log , f'.gitignore has been created')
    
    

    
    for c in recipe.get_commands(config.recipe_option) :
        resultat = subprocess.run(c ,cwd=config.location , shell=True)
        
        if resultat.returncode !=0 : 
            show_progress(f'command failed : {c}' , 'failed')
            append_log(set_up_log , f'{c} has been failed')
            if c == "python -m venv venv":
                return
        else :
            append_log(set_up_log , f'{c} has been instaled')
    if config.recipe_option["framework"] is not None:
        path = os.path.join(config.location,"requirements.txt")
        requirements_command= recipe.get_requirements_command()
        subprocess.run(requirements_command,cwd=config.location , shell=True)
        with open(path , "r" , encoding="utf-8") as f:
                    requirements = f.readlines()
                    for r in requirements : 
                        r = r.strip()
                        append_log(set_up_log , f'{r} has been add into requirements.txt')
    
    if config.recipe_option["Git"] :
        resultat = subprocess.run(["git", "init"],cwd=config.location , shell=True)
        append_log(set_up_log , f'git init')
        if resultat.returncode !=0 : 
            show_progress(f'command failed : git init ', 'failed')
            append_log(set_up_log , f'git failed to init')
            return
    
    show_progress(f'success', 'success')
    
    append_log(set_up_log , f'project has been set up sucessfally')
    return True

