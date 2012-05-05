import maya.mel as mel
import maya.cmds as cmds
import math

def addObjectID():
    
    '''
    add object id to selected objects.  check for existing object ID and add new one if there are existing.
    '''
    
    
    nodeList = cmds.ls(selection = True, dag=True, lf=True, type = 'mesh') # find shape nodes of current selection
    
    allNodes = cmds.ls(type = 'mesh') # look for meshes only in the scene
    
    existingIDs = [0]
    
    for node in allNodes: # go through and check for existing object IDs here
        attrList = cmds.listAttr(node)
        if 'vrayObjectID' in attrList:
            existingIDs.append (cmds.getAttr ('%s.vrayObjectID' % node))
    
    newObjectID = 1
    
    existingIDs.sort() # this is just for cleanliness.  not required.
    
    for id in range(max(existingIDs)+2): # look through the list and let's find an unused number if that exists we need to go one beyond the current values so we can add it if needed
        if id not in existingIDs:
            newObjectID = id
            existingIDs.append(newObjectID)
            break
    
    for node in nodeList:
        attrList = cmds.listAttr(node)
        if 'vrayObjectID' not in attrList:
            print newObjectID
            mel.eval ('vray addAttributesFromGroup %s vray_objectID 1' % node)
            cmds.setAttr('%s.vrayObjectID' % node ,newObjectID)
            renderElements = cmds.ls (type = 'VRayRenderElement')
        
    addedID = False # clear the slate here
    
    attrsToSearch = ['vray_redid_multimatte','vray_greenid_multimatte','vray_blueid_multimatte'] # just looking for these attrs
    
    multiMatteElements = [] # nice and tidy here
    
    for element in renderElements: #go through and find multi matte elements and add them to our list
        if cmds.getAttr('%s.vrayClassType' % element) == 'MultiMatteElement':
            multiMatteElements.append(element)
    
    if len(multiMatteElements) < int(math.modf((newObjectID+2)/3)[1]) : # check amount of multi matte elements against how many we can fit in a render element
        newMMate = mel.eval('vrayAddRenderElement MultiMatteElement') # add the element
        cmds.setAttr('%s.vray_considerforaa_multimatte' % newMMate, 1) #make sure it has AA on it...
        multiMatteElements.append(newMMate)
    
    for element in multiMatteElements: # go through the multimatte list
        for multimatte in attrsToSearch: # we are looking only through the id attributes
            if cmds.getAttr('%s.%s' % (element, multimatte)) == newObjectID : # if we find the ID already just try to skip the rest of the testing
                addedID = True
            if cmds.getAttr('%s.%s' % (element, multimatte)) == 0 and addedID == False : # didn't find anything eh?  good.  we add the id to the multimatte.
                cmds.setAttr('%s.%s' % (element, multimatte), newObjectID)
                addedID = True
