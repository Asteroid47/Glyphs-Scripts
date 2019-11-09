#MenuTitle: Select all guides
# -*- coding: utf-8 -*-
__doc__="""
Selects all guides, local and global, on active glyph.
"""


font = Glyphs.font
layer = font.selectedLayers[0]

layerMasterId = layer.master.id

layer.clearSelection()
for guide in layer.guides:
	layer.selection.append(guide)

for guide in layer.master.guides:
	layer.selection.append(guide)