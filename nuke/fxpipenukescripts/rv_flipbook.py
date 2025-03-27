# Copyright (c) 2010 The Foundry Visionmongers Ltd.  All Rights Reserved.
import platform
import sys
import os.path
import re
import threading
import nuke
import subprocess
import nukescripts
import nukescripts.flipbooking as flipbooking

class RVFlipbook(flipbooking.FlipbookApplication):
    """RV Flipbook integration for Nuke on Windows."""
    def __init__(self):
        # Path to RV executable
        self._rvPath = r"C:\Program Files\ShotGrid\RV-2023.0.1\bin\rv.exe"

    def name(self):
        return "RV"

    def path(self):
        return self._rvPath

    def cacheDir(self):
        return os.environ["NUKE_TEMP_DIR"]

    def run(self, filename, frameRanges, views, options):
        # Handle frame ranges
        sequence_interval = f"{frameRanges.minFrame()}-{frameRanges.maxFrame()}"
        for frame in range(frameRanges.minFrame(), frameRanges.maxFrame()+1):
            if frame not in frameRanges.toFrameList():
                print("This example only supports complete frame ranges")
                return

        filename = os.path.normpath(filename)

        # Build command arguments
        args = [self.path()]
        
        # Handle ROI (Region of Interest)
        roi = options.get("roi", None)
        if roi is not None and not (roi["x"] == 0.0 and roi["y"] == 0.0 and roi["w"] == 0.0 and roi["h"] == 0.0):
            args.extend(["-c", str(int(roi["x"])), str(int(roi["y"])), str(int(roi["w"])), str(int(roi["h"]))])

        # Handle LUT options
        lut = options.get("lut", "")
        if lut == "linear-sRGB":
            args.append("-sRGB")
        elif lut == "linear-rec709":
            args.append('-rec709')

        # Add filename and frame range
        args.append(filename)
        args.append(sequence_interval)

        # Launch RV as a separate process
        subprocess.Popen(args, shell=False)

    def capabilities(self):
        return {
            'proxyScale': False,
            'crop': True,
            'canPreLaunch': False,
            'supportsArbitraryChannels': True,
            'maximumViews': 2,
            'fileTypes': [
                "j2k", "jpt", "jp2", "dpx", "cin", "cineon", "jpeg", "jpg", 
                "rla", "rpf", "yuv", "exr", "openexr", "sxr", "tif", "tiff", 
                "sm", "tex", "tx", "tdl", "shd", "targa", "tga", "tpic", 
                "rgbe", "hdr", "iff", "png", "z", "zfile", "sgi", "bw", 
                "rgb", "rgba", "*mraysubfile*", "movieproc", "stdinfb", 
                "aiff", "aif", "aifc", "wav", "snd", "au", "mov", "avi", 
                "mp4", "m4v", "dv"
            ]
        }

# Register RV as a flipbook option
flipbooking.register(RVFlipbook()) 