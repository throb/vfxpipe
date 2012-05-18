import nuke

def postageStampControl(value=0):
    for node in nuke.allNodes('Read'):
        node['postage_stamp'].setValue(value)