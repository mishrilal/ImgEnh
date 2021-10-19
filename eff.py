from os.path import join

import cv2
from exposure_enhancement import enhance_image_exposure


def analyse(img):
    imgName = img
    imdir = 'static/uploads/'
    image = cv2.imread(imdir + img)

    savePath = 'static/outputs/'

    _gamma = 0.6
    _lambda = 0.15
    _lime = False
    _sigma = 3
    _bc = 1.0
    _bs = 1.0
    _be = 1.0
    _eps = 1e-3

    # enhance image
    enhanced_image = enhance_image_exposure(image, _gamma, _lambda, _lime,
                                            _sigma, _bc, _bs, _be, _eps)

    filename = imgName.rsplit('.', 1)[0]
    fileExt = imgName.rsplit('.', 1)[1]
    imgName = filename + '-EFF.' + fileExt
    cv2.imwrite(join(savePath, imgName), enhanced_image)

    return imgName


if __name__ == "__main__":
    analyse("kodim13.png")
