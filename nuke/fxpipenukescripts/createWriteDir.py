def createWriteDir():
    '''
    This function creates a write directory automatically so the user does not have to do it.
    Supports stereo notation with %v and %V
    '''
    import nuke, os
    curnode = nuke.thisNode()
    originalFileName = nuke.filename(curnode)
    allViews = curnode.knob('views').value() # look for views in the write node
    allViews = allViews.split() # split them out
    outputFilename = []
    for view in allViews:
        fileName = originalFileName
        # check for the standard nuke view parameters
        if '%v' in fileName :
            outputFilename.append(fileName.replace('%v',view[:1]))
        if '%V' in fileName :
            outputFilename.append(fileName.replace('%V',view))
        print outputFilename
        if len(outputFilename) < 1:
            outputFilename.append(originalFileName)
        for fileName in outputFilename:
            if fileName != '':
                dir = os.path.dirname( fileName )
                osdir = nuke.callbacks.filenameFilter( dir )
                if not os.path.exists( osdir ):
                    os.makedirs( osdir )
                    print 'Created : %s' % (osdir)