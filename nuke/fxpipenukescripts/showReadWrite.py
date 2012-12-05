import nuke
def showReadWrite ():
    """
    This panel gives you the number of reads that are either selected or in the entire script.
    Additionally, it tells you the path of either selected nodes or all read/write nodes.
    """
    reads = []
    readfiles = []
    writes = []
    writefiles = []
    nodes = nuke.selectedNodes('Read')
    wnodes = nuke.selectedNodes('Write')
    if len(nodes) < 1:
        nodes = nuke.allNodes('Read')
    if len(wnodes) < 1:
        wnodes = nuke.allNodes('Write')
    
    for node in nodes:
        if nuke.filename(node) not in readfiles:
            reads.append ({'file':nuke.filename(node),'start':node['first'].value(),'end':node['last'].value()})
            readfiles.append (nuke.filename(node))
    for node in wnodes:
        if nuke.filename(node) not in writefiles:
            writes.append(nuke.filename(node))
    
    read = ''
    output = ''
    writeOutput = ''
    x = 0
    for read in reads:
        x = x + 1
        output = '%s%s %d-%d\n' % (output, read['file'], int(read['start']), int(read['end']))
    if len(writes) > 0:
        for write in writes:
            writeOutput =  '%s%s\n' % (writeOutput, write)

    p = nuke.Panel('Read Paths', setWidth=650)
    
    p.addSingleLineInput('Script Name:',  nuke.root()['name'].value())
    p.addMultilineTextInput ('Read Paths:',output)
    p.addMultilineTextInput ('Write Paths:',writeOutput)
    p.addSingleLineInput ('Total Selected:', x)

    p.setWidth(1000)
    p.show()