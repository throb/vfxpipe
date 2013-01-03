import os, optparse, logging, subprocess, re


def searchDir(pathName, ext):
    '''
    Search a specified directory
    '''
    foundFiles = []
    for root, dirs, files in os.walk(pathName):
        for curFile in files:
            if ext in os.path.splitext(curFile)[1] : foundFiles.append(os.path.normpath(os.path.join(root, curFile)))
    return foundFiles

def processFiles(fileList, ext):
    '''
    Process files in list
    '''
    ffmpegPath = 'z:/software/ffmpeg/ffmpeg'

    for curFile in fileList:
        if os.path.exists(os.path.dirname(curFile.replace(ext,'m4v'))) == False:
            os.makedirs(os.path.dirname(curFile.replace(ext,'m4v')))        
        ffOpts = ' -y -i %s -vcodec libx264 -b:v 2000k -threads 0 -an %s' % (curFile, curFile.replace(ext,'m4v'))
        subprocess.call(ffmpegPath + ffOpts)
        #print ffmpegPath + ffOpts + '\n'
    

if __name__ == "__main__":
    '''
    Using an input path and a file extension, perform a batch process on these files
    '''
    logging.basicConfig(level=logging.INFO)
    usageStr = '%s [arguments] ' % (__file__)
    parser = optparse.OptionParser(usage = usageStr)
    
    ### Add options here:
    
    parser.add_option('-i','--input',action = 'store', dest = 'inputPath', help = 'Input Path (full path)', default = None)
    parser.add_option('-e','--ext',action = 'store', dest = 'extension', help = 'Extension to search for', default = 'mov')
    parser.add_option('-d','--debug', action = 'store_true', dest = 'debug', default = 'store_false', help = 'Allows you to set Debug')
    options, args = parser.parse_args()    

    ### END OPTIONS
    
    ### Option Checking here
    
    if options.inputPath == None:
        parser.error('Please enter a path')
    if os.path.isdir(options.inputPath) == False:
        parser.error('Please enter a valid directory\n%s is not valid' % (options.inputPath))
    
    ### End option checking    
    
    fileList = searchDir(options.inputPath, options.extension)
    processFiles(fileList, options.extension)
    print 'Processed %d files' % (len(fileList))
    