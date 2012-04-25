import maya.cmds as cmds

def createBaseRenderSettings(job='', seq='', shot=''):
    '''
    Set up some basic render settings that get reasonable speed and quality along with consistency
    Uses the dmc sampler and gauss filtering
    '''
    cmds.setAttr('vraySettings.sys_low_thread_priority', 1)
    cmds.setAttr('vraySettings.imageFormatStr', 'exr (multichannel)', type='string')
    cmds.setAttr('vraySettings.imgOpt_exr_compression', 3)
    cmds.setAttr('vraySettings.imgOpt_exr_bitsPerChannel', 16)
    cmds.setAttr('vraySettings.imgOpt_exr_autoDataWindow', 1)
    exrAttrs = ("job='%s';seq='%s';shot='%s'") % (job, seq, shot)
    cmds.setAttr('vraySettings.imgOpt_exr_attributes', exrAttrs)
    cmds.setAttr('vraySettings.sRGBOn', 1)
    cmds.setAttr('vraySettings.vfbOn', 1)
    cmds.setAttr('vraySettings.aaFilterType', 6)
    cmds.setAttr('vraySettings.aaFilterSize', 2.5)
    cmds.setAttr('vraySettings.cmap_gamma', 2.2)
    cmds.setAttr('vraySettings.cmap_adaptationOnly', 1)
    cmds.setAttr('vraySettings.dmcs_adaptiveAmount', 0.9)
    cmds.setAttr('vraySettings.sys_low_thread_priority', 1)
    cmds.setAttr('vraySettings.sys_rayc_dynMemLimit', 8000)