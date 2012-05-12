'''
Set up the maya/vray modules here
'''

import maya.cmds as cmds
try:
    # load up vray plugin
    cmds.loadPlugin('vrayformaya', quiet=True)
    # Autoload vray
    cmds.pluginInfo('vrayformaya', edit=True, autoload=True)
    # change renderer to vray
    cmds.setAttr('defaultRenderGlobals.ren', 'vray', type='string')
except :
    print 'VRay not loaded'
    
from exportVRScene import *
from vrayAddGamma import *
from createBaseRenderSettings import *
from createTechPasses import *
from createLightSelect import *
from addSubdivision import *
from addObjectID import *
from remSubdivision import *
from enableSubdivision import *
from vrayConvertToTiledEXR import *