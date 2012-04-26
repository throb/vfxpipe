import platform ,os, sys

'''
Set the variables here how you want the paths to work

Set the paths for windows, osx, linux as you see fit here.

'''
### have to declare global vars so maya, etc can see them and so the userSetup.py works transparently.
### globals suck but such is life.

global job, seq, shot, curApp, jobPath, jobPathLin, jobPathMaya, jobPathNuke,jobPathOsx, jobPathScripts, jobPathWin

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

# test for what called the pipeline
if 'maya' in sys.executable.lower() : 
    curApp = 'maya'
elif 'nuke' in sys.executable.lower() : 
    curApp = 'nuke'
else:
    curApp = None



try:
    job = os.environ['job']
except:
    job = ''
try:    
    seq = os.environ['seq']
except:
    seq = ''
try:
    shot = os.environ['shot']
except:
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
