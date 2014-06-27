'''
Filename filters for Nuke
FX Pipe variables apply
'''
import nuke
import fxpipe

def fxPipeFileNameFilter(fileName):
    swapped = False
    if nuke.env['LINUX']:
        fileName, swapped = pathSwap(fileName, fxpipe.jobPathWin, fxpipe.jobPathLin)
        if swapped == False:
            fileName = pathSwap(fileName, fxpipe.jobPathOsx, fxpipe.jobPathLin)
    if nuke.env['MACOS']:
        fileName, swapped = pathSwap(fileName, fxpipe.jobPathLin, fxpipe.jobPathOsx)
        if swapped == False:
            fileName, swapped = pathSwap(fileName, fxpipe.jobPathWin, fxpipe.jobPathOsx)        
    if nuke.env['WIN32']:
        fileName, swapped = pathSwap(fileName, fxpipe.jobPathLin, fxpipe.jobPathWin)
        if swapped == False:
            fileName, swapped = pathSwap(fileName, fxpipe.jobPathOsx, fxpipe.jobPathWin)
    return fileName

def pathSwap(inFile, pathA, pathB):
    swapped = False
    for pathCount in range(min(len(pathA),len(pathB))):
        if swapped == False:
            fileName = inFile.replace(pathA[pathCount],pathB[pathCount])
            if fileName != inFile:
                swapped = True
                continue
        print pathCount, pathA[pathCount], pathB[pathCount], swapped
    return fileName, swapped

nuke.addFilenameFilter(fxPipeFileNameFilter)
