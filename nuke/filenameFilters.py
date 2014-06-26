'''
Filename filters for Nuke
FX Pipe variables apply
'''
import nuke
import fxpipe

def fxPipeFileNameFilter(fileName):
    if nuke.env['LINUX']:
        fileName = pathSwap(fileName, fxpipe.jobPathWin, fxpipe.jobPathLin)
        fileName = pathSwap(fileName, fxpipe.jobPathOsx, fxpipe.jobPathLin)
    if nuke.env['MACOS']:
        fileName = pathSwap(fileName, fxpipe.jobPathLin, fxpipe.jobPathOsx)
        fileName = pathSwap(fileName, fxpipe.jobPathWin, fxpipe.jobPathOsx)        
    if nuke.env['WIN32']:
        fileName = pathSwap(fileName, fxpipe.jobPathLin, fxpipe.jobPathWin)
        fileName = pathSwap(fileName, fxpipe.jobPathOsx, fxpipe.jobPathWin)
    return fileName

def pathSwap(inFile, pathA, pathB):
    for pathCount in range(min(len(pathA),len(pathB))):
        fileName = inFile.replace(pathA[pathCount],pathB[pathCount])
    return fileName

nuke.addFilenameFilter(fxPipeFileNameFilter)
