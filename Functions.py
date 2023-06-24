# Questo script contine le funzione per modifica di file,
import os

class Path:
    def __init__(self) -> None: 
        self.user=os.environ['USERPROFILE']
        self.desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        self.file=os.getcwd()

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
        
class Director(Path):
    def __init__(self,path_dir) -> None:
        super().__init__()
        self.path_dir=path_dir
        self.Files= [File(os.path.join(self.path_dir,x) ) for x in  os.listdir(self.path_dir)]
        
    def delete(self,name):
        os.system('del {Pfile}'.format(Pfile=self.path_file))
        if self.Exists_path(self.path_file):
            return True
        else:
            return False
    
    #def Move(self,new_path):
    #    if  self.Exists_path(new_path):
    #        os.system('move {Pfile} {Npath}'.format(Pfile=self.path_file,Npath=new_path))
    #        return True 
    #    else:
    #        return False

if __name__=='__main__':
   dirc=Director('C:\\Users\\Paul\\Desktop\\nnn')
   print(dirc.Files[0])