import nuke

'''
Set up the generic formats for most things
'''

formats = [
    '1920 1080 1.0 hd',
    '960 540 1.0 hhd',
    '2048 1556 1.0 2kfa',
    '2048 1556 2.0 2kana',
    '1828 1556 2.0 ana',
    '720 486 1.21 d1',
    '720 405 1 hdvid'
    ]

for curFormat in formats:
    nuke.addFormat (curFormat)