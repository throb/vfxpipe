################################################################
#
# Breakout multichannels based on a specific set of parameters
#
# 

import nuke
import nukescripts
import fxpipe
import fxpipenukescripts

class autoComperPanel(nukescripts.PythonPanel):
    def __init__(self, node):
        channels = node.channels()
        layers = list( set([c.split('.')[0] for c in channels]) )
        layers.sort()
        layers.insert(0,'None')
        nukescripts.PythonPanel.__init__(self, 'Auto Comper')
        self.myNode = node
        self.diff = nuke.Enumeration_Knob('diffuse', 'Diffuse (lighting)', layers)
        self.gi = nuke.Enumeration_Knob('gi', 'GI', layers)
        self.spec = nuke.Enumeration_Knob('specular', 'Specular', layers)
        self.refl = nuke.Enumeration_Knob('reflect', 'Reflection', layers)
        self.refr = nuke.Enumeration_Knob('refract', 'Refraction', layers)
        self.sss = nuke.Enumeration_Knob('sss', 'SSS', layers)
        self.selfIllum = nuke.Enumeration_Knob('selfIllum', 'Self Illumination', layers)
        self.depth = nuke.Enumeration_Knob('zdepth', 'ZDepth', channels)
        self.depthNormal = nuke.Boolean_Knob('normalizeDepth','Normalize Depth?')

        for k in (self.diff, self.gi, self.spec, self.refl, self.refr, self.sss, self.selfIllum, self.depth, self.depthNormal):
            self.addKnob(k)
        if 'lighting' in layers:
            self.diff.setValue('lighting')
        if 'gi' in layers:
            self.gi.setValue('gi')
        if 'specular' in layers:
            self.spec.setValue('specular')
        if 'reflect' in layers:
            self.refl.setValue('reflect')
        if 'refract' in layers:
            self.refr.setValue('refract')
        if 'sss' in layers:
            self.sss.setValue('sss')
        if 'selfIllum' in layers:
            self.selfIllum.setValue('selfIllum')
        if 'depth.Z' in channels:
            self.depth.setValue('depth.Z')
        else:
            self.depth.setValue('None')

def shuffleLayer( node, layer ):
    shuffleNode = nuke.nodes.Shuffle( label=layer, inputs=[node] )
    shuffleNode['in'].setValue( layer )
    shuffleNode['postage_stamp'].setValue( False )
    if layer == 'None':
        shuffleNode['disable'].setValue(True)
    gradeNode = nuke.nodes.Grade( inputs=[shuffleNode] )    
    allNodes.append(shuffleNode)
    allNodes.append(gradeNode)
    return nuke.nodes.Dot( inputs=[ gradeNode ] )

def mergeLayers (nodeB, nodeA):
    mergeNode = nuke.nodes.Merge2( operation='plus', inputs=[ nodeB, nodeA ], output='rgb' )
    allNodes.append(mergeNode)
    if mergeNode.input(1).input(0).input(0)['label'].value() == 'None':
        mergeNode['disable'].setValue(True)
    return mergeNode

def autoComper(node):
    
    p = autoComperPanel(node)

    if p.showModalDialog():
        nuke.Undo().name('auto comp')
        nuke.Undo().begin()
        global allNodes
        allNodes = []
        dotParent = nuke.nodes.Dot(inputs=[node], ypos = node['ypos'].value(), xpos = node['xpos'].value()+200 )
        unPremultNode = nuke.nodes.Unpremult(inputs=[dotParent],channels='all')
        allNodes.append(unPremultNode)
        diffNode = shuffleLayer( unPremultNode, p.diff.value() )
        giNode = shuffleLayer( unPremultNode, p.gi.value() )
        specNode = shuffleLayer( unPremultNode, p.spec.value() )
        reflectNode = shuffleLayer( unPremultNode, p.refl.value() )
        refractNode = shuffleLayer( unPremultNode, p.refr.value() )
        sssNode = shuffleLayer( unPremultNode, p.sss.value() )
        selfIllumNode = shuffleLayer( unPremultNode, p.selfIllum.value() )
        depthNode = shuffleLayer( dotParent, p.depth.value() )
        
        

        mergeNode = mergeLayers(diffNode, giNode)
        mergeNode = mergeLayers(mergeNode, specNode)
        mergeNode = mergeLayers(mergeNode, reflectNode)
        mergeNode = mergeLayers(mergeNode, refractNode)
        mergeNode = mergeLayers(mergeNode, sssNode)
        mergeNode = mergeLayers(mergeNode, selfIllumNode)

        copyNode = nuke.nodes.Copy(from0='rgba.alpha',to0='rgba.alpha',inputs=[mergeNode,node])
        if p.depthNormal.value() == True:
            black, white = fxpipenukescripts.getMinMax( node, p.depth.value() )
            normNode = nuke.nodes.Grade( channels=p.depth.value(), blackpoint=black, whitepoint=white, white_clamp=True, label='normalize depth', inputs=[copyNode] )
            copyNode = nuke.nodes.Invert( channels=p.depth.value(), disable=True, inputs=[normNode])

        allNodes.append(nuke.nodes.Premult(channels='rgba',inputs=[copyNode]))
        for n in allNodes:
            n.setSelected(True)
        node.setSelected(False)    
        backdrop = nukescripts.autoBackdrop()
        backdrop['label'].setValue('Auto Comp')
        backdrop['tile_color'].setValue(2139062271)
        nuke.Undo.end()

