import random

dirTextPath = ""
exitCode = int(0)
currentDir = 0
fileNames = []
cdDirName = ""
filesMatches = 0

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
            cdDirName = commandLineInput.lstrip("cd ")
            

            #Iterate through the fileNames array, and relate the current working directory with the files record.

            for x in range(len(fileNames)):
                if fileNames[x][1] == 1 and cdDirName == fileNames[x][0] and currentDir == fileNames[x][3]:
                    currentDir = fileNames[x][2]
                    dirTextPath = "/"+fileNames[x][0]
            
            
            
#CD \ command used to go back to root dir    
        if commandLineInput.startswith("cd \\"):
            currentDir = 0
            dirTextPath = ""
        
          
           
#LIST Command 
        if commandLineInput == "ls" or commandLineInput == "ls ":
            
            
            for x in range(len(fileNames)):
                
                if  fileNames[x][3] == currentDir:
            
                    if fileNames[x][1] == 1:
                        print(fileNames[x][0] + " [D]")
                        filesMatches = filesMatches + 1
                    else:
                        print(fileNames[x][0])
                        filesMatches = filesMatches + 1
                        
            print ("\n[total",filesMatches, "files]")
            filesMatches = 0
               
                
            
     
#TOUCH command
        if commandLineInput == "touch":
            print ("Enter file name:")
            touchParam = input()
            
           
            if touchParam == "":
                print ("Please enter a valid file name")
            
            
            #Creates the file in the filenames table.
            #Array structure is: "NAME", "DIR or FILE SWITCH","RND hashID","WORKING DIRECTORY"
            
            else:
                fileHash = random.randint(1,9999999)
                
                fileNames.append([touchParam,0,fileHash,currentDir])
                
                print (touchParam + " file created.")
            
                
                
#MKDIR command
        if commandLineInput == "mkdir":
            print ("Enter directory name:")
            mkdirParam = input()
           
            if mkdirParam == "":
                print ("Please enter a valid directory name")
            
            #Similar to the file in the filenames table, directories get created using "1" instead, in the DIRorFILE switch.
            #Array structure is: "NAME", "DIR or FILE SWITCH","RND hashID","WORKING DIRECTORY"
            
            else:
                
                fileHash = random.randint(1,9999999)
                
                fileNames.append([mkdirParam,1,fileHash,currentDir])
                
                print (mkdirParam + " directory created.")
                
                
    
#HELP command
        if commandLineInput == "help":
            
            print ("\n")
            print ("cd \t \'Changes directories. Example: \"cd temp\". Use \"cd \\\" to go back to the root directory\'") 
            print ("ls \t \'Lists the files and directories only in the current working directory.\'") 
            print ("mkdir \t \'Creates a directory. Type \"mkdir\" followed by enter, then type the name of the directory\'") 
            print ("touch \t \'Creates a file. Type \"touch\" followed by enter, then type the name of the file\'") 
            print ("exit \t \'Exit jorgOS'") 
            print ("\n**Notes and caveats**\n")
            print ("File system commands must be issued from the working directory only.")
            print ("File system commands are lowercase.\nFiles and directories follow case formating")
            print ("This version of jorgOS currently doesnt supports \"cd ..\" directory traversal, please use \"cd \\\" instead.")
            print ("\n")
        
     
                
                
                
                
                
            
                
                
           
           
           
            
  
        
   
       
        
  
    

    
    








