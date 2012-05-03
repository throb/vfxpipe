import maya.cmds as cmds
import maya.mel as mel

def createTechPasses():
    '''
    Creates tech passes for rendering
    zdepth, xyz, normals, gi, spec, reflection, lighting, uv, top/down
    TODO : topdown not working well due to strange creation methods
    '''

    # first we make the sampler node as we will use this twice
    samplerNodeName = 'util_sampler_node'
    if not cmds.objExists(samplerNodeName) :
        samplerNode = cmds.shadingNode('samplerInfo', asUtility=True)
        samplerNode = cmds.rename(samplerNode, samplerNodeName)
    # now we make the xyz point render element
    layerToMake = 'XYZ_tex'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        cmds.rename (renderElement,layerToMake)
        cmds.setAttr (layerToMake + '.vray_explicit_name_extratex', 'world_xyz', type = 'string')
        cmds.setAttr (layerToMake + '.vray_considerforaa_extratex', 0)
        cmds.connectAttr (samplerNode + '.pointWorld', 'XYZ_tex.vray_texture_extratex')
    # now we make the normals render element
    layerToMake = 'normals'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        cmds.rename (renderElement,layerToMake)
        cmds.setAttr (layerToMake + '.vray_explicit_name_extratex', 'normals', type = 'string')
        cmds.connectAttr (samplerNode + '.normalCamera', layerToMake + '.vray_texture_extratex')    
    # uv render element
    layerToMake = 'uv'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        cmds.rename (renderElement,layerToMake)
        cmds.setAttr (layerToMake + '.vray_explicit_name_extratex', 'uv', type = 'string')
        cmds.connectAttr (samplerNode + '.uvCoord.uCoord', layerToMake + '.vray_texture_extratex.vray_texture_extratexR')    
        cmds.connectAttr (samplerNode + '.uvCoord.vCoord', layerToMake + '.vray_texture_extratex.vray_texture_extratexG')
        cmds.setAttr(layerToMake + '.vray_filtering_extratex', 0)
    # add zdepth unclamped and unfiltered
    layerToMake = 'zdepth'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement zdepthChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
        cmds.setAttr(renderElement + '.vray_depthClamp', 0)
        cmds.setAttr(renderElement + '.vray_filtering_zdepth', 0)
    # add zdepth filtered
    layerToMake = 'zdepthAA'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement zdepthChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
        cmds.setAttr(renderElement + '.vray_depthClamp', 0)
        cmds.setAttr(renderElement + '.vray_filtering_zdepth', 1)    
    # add base render layers for recomp
    layerToMake = 'gi'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement giChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
        cmds.setAttr (renderElement + '.vray_name_gi', layerToMake, type = 'string')
    layerToMake = 'lighting'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement lightingChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
    layerToMake = 'reflection'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement reflectChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
    layerToMake = 'specular'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement specularChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
    # create top down
    layerToMake = 'topdown'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        renderElement = cmds.rename (renderElement,layerToMake)
        cmds.setAttr (renderElement + '.vray_explicit_name_extratex', layerToMake, type = 'string')
        # now create the vray plugin with no placement on UV (0 = none, 1 = 2d, 2 = 3d)
        newNode = mel.eval('vrayCreateNodeFromDll ("topdown_tex", "texture", "TexFalloff", 2);')
        newNode = cmds.rename('topdown_tex','topdown_tex')
        cmds.setAttr (newNode + '.direction_type', 2)
        cmds.setAttr (newNode + '.color1', 1, 0, 0, type='double3')
        cmds.setAttr (newNode + '.color2', 0, 1, 0, type='double3')
        cmds.connectAttr (newNode + '.outColor', renderElement + '.vray_texture_extratex')  
        
    # create AO
    layerToMake = 'ao'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        renderElement = cmds.rename (renderElement,layerToMake)
        cmds.setAttr (renderElement + '.vray_explicit_name_extratex', layerToMake, type = 'string')
        newNode = cmds.shadingNode('VRayDirt', name = 'ao_tex', asTexture=True)
        cmds.connectAttr (newNode + '.outColor', renderElement + '.vray_texture_extratex')
        cmds.setAttr (newNode + '.invertNormal', 1)
        cmds.setAttr (newNode + '.ignoreForGi', 0)
        cmds.setAttr (newNode + '.blackColor', -0.5 ,-0.5 ,-0.5, type='double3')
        cmds.setAttr (newNode + '.falloff', 5)
        
        