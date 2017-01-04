OpenDatabase("localhost:/Users/cody.mckeon/Desktop/Disk/combined.00184.vtk", 0)
AddPlot("Pseudocolor", "dens", 1, 1)
SetActivePlots(0)
SetActivePlots(0)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Log  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
PseudocolorAtts.minFlag = 0
PseudocolorAtts.min = 0
PseudocolorAtts.maxFlag = 0
PseudocolorAtts.max = 1
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "hot"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 1
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 2
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeDisplayDensity = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.varyTubeRadius = 0
PseudocolorAtts.varyTubeRadiusVariable = ""
PseudocolorAtts.varyTubeRadiusFactor = 10
PseudocolorAtts.endPointType = PseudocolorAtts.None  # None, Tails, Heads, Both
PseudocolorAtts.endPointStyle = PseudocolorAtts.Spheres  # Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 1
PseudocolorAtts.endPointRadiusBBox = 0.005
PseudocolorAtts.endPointRatio = 2
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 1
SetPlotOptions(PseudocolorAtts)
DrawPlots()
AddOperator("Transform", 1)
TransformAtts = TransformAttributes()
TransformAtts.doRotate = 0
TransformAtts.rotateOrigin = (0, 0, 0)
TransformAtts.rotateAxis = (0, 0, 1)
TransformAtts.rotateAmount = 0
TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
TransformAtts.doScale = 0
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = 1
TransformAtts.doTranslate = 0
TransformAtts.translateX = 0
TransformAtts.translateY = 0
TransformAtts.translateZ = 0
TransformAtts.transformType = TransformAtts.Coordinate  # Similarity, Coordinate, Linear
TransformAtts.inputCoordSys = TransformAtts.Spherical  # Cartesian, Cylindrical, Spherical
TransformAtts.outputCoordSys = TransformAtts.Cartesian  # Cartesian, Cylindrical, Spherical
TransformAtts.m00 = 1
TransformAtts.m01 = 0
TransformAtts.m02 = 0
TransformAtts.m03 = 0
TransformAtts.m10 = 0
TransformAtts.m11 = 1
TransformAtts.m12 = 0
TransformAtts.m13 = 0
TransformAtts.m20 = 0
TransformAtts.m21 = 0
TransformAtts.m22 = 1
TransformAtts.m23 = 0
TransformAtts.m30 = 0
TransformAtts.m31 = 0
TransformAtts.m32 = 0
TransformAtts.m33 = 1
TransformAtts.invertLinearTransform = 0
TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # None, AsPoint, AsDisplacement, AsDirection
TransformAtts.transformVectors = 1
SetOperatorOptions(TransformAtts, 1)
DrawPlots()


AddOperator("Clip", 1)
ClipAtts = ClipAttributes()
ClipAtts.quality = ClipAtts.Fast  # Fast, Accurate
ClipAtts.funcType = ClipAtts.Plane  # Plane, Sphere
ClipAtts.plane1Status = 1
ClipAtts.plane2Status = 0
ClipAtts.plane3Status = 0
ClipAtts.plane1Origin = (0, 0, 0)
ClipAtts.plane2Origin = (0, 0, 0)
ClipAtts.plane3Origin = (0, 0, 0)
ClipAtts.plane1Normal = (1, 0, 0)
ClipAtts.plane2Normal = (0, 1, 0)
ClipAtts.plane3Normal = (0, 0, 1)
ClipAtts.planeInverse = 0
ClipAtts.planeToolControlledClipPlane = ClipAtts.Plane1  # None, Plane1, Plane2, Plane3
ClipAtts.center = (0, 0, 0)
ClipAtts.radius = 1
ClipAtts.sphereInverse = 0
SetOperatorOptions(ClipAtts, 1)
DrawPlots()

AddOperator("Isovolume", 1)
SetActivePlots(0)
SetActivePlots(0)
IsovolumeAtts = IsovolumeAttributes()
IsovolumeAtts.lbound = 0.001
IsovolumeAtts.ubound = 1e+37
IsovolumeAtts.variable = "default"
SetOperatorOptions(IsovolumeAtts, 1)
DrawPlots()


# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 0
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 1
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 1
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 0
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 0
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.826446
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.683013
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.564474
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.683013
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.826446
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.4641
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.900344, 0.256497, 0.351554)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.339318, -0.0920389, 0.936158)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.845662, 0.395377, 0.358516)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.340697, -0.117166, 0.932844)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.757395, 0.547595, 0.355658)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.330783, -0.147845, 0.932054)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.72457, 0.592782, 0.35158)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.328359, -0.151593, 0.932309)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.714525, 0.605786, 0.349968)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327959, -0.151834, 0.932411)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.690463, 0.634542, 0.3473)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.324288, -0.157639, 0.932731)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.681129, 0.645417, 0.345689)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.323842, -0.157877, 0.932846)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.673134, 0.653926, 0.345356)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.321429, -0.16187, 0.932996)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.673134, 0.653926, 0.345356)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.321429, -0.16187, 0.932996)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.4641
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.673134, 0.653926, 0.345356)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.321429, -0.16187, 0.932996)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.673134, 0.653926, 0.345356)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.321429, -0.16187, 0.932996)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.4641
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.673134, 0.653926, 0.345356)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.321429, -0.16187, 0.932996)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.643447, 0.667165, 0.375323)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.303335, -0.227944, 0.925219)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.639697, 0.665849, 0.38397)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.298362, -0.24527, 0.922401)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.632424, 0.660802, 0.404205)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.288111, -0.283714, 0.914603)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.627614, 0.659771, 0.413284)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.283174, -0.301032, 0.9106)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.617216, 0.66294, 0.42374)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.28417, -0.31438, 0.905766)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.600914, 0.669506, 0.436651)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.290269, -0.326208, 0.899629)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.580895, 0.673612, 0.456954)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.300504, -0.344254, 0.889487)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.56659, 0.683706, 0.459916)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.30083, -0.347989, 0.887922)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.551205, 0.6811, 0.481951)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.312209, -0.367295, 0.876139)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.826446
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.683013
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.564474
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.683013
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.826446
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.4641
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.14359
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.532273, 0.674667, 0.51138)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.327355, -0.393044, 0.859276)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.562759, 0.671514, 0.48205)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.331844, -0.350577, 0.875771)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.59118, 0.657745, 0.466773)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.335625, -0.325624, 0.883926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.622864, 0.65987, 0.420253)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.324882, -0.2705, 0.906246)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.643564, 0.650202, 0.40381)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.318265, -0.25248, 0.913762)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.673491, 0.647855, 0.35594)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.294273, -0.206736, 0.933093)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.67751, 0.647981, 0.347995)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.289341, -0.20018, 0.936061)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.697077, 0.639611, 0.324009)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.274181, -0.179759, 0.944728)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.711278, 0.629928, 0.311889)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.266208, -0.169253, 0.94894)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.715476, 0.632468, 0.29678)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.256697, -0.1571, 0.953638)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.728964, 0.630275, 0.267144)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.237815, -0.132777, 0.962192)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.73374, 0.628641, 0.25775)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.231772, -0.125019, 0.964703)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.742102, 0.625453, 0.241027)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.220894, -0.111298, 0.968927)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/homes/mckeonc/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.75309, 0.620912, 0.217542)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.206137, -0.0913201, 0.974253)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.760044, 0.616607, 0.205252)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.19819, -0.0808646, 0.976822)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.774524, 0.608737, 0.171908)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.176897, -0.0524776, 0.982829)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.77941, 0.606102, 0.158621)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.168381, -0.0412174, 0.98486)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.779749, 0.606164, 0.156706)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.167183, -0.039619, 0.98513)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.796006, 0.590808, 0.131611)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.150688, -0.0171625, 0.988432)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.803815, 0.582677, 0.119868)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.142762, -0.00666436, 0.989735)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.808707, 0.579246, 0.102311)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.131346, 0.00828556, 0.991302)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.813129, 0.575639, 0.0863818)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.120803, 0.021714, 0.992439)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.820065, 0.568674, 0.0640603)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.105645, 0.0404218, 0.993582)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.824403, 0.564101, 0.0463781)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.0936925, 0.055198, 0.99407)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.828784, 0.558944, 0.0264344)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.0801062, 0.0717596, 0.9942)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.836223, 0.548256, 0.0120688)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.0694377, 0.0840274, 0.994041)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.843428, 0.537224, -0.00439286)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.0571651, 0.097872, 0.993556)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.856064, 0.516251, -0.0252858)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.0405778, 0.115896, 0.992432)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.868166, 0.494353, -0.0436119)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.0251961, 0.131672, 0.990973)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.877563, 0.475427, -0.0620627)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.00977664, 0.14716, 0.989064)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.893344, 0.441058, -0.0860507)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.0123343, 0.167352, 0.98582)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.90013, 0.423474, -0.10216)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.0267842, 0.180271, 0.983252)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.905107, 0.408329, -0.118527)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.0412853, 0.193047, 0.980321)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.912424, 0.383303, -0.14339)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.0641842, 0.212011, 0.975157)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.916446, 0.36597, -0.161844)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.0812896, 0.225754, 0.970787)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.915903, 0.355988, -0.185457)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.100964, 0.242859, 0.964793)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.915493, 0.35057, -0.197414)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.111066, 0.251397, 0.961491)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.914388, 0.338787, -0.221626)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.131797, 0.268505, 0.954219)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.913781, 0.335217, -0.22942)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.138483, 0.27387, 0.951744)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.911364, 0.323463, -0.254535)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.160161, 0.290976, 0.943229)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.905396, 0.305253, -0.29509)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.195142, 0.318076, 0.927765)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.902361, 0.295371, -0.313848)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.211697, 0.330542, 0.919743)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.896666, 0.283718, -0.339844)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.234159, 0.347534, 0.907959)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.891585, 0.274317, -0.360314)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.251905, 0.360766, 0.897993)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.886557, 0.265197, -0.379061)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.268319, 0.372714, 0.888307)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.875794, 0.243546, -0.416737)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.301975, 0.397088, 0.866679)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.86783, 0.225046, -0.442973)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.326353, 0.414079, 0.849725)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.861026, 0.204776, -0.465512)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.348419, 0.429255, 0.833273)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.855523, 0.193867, -0.4801)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.362105, 0.438741, 0.822427)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.842955, 0.174549, -0.50888)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.388451, 0.456935, 0.800198)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.835633, 0.181238, -0.518526)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.393181, 0.461837, 0.795057)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.821758, 0.158403, -0.547378)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.431806, 0.453704, 0.779549)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.59374
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 2.14359
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.77156
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.4641
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.826446
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.683013
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.564474
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.466507
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.385543
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.318631
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810252, 0.131994, -0.571025)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.465587, 0.446817, 0.763926)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.817536, 0.167965, -0.550838)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.43851, 0.438453, 0.784518)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.862177, 0.471333, -0.185733)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (0.0661924, 0.258671, 0.963695)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.858389, 0.501815, -0.106536)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.000223972, 0.208039, 0.97812)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.834966, 0.550256, -0.00706459)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.0875529, 0.145506, 0.985476)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.820496, 0.570979, 0.0277305)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.117664, 0.121214, 0.985628)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.810495, 0.574016, 0.116634)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.187812, 0.0660624, 0.979981)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.819916, 0.528766, 0.219419)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.265146, 0.0110551, 0.964145)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.81813, 0.499128, 0.285545)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.315989, -0.0246489, 0.948443)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.824799, 0.415661, 0.383318)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.392731, -0.0665702, 0.917241)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.838995, 0.340834, 0.42417)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.426003, -0.0735564, 0.901726)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.217629
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.179859
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.217629
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.263331
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.318631
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.385543
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.466507
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.564474
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.683013
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 0.826446
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (0.898008, 0.135961, 0.418444)
View3DAtts.focus = (0, 0, -5.96046e-08)
View3DAtts.viewUp = (-0.419405, -0.0228956, 0.90751)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 4.5683
View3DAtts.nearPlane = -9.13661
View3DAtts.farPlane = 9.13661
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, -5.96046e-08)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
SetView3D(View3DAtts)
# End spontaneous state

