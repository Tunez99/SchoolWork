import os
"""
Quick script to clean the task list and create
a file system for usage.
"""

def main():
    
    tasks = []
    cwd = os.getcwd()
    
    with open ("taskList.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = line.replace("\\n", "")
            line = line.replace("\\", "")
            line = line.replace(".\t", " | ")
            line = line.split(" | ")
            tasks.append(line)
    
    if not os.path.exists("part_1"):
        os.mkdir("part_1")
    if not os.path.exists("part_2"):    
        os.mkdir("part_2")
    
    for items in tasks:
        if items[0].startswith("A"):
            mkFolder = f"{cwd}/part_1/Task_{items[0]}"
        else:
            mkFolder = f"{cwd}/part_2/{items[0]}"
        
        if not os.path.exists(mkFolder):
            os.mkdir(mkFolder)
        
        initFile = f"{mkFolder}/{items[0]}_Task.md"
        
        if not os.path.exists(initFile):
            with open(initFile, "w") as f:
                f.write(f"{items[0]} {items[1]}")
                f.close()
        else:
            print("File already exists")
       
                
main()
