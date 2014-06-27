#import nuke
import os
import sys
import inspect
import fxpipe
'''
This will add all items in subdirectories to their respective named menu items.
Eg. make a folder in plugins called 'Fire' and in Nuke there will be a menu called 'Fire' with those plugins
Additionally this checks to make sure that the correct OS is supported by the plugin based on directory naming below
(win, osx, lin)
'''

for (path, dirs, files) in os.walk('%s' % (fileDir)): # walk through the dir tree for things
    categories = path.replace(fileDir,'').replace('\\','/').title() # clear out the base dir and replace all \ with / and create a list of categories
    categories = categories[1:] # this is because there is a preceeding / in the string
    for curFile in files:
	if fxpipe.os == 'win':
	    ext = '.dll'
	if fxpipe.os == 'osx':
	    ext = '.dylib'
	if fxpipe.os == 'lin':
	    ext = '.so'
	    # look for the plugins 

	if fxpipe.os in path:
	    if os.path.splitext(curFile)[1].lower() == ext and 'msvc' not in curFile: 
		nodeName = os.path.splitext(curFile)[0] #get the name of the node
	        categories = categories.replace('%s/' % (fxpipe.os),'') 
	        nuke.menu('Nodes').addCommand('%s/%s' % (categories, nodeName), 'nuke.createNode("%s")' % (nodeName) ) # add to menu!