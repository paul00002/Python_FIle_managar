# Questo script contine le funzione per modifica di file,
import os
from  glob import glob
user=os.environ['USERPROFILE']
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
       
class File(): 
    def __init__(self,path_file ) -> None:
        if os.path.exists(path_file):
           self.namefile=os.path.basename(path_file)
           self.name=self.namefile.split('.')[0]
           self.root=self.namefile.split('.')[1]
           self.rootpath=path_file.replace(self.namefile,'')
           self.path_file=path_file
        else:
          raise ValueError('\n-Invalid file path \n-Enter a valid Argument \n-Argument: "path_file"')
        
    def copy(self,new_path):
        if  os.path.exists(new_path):
            os.system('copy {Pfile} {Npath}'.format(Pfile=self.path_file,Npath=new_path))
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
    def __init__(self,path_dir) -> None:
        self.path_dir=path_dir
        self.Files= {x:File(os.path.join(self.path_dir,x) ) for x in  os.listdir(self.path_dir)}
        
    def delete(self,name):
        if name in self.Files:
          os.system('del {Pfile}'.format(Pfile=self.Files[name].path_file))
          if os.path.exists(self.Files[name].path_file):
              return False
          else:
              return True
          
    def Move(self,name,new_path):
        if  os.path.exists(new_path):
            os.system('move {Pfile} {Npath}'.format(Pfile=self.Files[name].path_file,Npath=new_path))
            return True 
        else:
            return False
    
    def copy(self,name,new_path):
        if  os.path.exists(new_path):
            os.system('copy {Pfile} {Npath}'.format(Pfile=self.Files[name].path_file,Npath=new_path))
            return True 
        else:
            return False
    
    def exists(self,name):
        if name in self.Files:
            return True
        else: 
            return False

def type_path(path):
    for x in os.listdir(path):
        try: 
            x.split('.')[1]
            yield x,'file'
        except:
            yield x,'directory'
    

def Discovery():
    return {desktop:list(type_path(desktop))}
    
if __name__=='__main__':
   #dirc=Director(os.path.join(desktop,'nn'))
   #print(dirc.copy('pino.txt','C:\\Users\\PaulHernanAlarconPac\\Desktop\\Python_FIle_managar\\per_pino'))
   print(Discovery())