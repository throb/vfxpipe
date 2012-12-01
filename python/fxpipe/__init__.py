import platform ,os, sys, re

"""
Set the variables here how you want the paths to work

Set the paths for windows, osx, linux as you see fit here.

"""

### have to declare global vars so maya, etc can see them and so the userSetup.py works transparently.
### globals suck but such is life.

global job, seq, shot, curApp, jobPath, jobPathLin, jobPathMaya, jobPathNuke,jobPathOsx, jobPathScripts, jobPathWin

jobPathWin = 'z:/job'
jobPathOsx = '/Volumes/work/job'
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

### Here you can customize how to get your show/shot/sequence/version information

def showName(inputPath):
    inputPath = inputPath.replace('\\','/')
    return inputPath.split('/')[2]

def seqName(inputPath):
    inputPath = inputPath.replace('\\','/')
    return inputPath.split('/')[4]

def shotName(inputPath):
    inputPath = inputPath.replace('\\','/')
    return inputPath.split('/')[5]

def versionNumber(inputPath):
    versionData = re.search('v[0-9]+',inputPath)
    if not versionData :
        versionData = re.search('V[0-9]+',inputPath)
    if not versionData :
        versionData = 'v000'
    else:
        versionData = versionData.group(0)
    return versionData

def framePad(inputPath):
    pattern = re.compile(r'%[0-9]+d')
    framePadData = pattern.findall(inputPath)
    if framePadData:
        out = framePadData[0]
        outFormat = out
    
    if not framePadData:
        pattern = re.compile(r'#')
        framePadData = pattern.findall(inputPath)
        out = ''
        for n in range(len(framePadData)):
            out = out + framePadData[n]
        outFormat = '%' + '0%0dd' % (len(framePadData))
    return out, outFormat

def framePadReplace(inputPath, replaceNumber):
    padString, padFormat = framePad(inputPath)
    paddedNumber = padFormat % (int(replaceNumber))
    return (inputPath.replace(padString, paddedNumber))

### END DATA Collection

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
