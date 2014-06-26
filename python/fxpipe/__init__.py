import platform ,os, sys, re, json


"""
Set the variables here how you want the paths to work

Set the paths for windows, osx, linux as you see fit here.

"""

### have to declare global vars so maya, etc can see them and so the userSetup.py works transparently.
### globals suck but such is life.

global job, seq, shot, curApp, jobPath, jobPathLin, jobPathMaya, jobPathNuke,jobPathOsx, jobPathScripts, jobPathWin, nukeOutPath

jFile = open('%s/config.json' % os.environ['FXPIPEPATH'])
jData = json.load(jFile)

jobPathWin = jData['jobPathWin']
jobPathOsx = jData['jobPathOsx']
jobPathLin = jData['jobPathLin']
jobPathNuke = jData['jobPathNuke']
jobPathMaya = jData['jobPathMaya']
jobPathScripts = jData['jobPathScripts']
nukeOutPath = jData['nkOutputPath']
jFile.close()

### Here you can customize how to get your show/shot/sequence/version information

def getPathData(inputPath):
    jFile = open('%s/config.json' % os.environ['FXPIPEPATH'])
    jData = json.load(jFile)
    jFile.close()
    if platform.system() == 'Windows':
        show = int(jData['showNameWin'])
        seq = int(jData['seqNameWin'])
        shot = int(jData['shotNameWin'])
    if platform.system() == 'Darwin':
        show = int(jData['showNameOsx'])
        seq = int(jData['seqNameOsx'])
        shot = int(jData['shotNameOsx'])
    if platform.system() == 'Linux':
        show = int(jData['showNameLin'])
        seq = int(jData['seqNameLin'])
        shot = int(jData['shotNameLin'])

    return ({'job':inputPath.split('/')[show],'seq':inputPath.split('/')[seq],'shot':inputPath.split('/')[shot]})
'''
def showName(inputPath):
    jFile = open('%s/config.json' % os.environ['FXPIPEPATH'])
    jData = json.load(jFile)
    jFile.close()
    inputPath = inputPath.replace('\\','/')
    return inputPath.split('/')[jData['showName']]


def seqName(inputPath):
    jFile = open('%s/config.json' % os.environ['FXPIPEPATH'])
    jData = json.load(jFile)
    jFile.close()
    inputPath = inputPath.replace('\\','/')
    return inputPath.split('/')[jData['seqName']]

def shotName(inputPath):
    jFile = open('%s/config.json' % os.environ['FXPIPEPATH'])
    jData = json.load(jFile)
    jFile.close()
    inputPath = inputPath.replace('\\','/')
    return inputPath.split('/')[jData['shotName']]
'''

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
