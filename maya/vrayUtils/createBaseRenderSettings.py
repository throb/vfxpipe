import maya.cmds as cmds
import maya.utils as utils
import maya.mel as mel

def createBaseRenderSettings(job='', seq='', shot=''):
    
    vrayLoaded = False
    #let's load VRay
    try:
        # load up vray plugin
        cmds.loadPlugin('vrayformaya', quiet=True)
        # Autoload vray
        cmds.pluginInfo('vrayformaya', edit=True, autoload=True)
        # change renderer to vray
        cmds.setAttr('defaultRenderGlobals.ren', 'vray', type='string')
        vrayLoaded = True
        
    except :
        print 'VRay not loaded'    
    
    
    '''
    Set up some basic render settings that get reasonable speed and quality along with consistency
    Uses the dmc sampler and gauss filtering
    '''
    if vrayLoaded == True :
        cmds.setAttr('vraySettings.sys_low_thread_priority', 1)
        cmds.setAttr('vraySettings.dontSaveImage', 1)
        cmds.setAttr('vraySettings.imageFormatStr', 'exr (multichannel)', type='string')
        cmds.setAttr('vraySettings.imgOpt_exr_compression', 3)
        cmds.setAttr('vraySettings.imgOpt_exr_bitsPerChannel', 16)
        cmds.setAttr('vraySettings.imgOpt_exr_autoDataWindow', 1)
        cmds.setAttr('vraySettings.samplerType',1)
        cmds.setAttr('vraySettings.dmcMinSubdivs', 1)
        cmds.setAttr('vraySettings.dmcMaxSubdivs', 4)
        cmds.setAttr('vraySettings.dmcThreshold', 0.051)
        cmds.setAttr('vraySettings.sRGBOn', 1)
        cmds.setAttr('vraySettings.vfbOn', 1)
        cmds.setAttr('vraySettings.aaFilterType', 6)
        cmds.setAttr('vraySettings.aaFilterSize', 2.0)
        cmds.setAttr('vraySettings.cmap_gamma', 2.2)
        cmds.setAttr('vraySettings.cmap_adaptationOnly', 1)
        cmds.setAttr('vraySettings.dmcs_adaptiveAmount', 0.85)
        cmds.setAttr('vraySettings.sys_rayc_dynMemLimit', 40000) 
        exrAttrs = ("job='%s';seq='%s';shot='%s'") % (job, seq, shot)
        cmds.setAttr('vraySettings.imgOpt_exr_attributes', exrAttrs, type='string')
            
        
        

        
