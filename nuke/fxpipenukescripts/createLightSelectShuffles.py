import nuke

def createLightSelectShuffles(node):

    # thanks to Peter Hartwig for some sample code that got my brain going
    
    channels = node.channels()
    
    layers = list( set([c.split('.')[0] for c in channels]) )
    lsLayers = []
    for layer in layers:
        if 'ls_' in layer:
            lsLayers.append(layer)
            lsLayers.sort()
    
    for lightSelect in lsLayers:
        shuffleNode = nuke.nodes.Shuffle( label=lightSelect.split('ls_')[1], inputs=[node] )
        shuffleNode['in'].setValue( lightSelect )
        shuffleNode['postage_stamp'].setValue( True )
        removeNode = nuke.nodes.Remove(inputs = [shuffleNode])
        removeNode['operation'].setValue('keep')
        removeNode['channels'].setValue('rgb')
        