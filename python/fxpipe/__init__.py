import platform ,os

'''
Set the variables here how you want the paths to work

Set the paths for windows, osx, linux as you see fit here.

'''

jobPathWin = 'z:/job'
jobPathOsx = '/Volumes/job'
jobPathLin = '/mnt/job'

### END JOB PATH CUSTOMIZE

'''
Customize this for where your nuke scripts will be located that are show specific for each application
this will work out to (for nuke) :
jobPath + nukeJobPath = z:/job/myjobname/common/nuke
This is where __init__ files should be placed
'''

jobPathNuke = 'common/nuke'
jobPathMaya = 'common/maya'
jobPathScripts = 'common/python'

### END APP PATH CUSTOMIZE

try:
    job = os.environ['job']
except:
    print 'Job environment variable not set'
    job = ''
try:    
    seq = os.environ['seq']
except:
    print 'Seq environment variable not set'
    seq = ''
try:
    shot = os.environ['shot']
except:
    print 'Shot environment variable not set'
    shot = ''

### DO NOT CHANGE BELOW THIS LINE ###

### make sure we set the right path based on OS type
if platform.system() == 'Windows':
    jobPath = jobPathWin
if platform.system() == 'Linux':
    jobPath = jobPathLin
if platform.system() == 'Darwin':
    jobPath = jobPathOsx

def fixPath(inputPath):
    '''
    This function is what is used to transpose paths from one OS to another should these paths exist
    returns the fixed path based on OS type
    '''
    if platform.system() == 'Windows':
        newPath = inputPath.replace (jobPathLin, jobPathWin)
        newPath = inputPath.replace (jobPathOsx, jobPathWin)
        return newPath
    if platform.system() == 'Linux':
        newPath = inputPath.replace (jobPathWin, jobPathLin)
        newPath = inputPath.replace (jobPathOsx, jobPathLin)
        return newPath
    if platform.system() == 'Darwin':
        newPath = inputPath.replace (jobPathLin, jobPathOsx)
        newPath = inputPath.replace (jobPathWin, jobPathOsx)
        return newPath
