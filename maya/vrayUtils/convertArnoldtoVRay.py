'''
Convert Arnold Shader to VRay shader
'''
from pymel.core import *
 
        
selected = ls(materials=True, sl=True)

for g in selected:
    
    
    '''check for arnold mat'''
    
    if(nodeType(g) == "aiStandard"):
        sg = g.listConnections(type='shadingEngine')[0]
        mesh = sg.listConnections(type='mesh')
        n = shadingNode('VRayMtl', asShader=True, name='vr_'+g)
        
        #Make array with all the attributes that need to be compared, Arnold material attribute first, VRay material attribute second
        
    
        attrList = \
        [('color','color'),\
        ('Kd','diffuseColorAmount'),\
        ('diffuseRoughness','roughnessAmount'),\
        ('Ks','reflectionColorAmount'),\
        ('KsColor','reflectionColor'),\
        ('specularRoughness','reflectionGlossiness'),\
        ('specularAnisotropy','anisotropy'),\
        ('specularRotation','anisotropyRotation'),\
        ('reflectionExitColor','reflectionExitColor'),\
        ('Kt' ,'refractionColorAmount'),\
        ('IOR','refractionIOR'),\
        ('refractionRoughness','refractionGlossiness'),\
        ('KtColor','refractionColor'),\
        ('Fresnel','useFresnel')]



        #Connect maps if available, otherwise adjust values/colours

        for a in attrList:
            if connectionInfo(g + "." + a[0], id=True):
                outAttr = listConnections(g + "." + a[0], p=True)[0]
                inAttr = (n + "." + a[1])
                connectAttr(outAttr, inAttr)
            else:
                outAttr = getAttr(g + "." + a[0])
                inAttr = (n + "." + a[1])
                setAttr(inAttr, outAttr)
            roughnessCheck = ['specularRoughness','refractionRoughness']
            
            if a[0] in roughnessCheck:
                newVal =  1-int(cmds.getAttr(inAttr)*1000)/1000.0
                cmds.setAttr (inAttr, newVal)  

        
        
        #If there is a bump map, connect it and adjust the multiplier
        listAttr(g)    
        if connectionInfo(g + ".normalCamera", id=True):
            outAttr = listConnections(g + ".normalCamera")[0]
            outValue = listConnections(outAttr + ".bumpValue", p=True)[0]
            inValue = (n + "." + 'bumpMap')
            connectAttr(outValue, inValue+"R")
            connectAttr(outValue, inValue+"G")
            connectAttr(outValue, inValue+"B")
            outDepth = getAttr(outAttr + ".bumpDepth")
            inDepth = (n + "." + 'bumpMult')
            setAttr(inDepth, outDepth)
        
        vraySG = sets(renderable=True, noSurfaceShader=True, empty=True, name='vr_'+g+'_SG')
        # connect the mat and SG
        connectAttr(n+'.outColor', vraySG+'.surfaceShader', force=True)
        sets(vraySG, forceElement=mesh)