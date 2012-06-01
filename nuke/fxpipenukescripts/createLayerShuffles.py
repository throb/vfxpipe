import nuke

def createLayerShuffles(node):

    # thanks to Peter Hartwig for this code
    
    channels = node.channels()
    layers = list( set([c.split('.')[0] for c in channels]) )
    for layer in layers:
        shuffleNode = nuke.nodes.Shuffle( label=layer, inputs=[node] )
        shuffleNode['in'].setValue( layer )
        shuffleNode['postage_stamp'].setValue( True )
        removeNode = nuke.nodes.Remove(inputs = [shuffleNode])
        removeNode['operation'].setValue('keep')
        removeNode['channels'].setValue('rgb')