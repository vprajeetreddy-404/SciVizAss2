
#### import the simple module from the paraview
from paraview.simple import *
from numpy import arange, pi, sin, cos, arccos
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


n = 100
i = arange(0, n, dtype=float) + 0.5
phi = arccos(1 - 2*i/n)
goldenRatio = (1 + 5**0.5)/2
theta = 2 * pi * i / goldenRatio
x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi);

for i in range(100):

    # create a new 'Sphere'
    sphere1 = Sphere(registrationName='Sphere1')

    # Properties modified on sphere1
    sphere1.Center = [x[i], y[i], z[i]]
    sphere1.Radius = 0.1*abs(z[i])

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    sphere1Display = Show(sphere1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    sphere1Display.Representation = 'Surface'
    sphere1Display.ColorArrayName = [None, '']
    sphere1Display.SelectTCoordArray = 'None'
    sphere1Display.SelectNormalArray = 'Normals'
    sphere1Display.SelectTangentArray = 'None'
    sphere1Display.OSPRayScaleArray = 'Normals'
    sphere1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    sphere1Display.SelectOrientationVectors = 'None'
    sphere1Display.ScaleFactor = 0.020000000298023225
    sphere1Display.SelectScaleArray = 'None'
    sphere1Display.GlyphType = 'Arrow'
    sphere1Display.GlyphTableIndexArray = 'None'
    sphere1Display.GaussianRadius = 0.0010000000149011613
    sphere1Display.SetScaleArray = ['POINTS', 'Normals']
    sphere1Display.ScaleTransferFunction = 'PiecewiseFunction'
    sphere1Display.OpacityArray = ['POINTS', 'Normals']
    sphere1Display.OpacityTransferFunction = 'PiecewiseFunction'
    sphere1Display.DataAxesGrid = 'GridAxesRepresentation'
    sphere1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    sphere1Display.ScaleTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    sphere1Display.OpacityTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

    # reset view to fit data
    renderView1.ResetCamera()

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    # get layout
    layout1 = GetLayout()

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(1193, 401)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [0.0, 0.0, 0.658074870795789]
    renderView1.CameraParallelScale = 0.17032230966533082
