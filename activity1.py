class worker:
    def __init__(self,name):
        self.name=name


    def __del__(self):
        print("Object is deleted")

woeker1=worker("Ahmed")
print("name of the employee is",woeker1.name)


del woeker1