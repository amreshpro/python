import os


class File:
    def create_folder(self,name):
        os.makedirs(name, mode=0o777,exist_ok=True)
    
    def remove_folder(self, fname):
        os.removedirs(fname)    
        
    def rename_folder(self,oldName,newName):
        os.renames(oldName,newName)    
        
    def current_folder(self):
        print(os.getcwd())

file =  File()   

file.create_folder("fol1") 
file.create_folder("fol2")
file.create_folder("fol3")
file.remove_folder('fol2')
# file.rename_folder("fol1","Sachidanand")
file.current_folder()     
     
    
print(os.fspath("/Sachidanand"))
print(os.cpu_count())