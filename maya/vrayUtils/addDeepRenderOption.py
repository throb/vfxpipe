import maya.cmds as cmds

def addDeepRenderOption():
    
    vrayOutputSettings='''
from vray.utils import *
import maya.cmds as cmds
import os
# get current render layer
curRenderLayer = '%s' % (cmds.editRenderLayerGlobals( query=True, currentRenderLayer=True ))
if curRenderLayer == 'defaultRenderLayer':
    curRenderLayer = ''
else:
    curRenderLayer = '_%s' % (curRenderLayer)
# get current maya scene file
curMayaFile = os.path.splitext(os.path.basename(cmds.file(query=True, list=True)[0]))[0]
# get resolution details
resRender = "%dx%d" % (cmds.getAttr("defaultResolution.width"),cmds.getAttr("defaultResolution.height"))
#create output writer plugin
p=create("OutputDeepWriter", "deepWriter")
# set output path here
outputPath = "%s/%s/%s/%s/%s/vrst/%s%s..vrst" % (cmds.workspace(lfw=True)[0],cmds.workspace(fre="images"),curMayaFile,curRenderLayer,resRender,curMayaFile,curRenderLayer)
outputPath = outputPath.strip()
if os.path.exists(os.path.dirname(outputPath)) == False:
    os.makedirs(os.path.dirname(outputPath))

print 'Rendering to : %s' % (outputPath)
# set path and filename for output
p.set("file", outputPath)
# disable normal output to prevent errors
findByType("SettingsOutput")[0].set("img_file", "")
    
    
    '''
    
    cmds.setAttr ('vraySettings.postTranslatePython',vrayOutputSettings, type='string')
