import FreeCAD

panel = FreeCAD.activeDocument().addObject("Part::Box", "panelXZ")


selected = FreeCADGui.Selection.getSelection()
selectedLen = len(selected)

if selectedLen == 1:

	obj = FreeCADGui.Selection.getSelection()[0]
	sizes = [ obj.Length.Value, obj.Width.Value, obj.Height.Value ]
	sizes.sort()

	panel.Length = sizes[2]
	panel.Width = sizes[0]
	panel.Height = sizes[1]
	
else: 

	panel.Length = 600
	panel.Width = 18
	panel.Height = 300

FreeCAD.activeDocument().recompute()