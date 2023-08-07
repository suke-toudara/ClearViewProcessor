import os
import time
import cv2 
import numpy as np
from skimage import img_as_float64


class ClearViewProcessor():
    def __init__(self):
        self.sigmas = [15, 80, 250]
        self.alpha = 125.0
        self.beta = 46.0
        self.G = 5.0
        self.OFFSET = 25.0

    def msrcr(self,img):
        """
        MSRCR (Multi-scale retinex with color restoration)

        Parameters :

        img : input image
        sigmas : list of all standard deviations in the X and Y directions, for Gaussian filter
        alpha : controls the strength of the nonlinearity
        beta : gain constant
        G : final gain
        b : offset
        """
        img = img_as_float64(img)+1
        img_msr = self.multiScale(img)    
        img_color = self.crf(img)    
        img_msrcr = self.G * (img_msr*img_color + self.OFFSET)
        img_msrcr = (img_msrcr - np.min(img_msrcr, axis=(0, 1))) / (np.max(img_msrcr, axis=(0, 1)) - np.min(img_msrcr, axis=(0, 1))) * 255 #normalization　and change range to 0~255
        img_msrcr = np.uint8(np.minimum(np.maximum(img_msrcr, 0), 255)) #Processing to keep within 0<RGB<255
        return img_msrcr

    def singleScale(self,img,sigma):
        """
        Single-scale Retinex
        
        Parameters :

        img : input image
        sigma : the standard deviation in the X and Y directions, for Gaussian filter
        """
        #ssr = np.log10(img) - np.log10(cv2.GaussianBlur(img,(0,0),sigma))
        ssr = np.log10(img) - np.log10(cv2.blur(img, (sigma, sigma))) #高速化用
        return ssr

    def multiScale(self,img):
        """
        Multi-scale Retinex
        
        Parameters :

        img : input image
        sigma : list of all standard deviations in the X and Y directions, for Gaussian filter
        """
        retinex = np.zeros_like(img)
        for s in self.sigmas:
            retinex += self.singleScale(img,s)
        msr = retinex/len(self.sigmas)
        return msr

    def crf(self,img):
        """
        CRF (Color restoration function)

        Parameters :

        img : input image
        alpha : controls the strength of the nonlinearity
        beta : gain constant
        """
        img_sum = np.sum(img,axis=2,keepdims=True)

        color_rest = self.beta * (np.log10(self.alpha*img) - np.log10(img_sum))
        return color_rest

    def adjust_white_balance(self,image: np.ndarray) :
        # white balance adjustment for strong neutral white
        image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        avg_a = np.average(image[:, :, 1])
        avg_b = np.average(image[:, :, 2])
        image[:, :, 1] = image[:, :, 1] - (
            (avg_a - 128) * (image[:, :, 0] / 255.0) * 1.1
        )
        image[:, :, 2] = image[:, :, 2] - (
            (avg_b - 128) * (image[:, :, 0] / 255.0) * 1.1
        )
        image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)
        return image

def main():
  pass
if __name__ == '__main__':
    main()

