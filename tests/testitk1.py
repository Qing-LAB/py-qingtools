import os
import numpy
import SimpleITK
import matplotlib.pyplot as plt


def sitk_show(img, title='untitled', margin=0.05, dpi=40):
    nda = SimpleITK.GetArrayFromImage(img)
    spacing = img.GetSpacing()
    figsize = (1 + margin) * nda.shape[0] / dpi, (1 + margin) * nda.shape[1] / dpi
    extent = (0, nda.shape[1] * spacing[1], nda.shape[0] * spacing[0], 0)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([margin, margin, 1 - 2 * margin, 1 - 2 * margin])
    plt.set_cmap("gray")
    ax.imshow(nda, extent=extent, interpolation=None)
    if title:
        plt.title(title)



reader = SimpleITK.ImageFileReader()
reader.SetFileName('../resources/02.tif')
imgOriginal = reader.Execute()
#sitk_show(imgOriginal)

imgSmooth=SimpleITK.CurvatureFlow(image1=imgOriginal,
                                  timeStep=0.125,
                                  numberOfIterations=5)
sitk_show(imgSmooth)
plt.show()

lstSeeds=[(150,75)]
labelWhiteMatter=255

imgbackground=SimpleITK.ConnectedThreshold(image1=imgSmooth,
                                           seedList=lstSeeds,
                                           lower=70,
                                           upper=90,
                                           replaceValue=labelWhiteMatter)
imgSmoothInt=SimpleITK.Cast(SimpleITK.RescaleIntensity(imgSmooth), imgbackground.GetPixelID())
sitk_show(SimpleITK.LabelOverlay(imgSmoothInt, imgbackground))
plt.show()