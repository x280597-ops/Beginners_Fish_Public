import os
def load_file():
   modules = {}
   gamelist=[]
   updatelist=[]
   num=0
   for file in os.listdir():
     if file.endswith(".py") and file != "main.py" and file != "read_files.py":
        name = file[:-3]
        file_num=num
        modules[num] = __import__(name)
        if hasattr(modules[num], "main") and hasattr(modules[num], "update"):
            gamelist.append(modules[num].main)
            updatelist.append(modules[num].update)
            num+=1
        else:
                print(name, "にmainまたはupdateがありません")
   return gamelist,updatelist
   