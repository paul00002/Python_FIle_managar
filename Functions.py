# Questo script contine le funzione per modifica di file,
import os

class Path:
    def __init__(self) -> None: 
        self.user=os.environ['USERPROFILE']
        self.desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        self.file=os.getcwd()
    
    def Join_path(self,Root,dir):
        return os.path.join(Root,dir)
    
    def Exists_path(self,path):
        return os.path.exists(path)

class File(Path): 
    def __init__(self,path_file) -> None:
        super().__init__()
        if self.Exists_path(path_file):
           self.name=os.path.basename(path_file)
        else:
 
    def Move(self,Path_file,new_path):
        if  self.Exists_path(Path_file) and self.Exists_path(new_path):
            os.system('move {Pfile} {Npath}'.format(Pfile=Path_file,Npath=new_path))
            return True 
        else:
            return False
    
    def Delete():
        pass

    def Create():
        pass

    def copy():
        pass

    def Rename():
        pass

    def info():
        pass

if __name__=='__main__':
   m=File()
   print(m.Move('C:\\Users\\PaulHernanAlarconPac\\Desktop\\Gestorefile_v1\\GF_1\\per_pino'))
   