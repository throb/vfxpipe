import maya.cmds as cmds
import maya.mel as mel


def createMaterialSelect():
       
    selNodes = cmds.ls(selection=True) # get selection
    
    mtlSelectToCreate = [] # clean out array
    
    for node in selNodes:
        if cmds.nodeType(node) == 'VRayBlendMtl': #make sure it's a vray blend mat
            mat = (cmds.listConnections('%s.base_material' % (node))[0])
            print mat, node
            if mat != None and mat not in mtlSelectToCreate:
                mtlSelectToCreate.append(mat)
            for n in range(0,9):
                mat = (cmds.listConnections('%s.coat_material_%d' % (node,n))) # go thru each coat and add if it's there
                if mat != None and mat not in mtlSelectToCreate:
                    mtlSelectToCreate.append(mat[0])
        if cmds.nodeType(node) == 'VRayMtl':
            if node not in mtlSelectToCreate:
                mtlSelectToCreate.append(node) 
                
    for curMat in mtlSelectToCreate:
        matSelName = 'mtl_%s' % (curMat) # create a reasonable name
        if not cmds.objExists(matSelName): # make sure it doesn't already exist
            renderElement = mel.eval('vrayAddRenderElement MaterialSelectElement;') # create render element
            renderElement = cmds.rename(renderElement,matSelName) # rename the old to new
            cmds.connectAttr (curMat + '.outColor', renderElement + '.vray_mtl_mtlselect') # connect up the shader to the render element
            cmds.setAttr (renderElement + '.vray_explicit_name_mtlselect', matSelName, type = 'string') # make sure the name that gets shoved in the exr is named the same