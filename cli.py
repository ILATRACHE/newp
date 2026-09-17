
from config import ProjectConfiguration
from recipes.python import PythonRecipe
from safety import check_system_requirements , scan_directory
from colorama import Fore, Style, init
init()


def choose_recipe_name():
    recipe_name = "python"
    choice = input("please choose : \n" \
    "1.python\n" \
    "2.React\n" \
    "3.C++").upper()
    if choice.upper() in ["2"  , "REACT" , 'R'] :
        recipe_name ="React"
    elif choice.upper() in ['3' , "C" , "C++"] :
        recipe_name = 'C++'
    return recipe_name

def choose_recipe_option(recipe_name):
    if recipe_name == "python" :
        recipe_option = {"framework":"fastapi","Git":True}
        choice = input("please choose : \n" \
            "1.fastapi\n" \
            "2.flask\n" \
            "3.None\n"
            ).upper()
        if choice.upper() in ["2" , "FLASK" , 'F']  :
            git_choice = input("do yoo want initial git y/N : ").upper()
            if git_choice in ["N" , "NON"]  : 
                recipe_option = {"framework":"flask","Git":False}
            else : 
                recipe_option = {"framework":"flask","Git":True}
        elif choice.upper() in ["3" , "NONE" , 'N']  :
                    git_choice = input("do yoo want initial git y/N : ").upper()
                    if git_choice in ["N" , "NON"]  : 
                        recipe_option = {"framework":None,"Git":False}
                    else : 
                        recipe_option = {"framework":None,"Git":True}
        else : 
            git_choice = input("do yoo want initial git y/N : ").upper()
            if git_choice in ["N" , "NON"]  : 
                recipe_option = {"framework":"fastapi","Git":False}
            
            
    return recipe_option
                
            

    

def display_banner():
    
    print(Fore.CYAN + r"""
        ███╗   ██╗███████╗██╗    ██╗██████╗
        ████╗  ██║██╔════╝██║    ██║██╔══██╗
        ██╔██╗ ██║█████╗  ██║ █╗ ██║██████╔╝
        ██║╚██╗██║██╔══╝  ██║███╗██║██╔═══╝
        ██║ ╚████║███████╗╚███╔███╔╝██║
        ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚═╝
        """ + Style.RESET_ALL)

    print("\033[38;5;220m  Welcome to NEWP\033[0m")
    print(Fore.LIGHTBLACK_EX + "  Your project starts here." + Style.RESET_ALL)

def collect_user_input():
    project_name = input(Fore.YELLOW + "Project name: " + Style.RESET_ALL)
    location = input(Fore.CYAN + "Location: " + Style.RESET_ALL)
    if not location :
        location = project_name
    recipe_name = choose_recipe_name()
    recipe_option = choose_recipe_option(recipe_name)
    status = "draft"
    project_config = ProjectConfiguration(project_name , location , recipe_name , recipe_option , status)
    recipe = None
    if recipe_name == "python" :
        safety_report = []
        recipe= PythonRecipe(recipe_option)
        requirements = recipe.get_requirement()
        rq = check_system_requirements(requirements)
        if rq["safe"] == False : 
            print(rq["missing"])
            return
        structure = recipe.get_structure()
        sd = scan_directory(location , structure)
        if sd["safe"] == False : 
            safety_report.append(sd["conflicts"])
            
    else :
        print('wait for updates')
        return
    if display_review(project_config,safety_report) == True : 
        return project_config , recipe
    else : 
        return None
    
    
        
def display_review(config , safety_report):
    print(config.project_name)
    print(config.location)
    if safety_report != [] :
        print(safety_report) 
    print(config.recipe_name)
    print(config.recipe_option)
    print(config.status)
    choice = input("please choose : \n" \
        "1.continu\n" \
        "2.modifier\n" \
        "3.exit").lower()
    if choice in ["1" , 'c' , 'continu'] : 
        return True
    elif choice in ["2" , 'm' , 'modifier']:
        print("Edit not implemented yet — cancelling.")
        return False
    else:
        return False 

def show_progress(message , status):
    if status == "running":
        print (f'⟳ {message}')  
    elif status =="success" :
        print(f'✓ {message}') 
    elif status =="failed" :
        print (f'✗ {message}')
    return


