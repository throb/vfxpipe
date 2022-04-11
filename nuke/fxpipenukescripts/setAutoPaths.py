import nuke
import re

def setOutputPath(extension='exr'):
    pathName = nuke.root()['name'].getValue()

    pathItems = pathName.split('/')
    job = pathItems[2]
    seq = pathItems[4]
    shot = pathItems[5]
    task = pathItems[6]
    resolution = '%sx%s' % (nuke.thisNode().width(),nuke.thisNode().height())
    try:
        version = re.search('v[0-9]+',pathName.lower()).group(0)[1:]
        version = '%03d' % (int(version))
        newPath = 'z:/job/%s/shots/%s/%s/%s/images/v%s/%s/%s/%s_%s_v%s.####.%s' % (job, seq, shot, task, version, resolution,extension, shot, task, version, extension)
    except:
        print ('Version problem')
        newPath = ''

    return  newPath

def setLutPath():
    pathName = nuke.root()['name'].getValue()
    
    pathItems = pathName.split('/')
    job = pathItems[2]
    seq = pathItems[4]
    shot = pathItems[5]    
    
    lutPath = 'z:/job/%s/shots/%s/%s/lut/%s.cube' % (job, seq, shot, shot)
    
    return lutPath