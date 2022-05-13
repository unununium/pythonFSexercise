import uuid
import time
from datetime import datetime



dirTextPath = ""
exitCode = int(0)
currentDir = 0
fileNames = []
cdDirName = ""
filesMatches = 0
dirMatches = 0

print ("Welcome to jorgOS, the most basic FileSystem in the observable universe!\n")
print ("type \"help\", for a list of commands")
print ("\n")

#int main loop

while exitCode != 1:
    commandLineInput = input("<jorgOS " + dirTextPath + "/>: ")

    
    if commandLineInput:
    
    
        if commandLineInput == "":
           exitCode = int(0)
#EXIT command    
        if commandLineInput == "exit" or commandLineInput == "quit":
            print ("Bye!")
            exitCode = int(1)


#CD command accepting dir name parameter
        if commandLineInput.startswith("cd "):
            cdDirName = commandLineInput.split("cd ")
            

            #Iterate through the fileNames array, and relate the current working directory with the files record.

            for x in range(len(fileNames)):
                if fileNames[x][1] == 1 and cdDirName[1] == fileNames[x][0] and currentDir == fileNames[x][3]:
                    currentDir = fileNames[x][2]
                    dirTextPath = "/"+fileNames[x][0]
            
            
            
#CD \ command used to go back to root dir    
        if commandLineInput.startswith("cd \\"):
            currentDir = 0
            dirTextPath = ""
        
          
           
#LIST Command 
        if commandLineInput == "ls" or commandLineInput == "ls ":
            print("\n")

            
            for x in range(len(fileNames)):
                
                if  fileNames[x][3] == currentDir:
                    dt_obj = datetime.fromtimestamp(fileNames[x][5]).strftime('%m/%d/%y %H:%M:%S:%f')
                    dt_obj = dt_obj[:-4]

                    if fileNames[x][1] == 1:
                        print("[D] " + dt_obj + "\t\t\t\t"+  fileNames[x][0])
                        dirMatches = dirMatches + 1

                    else:
                        print("[ ] " + dt_obj + "\t\t\t\t"+  fileNames[x][0])
                        filesMatches = filesMatches + 1
                        
            print ("\n[total:",filesMatches,"files, and",dirMatches,"directories]")
            filesMatches = 0
            dirMatches = 0
            dt_obj = 0
               
                
            
     
#TOUCH command
        
        if commandLineInput.startswith("touch "):
            
            try:
                touchParam = commandLineInput.split("touch ")
           
            except NameError:
                print("enter valid filename")

            #Creates the file in the filenames table.
            #Array structure is: "NAME", "DIR or FILE SWITCH","RND hashID","WORKING DIRECTORY,PARENT DIRECTORY,TIMESTAMP"
            
            else:
                
                
                if (touchParam[1] != ""):

                    for x in range(len(fileNames)):

                        if(fileNames[x][0] == touchParam[1] and fileNames[x][3] == currentDir):
                            print("\nCant touch this! ile or directory \"" + touchParam[1] + "\" already exists.")
                            break
                            
                    else:
                        fileHash = str(uuid.uuid4())
                        #fileHash = random.randint(1,9999999)
                        timestamp = time.time()
                        fileNames.append([touchParam[1],0,fileHash,currentDir,currentDir,timestamp])
                        print ("\"" + touchParam[1] + "\" file created.")
                


#MKDIR command
        
        if commandLineInput.startswith("mkdir "):
            try:
                mkdirParam = commandLineInput.split("mkdir ")
                
                    
           
            except:
                print("enter valid filename")

            #Creates the file in the filenames table.
            #Array structure is: "NAME", "DIR or FILE SWITCH","RND hashID","WORKING DIRECTORY,PARENT DIRECTORY,TIMESTAMP"
            
            else:
                
                
                if (mkdirParam[1] != ""):

                    for x in range(len(fileNames)):

                        if(fileNames[x][0] == mkdirParam[1] and fileNames[x][3] == currentDir):
                            print("\nCant create directory! \"" + mkdirParam[1] + "\" already exists.")
                            break
                            
                    else:
                        fileHash = str(uuid.uuid4())
                        
                        #fileHash = random.randint(1,9999999)
                        timestamp = time.time()
                        fileNames.append([mkdirParam[1],1,fileHash,currentDir,currentDir,timestamp])
                        print ("\"" + mkdirParam[1] + "\" directory created.")

                #print(fileNames)


    
#HELP command
        if commandLineInput == "help":
            
            print ("\n")
            print ("cd \t \'Changes directories. Example: \"cd temp\". Use \"cd \\\" to go back to the root directory\'") 
            print ("ls \t \'Lists the files and directories only in the current working directory.\'") 
            print ("mkdir \t \'Creates a directory. Example: Type \"mkdir temp\"'") 
            print ("touch \t \'Creates a file. Example: \"touch temp\"\'") 
            print ("exit \t \'Exit jorgOS'") 
            print ("\n**Notes and caveats**\n")
            print ("File system commands must be issued from the working directory only.")
            print ("File system commands are lowercase.\nFiles and directories follow case formating")
            print ("This version of jorgOS currently doesnt supports \"cd ..\" directory traversal, please use \"cd \\\" instead.")
            print ("\n")
        
     
                
                
                
                
                
            
                
                
           
           
           
            
  
        
   
       
        
  
    

    
    








