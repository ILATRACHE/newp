class BaseRecipe():
    def __init__(self,options):
        self.options = options
    def get_requirement(self):
        pass
    def get_structure(self):
        pass
    def get_commands(self,options):
        pass
    def get_dependencises(self,option):
        pass
    def get_gitignore_rules(self):
        pass