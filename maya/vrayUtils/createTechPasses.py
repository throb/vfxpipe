import maya.cmds as cmds
import maya.mel as mel

def createTechPasses():
    '''
    Creates tech passes for rendering
    zdepth, xyz, normals, gi, spec, reflection, lighting, uv, top/down
    TODO : topdown not working well due to strange creation methods
    '''

    # first we make the sampler node as we will use this twice
    samplerNode = cmds.shadingNode('samplerInfo', asUtility=True)    
    # now we make the xyz point render element
    renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
    cmds.rename (renderElement,'XYZ_tex')
    cmds.setAttr ('XYZ_tex.vray_explicit_name_extratex', 'world_xyz', type = 'string')
    cmds.setAttr ('XYZ_tex.vray_considerforaa_extratex', 0)
    cmds.connectAttr (samplerNode + '.pointWorld', 'XYZ_tex.vray_texture_extratex')
    # now we make the normals render element
    renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
    cmds.rename (renderElement,'normals')
    cmds.setAttr ('normals.vray_explicit_name_extratex', 'normals', type = 'string')
    cmds.connectAttr (samplerNode + '.normalCamera', 'normals.vray_texture_extratex')    
    # uv render element
    renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
    cmds.rename (renderElement,'uv')
    cmds.setAttr ('uv.vray_explicit_name_extratex', 'uv', type = 'string')
    cmds.connectAttr (samplerNode + '.uvCoord.uCoord', 'uv.vray_texture_extratex.vray_texture_extratexR')    
    cmds.connectAttr (samplerNode + '.uvCoord.vCoord', 'uv.vray_texture_extratex.vray_texture_extratexG')
    cmds.setAttr('uv.vray_filtering_extratex', 0)
    # add zdepth unclamped and unfiltered
    #renderElement = mel.eval('vrayAddRenderElement zdepthChannel;')
    #renderElement = cmds.rename (renderElement, 'zdepth')
    #cmds.setAttr(renderElement + '.vray_depthClamp', 0)
    #cmds.setAttr(renderElement + '.vray_filtering_zdepth', 0)
    # add zdepth filtered
    renderElement = mel.eval('vrayAddRenderElement zdepthChannel;')
    renderElement = cmds.rename (renderElement, 'zdepthAA')
    cmds.setAttr(renderElement + '.vray_depthClamp', 0)
    cmds.setAttr(renderElement + '.vray_filtering_zdepth', 1)    
    # add base render layers for recomp
    renderElement = mel.eval('vrayAddRenderElement giChannel;')
    renderElement = cmds.rename (renderElement, 'gi')
    cmds.setAttr (renderElement + '.vray_name_gi', 'gi', type = 'string')
    renderElement = mel.eval('vrayAddRenderElement lightingChannel;')
    renderElement = cmds.rename (renderElement, 'lighting')
    renderElement = mel.eval('vrayAddRenderElement reflectChannel;')
    renderElement = cmds.rename (renderElement, 'reflection')
    renderElement = mel.eval('vrayAddRenderElement specularChannel;')
    renderElement = cmds.rename (renderElement, 'specular')
    # create top down -- CURRENTLY NOT ACTIVE DUE TO CREATION ISSUE
    '''
    renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
    renderElement = cmds.rename (renderElement,'topdown')
    cmds.setAttr (renderElement + '.vray_explicit_name_extratex', 'topdown', type = 'string')
    # now create the vray plugin with no placement on UV (0 = none, 1 = 2d, 2 = 3d)
    newNode = mel.eval('vrayCreateNodeFromDll ("topdown_tex", "texture", "TexFalloff", 2);')
    newNode = cmds.rename('topdown_tex','topdown_tex')
    cmds.setAttr (newNode + '.direction_type', 2)
    cmds.setAttr (newNode + '.color1', 1, 0, 0, type='double3')
    cmds.setAttr (newNode + '.color2', 0, 1, 0, type='double3')
    cmds.connectAttr ('topdown_textex.outColor', renderElement + '.vray_texture_extratex')  
    '''
    # create AO
    renderElement = mel.eval ('vrayAddRenderElement ExtraTexElement;')
    renderElement = cmds.rename (renderElement,'ao')
    cmds.setAttr (renderElement + '.vray_explicit_name_extratex', 'ao', type = 'string')
    newNode = cmds.shadingNode('VRayDirt', name = 'ao_tex', asTexture=True)
    cmds.connectAttr ('topdown_textex.outColor', renderElement + '.vray_texture_extratex')
    cmds.setAttr (newNode + '.invertNormal', 1)
    cmds.setAttr (newNode + '.ignoreForGi', 0)
    cmds.setAttr (newNode + '.blackColor', -0.5 ,-0.5 ,-0.5, type='double3')
    cmds.setAttr (newNode + '.falloff', 5)
    
    