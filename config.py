class ProjectConfiguration :
    def __init__(self,project_name,location,recipe_name,recipe_option,status):
        self.project_name = project_name
        self.location = location
        self.recipe_name = recipe_name
        self.recipe_option = recipe_option
        self.status = status

    def to_dic(self):
        return self.__dict__
