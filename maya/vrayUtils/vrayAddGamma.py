import maya.cmds as cmds
import maya.mel as mel

def vrayAddGamma(): 
    '''
    Add VRay gamma parameters to the extra attributes and set them to sRGB
    This will need to br clicked/run twice because maya doesn't really get the fact that things have been created.
    Bonkers Maya!  Bonkers!
    '''
    #import maya.cmds as cmds	
    #import maya.mel as mel
    import os
    allFileNodes = cmds.ls(type='file') # look for file nodes
    nonFloatFiles = []
    for curFile in allFileNodes:

        cmds.setAttr (curFile + '.filterType', 0) # turn off the damned filtering
        fileName = cmds.getAttr(curFile + '.fileTextureName') # get the filename
        if fileName != '': # test for stupid user
            fileExt = os.path.splitext(fileName)[1].lower()[1:] # get the extention
            if fileExt != 'exr' or fileExt != '.hdr': # test for hdr and exr
                nonFloatFiles.append(curFile)
                mel.eval('vray addAttributesFromGroup ' + curFile + ' vray_file_gamma 1') # add the proper vray stuff to the attribs

    allFileNodes = cmds.ls(type='file') # look for file nodes
    for curFile in nonFloatFiles:
        if cmds.objExists(curFile + '.vrayFileGammaEnable'):
            cmds.setAttr (curFile + '.vrayFileGammaEnable', 1) # make sure the gamma correction is enabled
            cmds.setAttr (curFile + '.vrayFileColorSpace', 2) # set it to sRGB
        else :
            print 'The attribute for VRay is not found in %s' % curFile # may as well print something here