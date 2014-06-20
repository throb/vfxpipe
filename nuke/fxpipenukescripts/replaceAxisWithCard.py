import nuke

########################################
# replace all axis nodes with cards
# keep all animation data

def replaceAxisWithCard():
    allCards = []
    for curNode in nuke.allNodes('Axis2'):
        card = nuke.nodes.Card()
        allCards.append(card)
        #copy the animation here
        card['translate'].fromScript(curNode['translate'].toScript())
        card['rotate'].fromScript(curNode['rotate'].toScript())
        card['scaling'].fromScript(curNode['scaling'].toScript())
        card['uniform_scale'].fromScript(curNode['uniform_scale'].toScript())
        card['skew'].fromScript(curNode['skew'].toScript())
        card['pivot'].fromScript(curNode['pivot'].toScript())
        card['xpos'].setValue(curNode['xpos'].value()-110)
        card['ypos'].setValue(curNode['ypos'].value())
        card['label'].setValue(curNode['name'].value())
        curNode['disable'].setValue(True) 
            



