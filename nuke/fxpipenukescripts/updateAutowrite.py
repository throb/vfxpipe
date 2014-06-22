#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: robn
# @Date:   2014-06-16 11:58:57
# @Last Modified by:   robn
# @Last Modified time: 2014-06-17 16:16:47
#
# update the autowrite nodes based on parameters inside the node when the script updates

import nuke
import re
import fxpipe

def updateAutowrite():
    for curNode in nuke.allNodes('Write'):
        tempPath = nuke.root()['name'].value()
        if 'shot' in tempPath:
            if 'AutoWrite' in curNode['name'].value():
                #width = curNode.width()
                #height = curNode.height()
                format = curNode.format().name().lower()
                colorspace = curNode['colorspace'].value()
                colorspace = colorspace.replace ('default (','')
                colorspace = colorspace.replace (')','').lower()
                fileType = curNode['file_type'].value()
                ###################
                ## deal with the longer file types
                if fileType == 'jpeg': fileType = 'jpg'
                elif fileType == 'tiff': fileType = 'tif'
                elif fileType == 'targa': fileType = 'tga'
                outputPath = tempPath.split('/')
                outputFile = outputPath[-1].split('.')[0]
                outputVersion = re.search('v[0-9]+',outputFile).group(0)
                outputShot = outputPath[7].lower()
                outputRez = outputPath[-2]
                newPath = '/'.join(outputPath[0:8])
                outputFormat = '%s_%s' % (format, colorspace)
                outputType = curNode['outputType'].value().lower()
                descriptor = curNode['descriptor'].value()
                if descriptor != '':
                    descriptor = '_%s' % (descriptor)
                aov = curNode['aov'].value()
                if aov != '':
                    aov = '_%s' % (aov)
                outputName = '%s%s_%s%s_%s' % (outputShot, aov, outputType, descriptor, outputVersion)                

                newPath = '%s/img/output/2D/%s/%s_%s/%s_%s.####.%s' % (newPath, outputName,outputFormat, fileType, outputName, outputFormat, fileType)
                curNode['file'].setValue(newPath.replace(' ','_'))
            #else: 
            #    curNode['label'].setValue('Please save your script in the proper location')
            #    curNode['file'].setValue('')           