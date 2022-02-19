# I have used the filter "Warp by Scalar" and set the scale factor to 1.5
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Image Data Reader'
a2dvti = XMLImageDataReader(registrationName='2d.vti', FileName=['/home/u1365431/Downloads/SciViz2/data02/2d.vti'])
a2dvti.PointArrayStatus = ['Scalars_']

# Properties modified on a2dvti
a2dvti.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
a2dvtiDisplay = Show(a2dvti, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'Scalars_'
scalars_LUT = GetColorTransferFunction('Scalars_')

# get opacity transfer function/opacity map for 'Scalars_'
scalars_PWF = GetOpacityTransferFunction('Scalars_')

# trace defaults for the display properties.
a2dvtiDisplay.Representation = 'Slice'
a2dvtiDisplay.ColorArrayName = ['POINTS', 'Scalars_']
a2dvtiDisplay.LookupTable = scalars_LUT
a2dvtiDisplay.SelectTCoordArray = 'None'
a2dvtiDisplay.SelectNormalArray = 'None'
a2dvtiDisplay.SelectTangentArray = 'None'
a2dvtiDisplay.OSPRayScaleArray = 'Scalars_'
a2dvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a2dvtiDisplay.SelectOrientationVectors = 'None'
a2dvtiDisplay.ScaleFactor = 409.6
a2dvtiDisplay.SelectScaleArray = 'Scalars_'
a2dvtiDisplay.GlyphType = 'Arrow'
a2dvtiDisplay.GlyphTableIndexArray = 'Scalars_'
a2dvtiDisplay.GaussianRadius = 20.48
a2dvtiDisplay.SetScaleArray = ['POINTS', 'Scalars_']
a2dvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a2dvtiDisplay.OpacityArray = ['POINTS', 'Scalars_']
a2dvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a2dvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
a2dvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
a2dvtiDisplay.ScalarOpacityUnitDistance = 22.538152910782724
a2dvtiDisplay.ScalarOpacityFunction = scalars_PWF
a2dvtiDisplay.OpacityArrayName = ['POINTS', 'Scalars_']
a2dvtiDisplay.IsosurfaceValues = [100.0]
a2dvtiDisplay.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
a2dvtiDisplay.ScaleTransferFunction.Points = [13.0, 0.0, 0.5, 0.0, 187.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
a2dvtiDisplay.OpacityTransferFunction.Points = [13.0, 0.0, 0.5, 0.0, 187.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
a2dvtiDisplay.SliceFunction.Origin = [2048.0, 1024.0, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2048.0, 1024.0, 10000.0]
renderView1.CameraFocalPoint = [2048.0, 1024.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
a2dvtiDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(registrationName='WarpByScalar1', Input=a2dvti)
warpByScalar1.Scalars = ['POINTS', 'Scalars_']

# Properties modified on warpByScalar1
warpByScalar1.ScaleFactor = 1.5

# show data in view
warpByScalar1Display = Show(warpByScalar1, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
warpByScalar1Display.Representation = 'Surface'
warpByScalar1Display.ColorArrayName = ['POINTS', 'Scalars_']
warpByScalar1Display.LookupTable = scalars_LUT
warpByScalar1Display.SelectTCoordArray = 'None'
warpByScalar1Display.SelectNormalArray = 'None'
warpByScalar1Display.SelectTangentArray = 'None'
warpByScalar1Display.OSPRayScaleArray = 'Scalars_'
warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByScalar1Display.SelectOrientationVectors = 'None'
warpByScalar1Display.ScaleFactor = 409.6
warpByScalar1Display.SelectScaleArray = 'Scalars_'
warpByScalar1Display.GlyphType = 'Arrow'
warpByScalar1Display.GlyphTableIndexArray = 'Scalars_'
warpByScalar1Display.GaussianRadius = 20.48
warpByScalar1Display.SetScaleArray = ['POINTS', 'Scalars_']
warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.OpacityArray = ['POINTS', 'Scalars_']
warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
warpByScalar1Display.ScalarOpacityFunction = scalars_PWF
warpByScalar1Display.ScalarOpacityUnitDistance = 22.574728150762517

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByScalar1Display.ScaleTransferFunction.Points = [13.0, 0.0, 0.5, 0.0, 187.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByScalar1Display.OpacityTransferFunction.Points = [13.0, 0.0, 0.5, 0.0, 187.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(a2dvti, renderView1)

# show color bar/color legend
warpByScalar1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#change interaction mode for render view
renderView1.InteractionMode = '3D'

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
renderView1.CameraPosition = [-14.48745901107524, -5782.566057668492, 7034.2803892870215]
renderView1.CameraFocalPoint = [2107.958198619794, -798.0800180079921, 1901.4977598998041]
renderView1.CameraViewUp = [0.05206129084842455, 0.7278113864631538, 0.6837983677443064]
renderView1.CameraViewAngle = 12.045264040234702
renderView1.CameraParallelScale = 2289.7336089597848

