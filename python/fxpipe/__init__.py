import platform ,os

'''
Set the variables here how you want the paths to work

Set the paths for windows, osx, linux as you see fit here.

'''

win_jobpath = 'z:/job'
osx_jobpath = '/Volumes/job'
lin_jobpath = '/mnt/job'
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
    print 'Seq environment variable not set'
    shot = ''

### DO NOT CHANGE BELOW THIS LINE ###

### make sure we set the right path based on OS type
if platform.system() == 'Windows':
    jobPath = win_jobpath
if platform.system() == 'Linux':
    jobPath = lin_jobpath
if platform.system() == 'Darwin':
    jobPath = osx_jobpath

def fixPath(inputPath):
    '''
    This function is what is used to transpose paths from one OS to another should these paths exist
    returns the fixed path based on OS type
    '''
    if platform.system() == 'Windows':
        newPath = inputPath.replace (lin_jobpath, win_jobpath)
        newPath = inputPath.replace (osx_jobpath, win_jobpath)
        return newPath
    if platform.system() == 'Linux':
        newPath = inputPath.replace (win_jobpath, lin_jobpath)
        newPath = inputPath.replace (osx_jobpath, lin_jobpath)
        return newPath
    if platform.system() == 'Darwin':
        newPath = inputPath.replace (lin_jobpath, osx_jobpath)
        newPath = inputPath.replace (win_jobpath, osx_jobpath)
        return newPath
