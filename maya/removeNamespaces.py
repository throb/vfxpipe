import maya.cmds as cmds
import maya.utils as utils


def removeNamespaces():
    ''' removes namespaces from the file and merges with root.
    Requires Maya 2013 to work since the new python option to mergeNamespaceWithRoot is not supported in 2012
    '''
    
    allNodes = cmds.ls () # get everything!
    allNamespaces = []
    
    for node in allNodes:
        if ':' in node: # check out for namespaces
            if node.split(':')[0] not in allNamespaces:
                allNamespaces.append(node.split(':')[0]) #only keep the name space name onces
            
    for curNamespace in allNamespaces: # look through the namespaces
        cmds.namespace( removeNamespace=curNamespace, mergeNamespaceWithRoot=True) # remove the namespace and merge with root because the namespace won't be empty generally