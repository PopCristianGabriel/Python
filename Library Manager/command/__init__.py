class create_command():
    def __init__(self,name,arguments):
        self.name = name
        self.arguments = arguments
        
        
    def command_get_name(self):
        return self.name
    def command_get_arguments(self):
        return self.arguments
        