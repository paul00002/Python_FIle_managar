# Questo script contine le funzione per modifica di file,
import os
import pandas as pd
       
class File: 
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
    def open(self):
        os.system(os.path.join(self.rootpath,'"'+self.namefile+'"'))
        
class Director:
    def __init__(self,path) -> None:
        self.path=path
        self.namefile=os.path.basename(path)
        
      
    def Load(self):
        self.load=self.Type_path()
        self.files={x:[y,z,r] for x,y,z,r in self.load}
        return self
        
    def Pd_DataFrame(self):
        self.pb=pd.DataFrame(list(self.Type_path()),columns=["Name_file","Object","Type","Root"])
        return self.pb
    
    def Delete(self,name):
        if name in self.files:
          os.system('del {Pfile}'.format(Pfile=self.files[name].path))
          if os.path.exists(self.files[name].path):
              return False
          else:
              return True
          
    def Move(self,name,new_path):
        if  os.path.exists(new_path):
            os.system('move {Pfile} {Npath}'.format(Pfile=self.files[name].path,Npath=new_path))
            return True 
        else:
            return False
    
    def Copy(self,name,new_path):
        if  os.path.exists(new_path):
            os.system('copy {Pfile} {Npath}'.format(Pfile=self.files[name].path,Npath=new_path))
            return True 
        else:
            return False
    
    def Exists(self,name):
        if name in self.files:
            return True
        else: 
            return False

    def Type_path(self):
        for x in os.listdir(self.path):
            try: 
                x.split('.')[1]
                yield x,File(os.path.join(self.path,x)),"File",x.split('.')[1]
            except:
                yield x,Director(os.path.join(self.path,x)),"Director",None
     
    def find(self,name):
        if self.load:
          self.Load()
        mblis=[]
        for key in self.files.keys():
            if key.find(name)!=-1:
                mblis.append(key)
        return mblis
    
if __name__=='__main__':
   user=os.environ['USERPROFILE']
   desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop') 
   dire=Director(desktop).Load()
   pf=dire.Pd_DataFrame()
   files=pf.loc[pf['Root'].isin(["csv"])].iloc[:,0:2]
   print(dire.find('bot'))