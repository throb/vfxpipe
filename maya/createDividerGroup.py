def createDividerGroup():
    import maya.cmds as cmds
    grp = cmds.CreateEmptyGroup()
    cmds.rename(grp,'____________________________________________')