

from paraview.simple import *

paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Image Data Reader'
a2dvti = XMLImageDataReader(registrationName='2d.vti', FileName=['/home/u1365431/Downloads/SciViz2/data02/2d.vti'])
a2dvti.PointArrayStatus = ['Scalars_']


a2dvti.TimeArray = 'None'


renderView1 = GetActiveViewOrCreate('RenderView')


a2dvtiDisplay = Show(a2dvti, renderView1, 'UniformGridRepresentation')


scalars_LUT = GetColorTransferFunction('Scalars_')

scalars_PWF = GetOpacityTransferFunction('Scalars_')

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


a2dvtiDisplay.ScaleTransferFunction.Points = [13.0, 0.0, 0.5, 0.0, 187.0, 1.0, 0.5, 0.0]


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

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=a2dvti,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine1.Source.Point2 = [4096.0, 2048.0, 0.0]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'Scalars_']
plotOverLine1Display.LookupTable = scalars_LUT
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.OSPRayScaleArray = 'Scalars_'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'None'
plotOverLine1Display.ScaleFactor = 409.6
plotOverLine1Display.SelectScaleArray = 'Scalars_'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'Scalars_'
plotOverLine1Display.GaussianRadius = 20.48
plotOverLine1Display.SetScaleArray = ['POINTS', 'Scalars_']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'Scalars_']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [29.0, 0.0, 0.5, 0.0, 150.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [29.0, 0.0, 0.5, 0.0, 150.0, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Scalars_']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Scalars_', 'Scalars_', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Scalars_', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Z', '1', '0.5000076295109483', '0', 'Points_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Scalars_', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Scalars_', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Scalars_', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Scalars_', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'Scalars_', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Scalars_', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Scalars_', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Scalars_', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Scalars_', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Scalars_', '4', 'arc_length', '4', 'vtkValidPointMask', '4']



# layout/tab size in pixels
layout1.SetSize(788, 427)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2048.0, 1024.0, 10000.0]
renderView1.CameraFocalPoint = [2048.0, 1024.0, 0.0]
renderView1.CameraParallelScale = 2289.7336089597848

