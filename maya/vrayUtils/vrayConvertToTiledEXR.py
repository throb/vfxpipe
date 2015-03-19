import maya.cmds as cmds
import maya.mel as mel
import sys
import platform
import os, sys, subprocess, platform, re
import pymel.core as pm

def vrayConvertToTiledEXR(): 
    '''
    Take all images that are NOT exr files and convert them to tiled exr files

    '''

    # setup a window
    window = pm.window()
    pm.columnLayout()
    
    mayaVersion = re.search('[0-9]+',re.search('maya[0-9]+',sys.argv[0].lower()).group(0)).group(0) # look for the 2012 or 2013 etc in path name
    pathToVRayTools = os.path.normpath(os.environ['VRAY_TOOLS_MAYA%s_x64' % (mayaVersion)]) # make sure we have the right vray tools path
    allFileNodes = cmds.ls(type='file') # look for file nodes
    progressControl = pm.progressBar(maxValue=len(allFileNodes)-1, width=300) # make sure window is prepped for size
    if platform.system() == 'Windows':
        execFile = '"%s/img2tiledexr.exe"' % (pathToVRayTools) # needs quotes in case there are spaces in filename
    else:
        execFile = '"%s/img2tiledexr"' % (pathToVRayTools) # needs quotes in case there are spaces in filename
    if os.path.exists(os.path.normpath(execFile.replace('"',''))) == False:    
        print '%s does not exist.  exiting.' % (execFile)
        sys.exit(1)
    nonFloatFiles = []
    pm.showWindow( window )
    for curFile in allFileNodes:
        pm.progressBar(progressControl,edit=True,step=1)
        curFileName = cmds.getAttr(curFile + '.fileTextureName')
        if 'exr' not in os.path.splitext(curFileName)[1].lower(): #check for exr
            print 'Converting %s' % (curFileName)
            newFileName = '%s_tiled.exr' % ( os.path.splitext(curFileName)[0] )
            
                                
            subprocess.call(execFile + ' ' + curFileName + ' ' + newFileName, shell=True) #actually do the work
            if os.path.exists(newFileName):
                cmds.setAttr(curFile + '.fileTextureName', newFileName, type='string') # replace old filename with a new one
                if cmds.objExists(curFile + '.vrayFileGammaEnable'):
                    cmds.setAttr (curFile + '.vrayFileGammaEnable', 0) # make sure the gamma correction is disabled if it's there
        else:
            print 'Skipping %s' % (curFileName)
                
             