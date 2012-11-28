import nuke
import os, re, threading, time


# Get the deadlinecommand executable (we try to use the full path on OSX).
deadlineCommand = "deadlinecommand"
if os.path.exists( "/Applications/Deadline/Resources/bin/deadlinecommand" ):
    print( "Using full deadline command path" )
    deadlineCommand = "/Applications/Deadline/Resources/bin/deadlinecommand"

# Get the current user Deadline home directory, which we'll use to store settings and temp files.
deadlineHome = ""
try:
    stdout = os.popen( deadlineCommand + " -GetCurrentUserHomeDirectory" )
    #deadlineHome = stdout.readline()
    deadlineHome = stdout.read()
    stdout.close()
except IOError:
    print( "An error occurred while collecting the user's home directory from Deadline. Please try again, or if this is a persistent problem, contact Deadline Support." )
    sys.exit(1)

deadlineHome = deadlineHome.replace( "\n", "" )
deadlineSettings = deadlineHome + "/settings"
deadlineTemp = deadlineHome + "/temp"

def checkPath (path):
    filesplit = os.path.basename(path).split('_')
    if len(filesplit[0]) != 5 or len(filesplit[1]) !=3 :
        return False
    return True

def processWriteNode():
    try:
        n = nuke.selectedNode()
    except :
        awNodes = nuke.allNodes('AutoWriter')
        n = awNodes[0]
        if len(awNodes) > 1 : 
            nuke.message('Error :\nYou have more than one AutoWrite.  Please select one.')
            return



    if n.Class() == 'AutoWriter':
        with n:
            nodes = nuke.allNodes('Write')
        for curNode in nodes:
            if 'exr' in nuke.filename(curNode).lower():
                outputFile = nuke.filename(curNode)
    elif n.Class() == 'Read' or n.Class == 'Write':
        outputFile = nuke.filename(curNode)
    else:
        nuke.message('Error:\nThis node is not an AutoWrite, Read, or Write')
        return

    if checkPath(outputFile) == True:

        p = nuke.Panel('Send this to Client')
        p.addEnumerationPulldown('For:','WIP Final')
        p.show()

        status =  p.value('For:').lower()
        frameFirst = int(nuke.root()['first_frame'].getValue())-1
        frameLast = int(nuke.root()['last_frame'].getValue())
        frameRange = '%04d-%04d' % (frameFirst, frameLast)

        jobFiles = createDeadlineJobFiles(outputFile, status, frameRange)
        submitToDeadline(jobFiles[0], jobFiles[1])

    else : 
        nuke.message('Error : Your output is not in a format like aa000_000_task_v000\nPlease resolve and try again')

def createClientName(outputPath):
    return os.path.basename(outputPath).split('_')[0] + '_' + os.path.basename(outputPath).split('_')[1] + '_' + re.search('v[0-9]+', outputPath).group(0)

def createDeadlineJobFiles (outputPath, status, frameRange):    

    jobInfoFile = deadlineTemp + ('/python_submit_info.job' )# % jobCount)
    fileHandle = open( jobInfoFile, 'w' )
    fileHandle.write( 'Plugin=Python\n' )    
    fileHandle.write( 'Name=CLIENT:%s\n' % createClientName(outputPath))
    fileHandle.write( 'Pool=process\n')
    fileHandle.write( 'Group=none\n')
    fileHandle.write( 'Priority=75\n')
    fileHandle.write( 'ChunkSize=1\n')
    fileHandle.write( 'Frames=1\n')
    fileHandle.close()

    pluginInfoFile = deadlineTemp + ("/python_plugin_info.job" )# % jobCount)
    fileHandle = open( pluginInfoFile, "w" )    
    fileHandle.write( 'ScriptFile=Z:\\software\\vfxpipe\\python\\processClientOutput.py\n')
    fileHandle.write( 'Arguments=-f %s -i %s -s %s\n' % (frameRange, outputPath, status))
    fileHandle.write( 'Version=2.6\n')
    fileHandle.close()

    return jobInfoFile, pluginInfoFile

def submitToDeadline (jobInfoFile, pluginInfoFile):
    submitCmd = ('%s %s %s' % (deadlineCommand, jobInfoFile, pluginInfoFile))
    stdout = os.popen(submitCmd)
    stdoutParse = stdout.read()
    jobID = stdoutParse.split('=')[len(stdoutParse.split('='))-1]
    jobID = jobID.strip()    
    nuke.message('Job Submitted : %s' % (jobID))

if __name__ == "__main__":
    processWriteNode()

def submitJobProgress():
    task = nuke.ProgressTask("Self Destructing")
    task.setMessage("Deleting files")
    for i in xrange( 0, 100 ):
        if task.isCancelled():
            nuke.executeInMainThread( nuke.message, args=( "Phew!" ) )
            break;
        task.setProgress(i)
        time.sleep( 0.5 )
    threading.Thread( None, selfDestruct ).start()