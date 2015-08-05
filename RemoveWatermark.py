#coding:utf-8
import os
import os.path
import Image

outputFormat = '.png'

def hasBlackAround(x, y, distance, img):
    w, h = img.size
    startX = 0 if x - distance < 0 else x - distance
    startY = 0 if y - distance < 0 else y - distance
    endX = w - 1 if x + distance > w - 1 else x + distance
    endY = h - 1 if y + distance > h - 1 else y + distance
    hasBlackAround = False
    for j in range(startX, endX):
        for k in range(startY, endY):
            r, g, b = img.getpixel((j, k))
            if r < 130 and g < 130 and b < 130:
                return True
    return False

currentPath = os.getcwd()
fileList = os.listdir(currentPath)
for file in fileList:
    if(os.path.isdir(file)):
        targetFiles = os.listdir(file)
        outputDir = file + '/output/'
        if not os.path.isdir(outputDir):
            os.makedirs(outputDir)
        for targetFile in targetFiles:
            try:
                img = Image.open(file + '/' + targetFile)
                w, h = img.size
                rgb_im = img.convert('RGB')
                for x in range(0, w - 1):
                    for y in range(0, h - 1):
                        if not hasBlackAround(x, y, 1, rgb_im):
                            rgb_im.putpixel((x, y), (255, 255, 255))
                rgb_im.save(outputDir + targetFile[0:targetFile.rfind('.')] + outputFormat)
            except IOError:
                print targetFile + ' is not a image file'
            except  Exception as e:
                print e
print 'Done'