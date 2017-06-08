

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
    layerToMake = 'pWorld'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        cmds.rename (renderElement,layerToMake)
        cmds.setAttr (layerToMake + '.vray_explicit_name_extratex', layerToMake, type = 'string')
        cmds.setAttr (layerToMake + '.vray_considerforaa_extratex', 0)
        cmds.setAttr (layerToMake + '.vray_filtering_extratex', 0)
        cmds.connectAttr (samplerNodeName + '.pointWorld', layerToMake+'.vray_texture_extratex')
    layerToMake = 'pObject'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        cmds.rename (renderElement,layerToMake)
        cmds.setAttr (layerToMake + '.vray_explicit_name_extratex', layerToMake, type = 'string')
        cmds.setAttr (layerToMake + '.vray_considerforaa_extratex', 0)
        cmds.setAttr (layerToMake + '.vray_filtering_extratex', 0)
        cmds.connectAttr (samplerNodeName + '.pointObj', layerToMake+'.vray_texture_extratex')        
    # now we make the normals render element
    layerToMake = 'normals'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement normalsChannel;')
        cmds.rename (renderElement,layerToMake)
        cmds.setAttr(layerToMake + '.vray_filtering_normals', 0)
    # uv render element
    layerToMake = 'uv'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        cmds.rename (renderElement,layerToMake)
        cmds.setAttr (layerToMake + '.vray_explicit_name_extratex', 'uv', type = 'string')
        cmds.connectAttr (samplerNodeName + '.uvCoord.uCoord', layerToMake + '.vray_texture_extratex.vray_texture_extratexR')    
        cmds.connectAttr (samplerNodeName + '.uvCoord.vCoord', layerToMake + '.vray_texture_extratex.vray_texture_extratexG')
        cmds.setAttr(layerToMake + '.vray_filtering_extratex', 0)
    # add zdepth unclamped and unfiltered
    layerToMake = 'zdepthNoAA'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
        cmds.rename (renderElement,layerToMake)
        cmds.setAttr (layerToMake + '.vray_explicit_name_extratex', layerToMake, type = 'string')
        cmds.setAttr (layerToMake + '.vray_considerforaa_extratex', 0)
        cmds.setAttr (layerToMake + '.vray_filtering_extratex', 0)
        cmds.connectAttr (samplerNodeName + '.pointCameraZ', layerToMake+'.vray_texture_extratexR')        
    # add zdepth filtered
    layerToMake = 'zdepthAA'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement zdepthChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
        cmds.setAttr(renderElement + '.vray_depthClamp', 1)
        cmds.setAttr(renderElement + '.vray_filtering_zdepth', 1)  
        cmds.setAttr(layerToMake + '.vray_name_zdepth','zDepthAA', type='string')  
    # add base render layers for recomp
    layerToMake = 'gi'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement giChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
        cmds.setAttr (renderElement + '.vray_name_gi', layerToMake, type = 'string')
    layerToMake = 'diffuse'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement diffuseChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)
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
    layerToMake = 'refraction'
    if not cmds.objExists(layerToMake) :
        renderElement = mel.eval('vrayAddRenderElement refractChannel;')
        renderElement = cmds.rename (renderElement, layerToMake)


    ### Look for the shaders so we can either add the SSS or not.  Don't want to waste the layers
    shaders = cmds.ls(mat=True, showType = True)
    createSSS = False
    createIllum = False
    for shader in shaders:
        surfaceShader = cmds.listConnections (shader, type='shadingEngine')
        if 'SSS' in surfaceShader[0].lower() or 'skin' in surfaceShader[0].lower():
            createSSS = True
        if 'light' in surfaceShader[0].lower():
            createIllum = True    
    if createSSS == True:
        layerToMake = 'sss'        
        if not cmds.objExists(layerToMake) :
            renderElement = mel.eval('vrayAddRenderElement FastSSS2Channel;')
            renderElement = cmds.rename (renderElement, layerToMake)
    if createIllum == True:
        layerToMake = 'selfIllum'
        if not cmds.objExists(layerToMake) :
            renderElement = mel.eval('vrayAddRenderElement selfIllumChannel;')
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
        cmds.setAttr (renderElement + '.enabled', 0)
        newNode = cmds.shadingNode('VRayDirt', name = 'ao_tex', asTexture=True)
        cmds.connectAttr (newNode + '.outColor', renderElement + '.vray_texture_extratex')
        cmds.setAttr (newNode + '.invertNormal', 1)
        cmds.setAttr (newNode + '.ignoreForGi', 0)
        cmds.setAttr (newNode + '.blackColor', -0.5 ,-0.5 ,-0.5, type='double3')
        cmds.setAttr (newNode + '.falloff', 5)
