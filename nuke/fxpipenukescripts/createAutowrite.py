#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: robn
# @Date:   2014-06-16 11:58:57
# @Last Modified by:   robn
# @Last Modified time: 2014-06-17 15:56:04
#
# create autowrite node with knobs needed

import nuke

def createAutowrite():
	w = nuke.createNode('Write', inpanel=False)
	count = 1
	while nuke.exists('AutoWrite' + str(count)):
	    count += 1
	w.knob('name').setValue('AutoWrite' + str(count))
	w.knob('tile_color').setValue(8388607)
	t = nuke.Tab_Knob("Additional Parameters")
	w.addKnob(t)
	w.addKnob(nuke.Enumeration_Knob('outputType', 'Output Type', ['Comp', 'Precomp','LTComp','Matte']))
	w.addKnob(nuke.EvalString_Knob('descriptor','Descriptor',''))
	w.addKnob(nuke.EvalString_Knob('aov','AOV',''))
	w['file_type'].setValue('exr')

