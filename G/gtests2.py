# view and viewport tests for g
from RLtoolkit.g import *

# using gd (device) coordinates 
w1=Gwindow(gdViewport=(0, 20, 340, 360))
gClear(w1, 'yellow')
v11=Gview(w1)
gdSetViewport(v11, 10, 10, 110, 110)
gClear(v11, 'red')
v12=Gview(w1)
gdSetViewportR(v12, 90, 90, 100, 100)
gClear(v12, 'green')
v13=Gview(w1)
gdSetViewportR(v13, 170, 170, 100, 100)
gClear(v13, 'blue')
print "gdGetViewport w1", gdGetViewport(w1)
print "gdGetViewportR w1", gdGetViewportR(w1)
print "gGetViewport w1", gGetViewport(w1)
print "gGetViewportR w1", gGetViewportR(w1)
print "gdGetViewport v11", gdGetViewport(v11)
print "gdGetViewportR v11", gdGetViewportR(v11)
print "gGetViewport v11", gGetViewport(v11)
print "gGetViewportR v11", gGetViewportR(v11)

# using g (normalized) coordinates
w2=Gwindow(gViewport=(.25, .75, .5, .5))
gClear(w2, 'pink')
v21=Gview(w2)
gSetViewport(v21, 0, 0, .5, .5)
gClear(v21, 'purple')
v22=Gview(w2)
gSetViewport(v22, .25, .25, .75, .75)
gClear(v22, 'cyan')
v23=Gview(w2)
gSetViewportR(v23, .5, .5, .5, .5)
gClear(v23, 'magenta')
v231=Gview(v23)
gSetViewportR(v231, .25, .25, .5, .5)
gClear(v231, 'white')
print "gdGetViewport w2", gdGetViewport(w2)
print "gdGetViewportR w2", gdGetViewportR(w2)
print "gGetViewport w2", gGetViewport(w2)
print "gGetViewportR w2", gGetViewportR(w2)
print "gdGetViewport v23", gdGetViewport(v23)
print "gdGetViewportR v23", gdGetViewportR(v23)
print "gGetViewport v23", gGetViewport(v23)
print "gGetViewportR v23", gGetViewportR(v23)

# using a mixture
w3=Gwindow(gdViewportR=(30, 500, 300, 300))
gClear(w3, 'light gray')
v31=Gview(w3, 75, 75)
gClear(v31, 'dark gray')
v32=Gview(w3)
gSetViewportR(v32, .25, .5, .25, .25)
gClear(v32, 'black')
v33=Gview(w3)
gdSetViewportR(v33, 150, 150, 75, 75)
gClear(v33, 'red')
v34=Gview(w3)
gSetViewport(v34, .75, 0, 1.0, .25)
gClear(v34, 'white')

w4=Gwindow(gViewportR=(.5, 0.025, .3, .2))
gClear(w4, 'light blue')
v41=Gview(w4)
gSetViewportR(v41, .25, .25, .5, .5)
gClear(v41, 'dark green')
v411=Gview(v41)
gdSetViewportR(v411, 30, 20, 50, 30)
gClear(v411, 'orange')

gStartEventLoop()

