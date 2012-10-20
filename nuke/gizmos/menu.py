import nuke
import os
import inspect
'''
This will add all items in subdirectories to their respective named menu items.
Eg. make a folder in gizmos called 'Fire' and in Nuke there will be a menu called 'Fire' with your gizmos in it
'''
curInitFile = inspect.getfile(inspect.currentframe()) # get location of current py file
fileDir = os.path.dirname(curInitFile) # get the dir name of that file

          
for (path, dirs, files) in os.walk('%s' % (fileDir)): # walk through the dir tree for things
    categories = path.replace(fileDir,'').replace('\\','/').title() # clear out the base dir and replace all \ with / and create a list of categories
    categories = categories[1:] # this is because there is a preceeding / in the string
    for curFile in files:
        if os.path.splitext(curFile)[1].lower() == '.gizmo': #look for gizmos
            nodeName = os.path.splitext(curFile)[0] #get the name of the node
            nuke.menu('Nodes').addCommand('%s/%s' % (categories, nodeName), 'nuke.createNode("%s")' % (nodeName) ) # add to menu!