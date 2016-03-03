# file rename program for reference and system genereated summaries according to rouge-2.0.0 specification
import os
pathforrefrencesummary = "/home/kalani/workspace/textrank.py/Goldsummaries"
pathforSystemgeneratessummary = "/home/kalani/workspace/textrank.py/summaries"      
i = 0
j = 0
for file_name in os.listdir(pathforrefrencesummary):
    for file_n in os.listdir(pathforSystemgeneratessummary):
        if file_name == file_n:
            i = i + 1
            j = j + 1
            newname_for_reference = "yo_reference" + str(i) + ".txt"
            newname_for_system = "yo_system" + str(j) + ".txt"
            print "renaming file " + file_name + " to-->" + newname_for_reference
            print "renaming file " + file_n + " to-->" + newname_for_system  
            os.rename(os.path.join(os.getcwd(), "Goldsummaries", file_name), os.path.join(os.getcwd(), "renamedref", newname_for_reference))
            os.rename(os.path.join(os.getcwd(), "summaries", file_name), os.path.join(os.getcwd(), "renamedsys", newname_for_system))
