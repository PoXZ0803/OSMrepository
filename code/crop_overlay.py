"""该代码分为两部分，前半部分是根据经纬度对NASA开源nightlights图像的裁剪，后半部分是将node散点图与nightlight图像重合"""

import numpy as np
from osgeo import gdal
import cv2
from PIL import Image

data = gdal.Open("BlackMarble_2016_3km_geo.tif")
adfgeotransform = data.GetGeoTransform()
image = Image.open('BlackMarble_2016_3km_geo.tif')
nxsize = data.RasterXSize
nysize = data.RasterYSize

print(nxsize)
print(nysize)
print(adfgeotransform)
startx = (-125.2 + 180) / 360 * nxsize
stopx = (-66.8 + 180) / 360 * nxsize
starty = (90 - 49.6) / 180 * nysize
stopy = (90 - 24) / 180 * nysize
cropped_image = image.crop((startx, starty, stopx, stopy))
cropped_image.save('crop_nightlight_-125.2_-66.8_24.0_49.6.png')


# image1 = cv2.imread('nodeplot_0.2_s=64_red.jpg')
# image2 = cv2.imread('crop_nightlight_-125.2_-66.8_24.0_49.6.png')
#
# resized_img1 = cv2.resize(image1, (1440, 960))
# resized_img2 = cv2.resize(image2, (1440, 960))
# dst = cv2.addWeighted(resized_img2, 0.3, resized_img1, 0.7, 0)  # 此处可更改两张图片overlay时的权重，以达到不同的效果
#
# cv2.imwrite('node_nightlight_overlay_red.png', dst)
