from .base import BaseRecipe
class PythonRecipe(BaseRecipe):
    def __init__(self, options):
        super().__init__(options)



    def get_requirement(self):
        return ["python","git"]



    
    def get_structure(self):
        return {"folder": ["src","test"], "files" : ["main.py","requirements.txt"] }

    
    def get_commands(self, options):
        commands = ["python -m venv venv"]

        framework = options.get("framework", "fastapi")
        print("OPTIONS:", options)
        print("FRAMEWORK:", framework)
        if framework == "fastapi":
            commands.append("venv\\Scripts\\python.exe -m pip install fastapi uvicorn")
        elif framework == "flask":
            commands.append("venv\\Scripts\\python.exe -m pip install flask")

        return commands
    def get_requirements_command(self):
        return "venv\\Scripts\\python.exe -m pip freeze > requirements.txt"




    
    def get_gitignore_rules(self):
        return [
    "__pycache__/",
    "*.py[cod]",
    "*.pyo",
    ".Python",
    ".venv/",
    "venv/",
    "env/",
    ".env",
    ".env.*",
    "*.log",
    ".pytest_cache/",
    ".mypy_cache/",
    ".ruff_cache/",
    ".coverage",
    "htmlcov/",
    "dist/",
    "build/",
    "*.egg-info/",
    ".idea/",
    ".vscode/",
    '.newp/'
]