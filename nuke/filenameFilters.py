'''
Filename filters for Nuke
FX Pipe variables apply
'''
import nuke
import fxpipe

def fxPipeFileNameFilter(fileName):
    if nuke.env['LINUX']:
        fileName = fileName.replace(fxpipe.jobPathWin, fxpipe.jobPathLin)
        fileName = fileName.replace(fxpipe.jobPathOsx, fxpipe.jobPathLin)
    if nuke.env['MACOS']:
        fileName = fileName.replace(fxpipe.jobPathLin, fxpipe.jobPathOsx)
        fileName = fileName.replace(fxpipe.jobPathWin, fxpipe.jobPathOsx)        
    if nuke.env['WIN32']:
        fileName = fileName.replace(fxpipe.jobPathLin, fxpipe.jobPathWin)
        fileName = fileName.replace(fxpipe.jobPathOsx, fxpipe.jobPathWin)
    return fileName

nuke.addFilenameFilter(fxPipeFileNameFilter)