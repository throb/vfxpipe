import fxpipe
import shotgunUtils
import xlwt # this is required to write the actual excel doc
import datetime
import os, sys



def getPlaylist (projectName, playlistName):
    sg = shotgunUtils.genericUtils()
    project = sg.project(projectName)
    if project == '':
        raise Exception ('Project name %s not found.' % (projectName))
    playlist = sg.playlistFind(project, playlistName)
    if playlist == '':
            raise Exception ('Playlist %s not found.' % (playlistName))
    retValue = {'project' : project, 'playlist': playlist}
    return playlist

def createHeader(headerData, sheet):
    row = 0
    column = 0    
    for headerItem in headerData:
        sheet.write(row, column, headerItem, xlwt.easyxf('font: bold 1; font: color white; pattern: pattern solid, back_color black;'))
        #sheet.col(col).width = 30
        sheet.col(column).width = 256 * (len(headerItem) + 10)
        #curCol = sheet.col(column)
        #curCol.width = 1024* len(headerItem) + 10
        column += 1
    
def getVersions(playlist):
    sg = shotgunUtils.genericUtils()
    versionPaths = []    
    for item in playlist['versions']:
        versionData = sg.versionFind(item['id'])
        versionPaths.append({'file' : versionData['sg_path_to_frames'], 'range' : versionData['sg_last_frame'] - versionData['sg_first_frame'] + 1})
    return versionPaths

def getOutputDirsFromVersions(versionData):
    outputDirs = []
    for item in versionData:
        outputDirs.append(os.path.split(item['file'])[0])
    return outputDirs
    
def getFileNamesFromVersions(versionData):
    clientNames = []
    for item in versionData:
        clientNames.append (os.path.basename(item['file']).split('.')[0])
    return clientNames

def getShotNamesFromVersions(versionData):
    shotNames = []
    for item in versionData:
        shotNames.append(os.path.basename(item['file']).split('.')[0].split('_')[0] + '_' + os.path.basename(item['file']).split('.')[0].split('_')[1])
    return shotNames

def versionPrep(versionData):
    excelVersions = []
    for item in versionData:
        shotName = os.path.basename(item['file']).split('.')[0].split('_')[0] + '_' + os.path.basename(item['file']).split('.')[0].split('_')[1]
        shotName = shotName.upper()
        fileName = os.path.basename(item['file']).split('.')[0]
        fileName = fileName.upper()
        frameRange = item['range']
        excelVersions.append({'shot' : shotName, 'filename' : fileName, 'length' : item['range']})
    return excelVersions


def createExcelFromPlaylist (projectName, playlistName):

    #playlistName = 'AE Client Review - 20121025'
    #projectName = 'after_earth'

    todayDate = datetime.date.today()
    humanDate = ('%02d/%02d/%04d' % (todayDate.month, todayDate.day, todayDate.year))
    compactDate = ('%04d%02d%02d' % (todayDate.year, todayDate.month, todayDate.day))
    
    vendorName = 'Svengali'
    
    wbk = xlwt.Workbook(encoding='utf-8')
    sheet = wbk.add_sheet('VENDOR', cell_overwrite_ok=True)
    
    # create the header here
    headerData = ['VENDOR','DATE','SHOT NUM','LENGTH','FILENAME','FILE TYPE','FORMAT','RES','FOR','VIA','VENDOR NOTES']
    createHeader(headerData, sheet)
    
    # get the data we need
    playlist = getPlaylist(projectName, playlistName)
    versions = getVersions(playlist)
    dirList = getOutputDirsFromVersions(versions)
    fileList = getFileNamesFromVersions(versions)
    clientVersions = versionPrep(versions)
    
    row = 2
    fileTypes = 'exr','dpx','avid_mov','photo jpg_mov'
    for version in clientVersions:
        for fileType in fileTypes:
            sheet.write(row,0,vendorName)
            sheet.write(row,1,humanDate)
            sheet.write(row,2,version['shot'])
            sheet.write(row,3,version['length'])
            if 'photo' not in fileType:
                sheet.write(row,4,version['filename'])
            else:
                sheet.write(row,4,version['filename'] + '_CC')
            if 'mov' not in fileType:
                sheet.write(row,5,'image')
                sheet.write(row,6,fileType.lower())
                sheet.write(row,7,'2048x1080')
            else:
                movType = fileType.split('_')[0].upper()
                sheet.write(row,5,movType)
                sheet.write(row,6,'mov')
                if 'avid' in fileType:
                    sheet.write(row,7,'1920x1080')
                else:
                    sheet.write(row,7,'1280x720')
            sheet.write(row,8,'')
            sheet.write(row,9,'FTP')
            row += 1
            
            
            
                    
    excelFile = 'z:/job/after_earth/prod/io/client/client_out/%s/FROM_%s/%s/%s_submission_report_%s.xls' % (compactDate, vendorName, compactDate, vendorName, compactDate)
    if not os.path.exists(os.path.dirname(excelFile)) :
        os.makedirs(os.path.dirname(excelFile))
    wbk.save(excelFile)
    
def processVersions(projectName, playlistName):
    playlist = getPlaylist(projectName, playlistName)
    versions = getVersions(playlist)
    dirList = getOutputDirsFromVersions(versions)
    versionDir = getOutputDirsFromVersions(versions)
    for curDir in versionDir:
        execCmd = '"c:\\Program Files\\Nuke6.3v8\\Nuke6.3.exe" -t z:\\job\\after_earth\\common\\nuke\\python\\autoQuicktime.py %s' %  (curDir)
        print execCmd
        stdout = os.popen(execCmd)
        stdoutParse = stdout.read()
        jobID = stdoutParse.split('=')[len(stdoutParse.split('='))-1]
        jobID = jobID.strip()
        print jobID
    
if __name__ == '__main__':
    project = sys.argv[1]
    playlist = sys.argv[2]
    
    try :
        if len(sys.argv[3]) > 0:
            createOutput = True
    except:
        createOutput = False
    
    
    createExcelFromPlaylist(project, playlist)
    
    
    if createOutput == True:
        processVersions(project, playlist)
    
        