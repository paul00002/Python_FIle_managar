# Questo script contine le funzione per modifica di file,
import os
from  glob import glob
from typing import Any
import pandas as pd
user=os.environ['USERPROFILE']
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
       
class File(): 
    def __init__(self,path ) -> None:
        if os.path.exists(path):
           self.namefile=os.path.basename(path)
           self.name=self.namefile.split('.')[0]
           self.root=self.namefile.split('.')[1]
           self.rootpath=path.replace(self.namefile,'')
           self.path=path
        else:
          raise ValueError('\n-Invalid file path \n-Enter a valid Argument \n-Argument: "path"')
        
    def copy(self,new_path):
        if  os.path.exists(new_path):
            os.system('copy {Pfile} {Npath}'.format(Pfile=self.path,Npath=new_path))
            return True
        else:
            return False
        
    def rename(self,new_nam):
         if  not os.path.exists(os.path.join(self.rootpath,new_nam)):
            os.system('ren {fname} {Npath}'.format(fname=self.namefile,Npath=new_nam))
            return True
         else:
            return False
        
class Director():
    def __init__(self,path) -> None:
        self.path=path
        self.namefile=os.path.basename(path)
      
    def load(self):
        return pd.DataFrame(list(self.type_path()),columns=["Name_file","Object","Type"])
          
    def delete(self,name):
        if name in self.Files:
          os.system('del {Pfile}'.format(Pfile=self.Files[name].path))
          if os.path.exists(self.Files[name].path):
              return False
          else:
              return True
          
    def Move(self,name,new_path):
        if  os.path.exists(new_path):
            os.system('move {Pfile} {Npath}'.format(Pfile=self.Files[name].path,Npath=new_path))
            return True 
        else:
            return False
    
    def copy(self,name,new_path):
        if  os.path.exists(new_path):
            os.system('copy {Pfile} {Npath}'.format(Pfile=self.Files[name].path,Npath=new_path))
            return True 
        else:
            return False
    
    def exists(self,name):
        if name in self.Files:
            return True
        else: 
            return False

    def type_path(self):
        for x in os.listdir(self.path):
            try: 
                x.split('.')[1]
                yield x,File(os.path.join(self.path,x)),"File",
            except:
                yield x,Director(os.path.join(self.path,x)),"Director"
   
if __name__=='__main__':
   dire=Director(desktop).load()
   fi=dire['Object'][0]