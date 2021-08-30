#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback, math

# start angle
st = 0
# end angle
ed = 360
# angle step
stp = 5
# wave width
wd = 1
# wave length
lg = 10
# x offset
xofs = 0
# y offset
yofs = 0

app = adsk.core.Application.get()
if app:
    ui = app.userInterface
    product = app.activeProduct
design = adsk.fusion.Design.cast(product)
rootComp = design.rootComponent

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        pathSketch = sketches.add(xyPlane)
        points = adsk.core.ObjectCollection.create()
        for i in range(st, ed + stp, stp):
            x = (i - st) / (ed - st) * lg + xofs
            y = math.sin(math.pi / 180 * i) * wd / 2 + yofs
            points.add(adsk.core.Point3D.create(x, y, 0))
        pathSketch.sketchCurves.sketchFittedSplines.add(points)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
