import cv2
import random
import numpy as np


def change_light(image, coeff):
    image_HLS = cv2.cvtColor(image,cv2.COLOR_BGR2HLS) ## Conversion to HLS
    image_HLS = np.array(image_HLS, dtype = np.float64) 
    image_HLS[:,:,1] = image_HLS[:,:,1]*coeff ## scale pixel values up or down for channel 1(Lightness)
    if(coeff>1):
        image_HLS[:,:,1][image_HLS[:,:,1]>255]  = 255 ##Sets all values above 255 to 255
    else:
        image_HLS[:,:,1][image_HLS[:,:,1]<0]=0
    image_HLS = np.array(image_HLS, dtype = np.uint8)
    image_BGR = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2BGR) ## Conversion to BGR
    return image_BGR


def is_numpy_array(x):
    return isinstance(x, np.ndarray)

def is_list(x):
    return type(x) is list


def verify_image(image):
    if is_numpy_array(image):
        pass
    elif(is_list(image)):
        image_list=image
        for img in image_list:
            if not is_numpy_array(img):
                raise Exception("error: not numpy image!")
    else:
        raise Exception("error: not numpy image!")


def brighten(image, brightness_coeff=-1): ##function to brighten the image
    verify_image(image)
    if(brightness_coeff!=-1):
        if(brightness_coeff<0.0 or brightness_coeff>1.0):
            raise Exception(err_brightness_coeff)
    if(is_list(image)):
        image_BGR=[]
        image_list=image
        for img in image_list:
            if(brightness_coeff==-1):
                brightness_coeff_t=1+ random.uniform(0,1) ## coeff between 1.0 and 1.5
            else:
                brightness_coeff_t=1+ brightness_coeff ## coeff between 1.0 and 2.0
            image_BGR.append(change_light(img,brightness_coeff_t))
    else:
        if(brightness_coeff==-1):
            brightness_coeff_t=1+ random.uniform(0,1) ## coeff between 1.0 and 1.5
        else:
            brightness_coeff_t=1+ brightness_coeff ## coeff between 1.0 and 2.0
        image_BGR= change_light(image,brightness_coeff_t)
    return image_BGR


def darken(image, darkness_coeff=-1): ##function to darken the image
    verify_image(image)
    if(darkness_coeff!=-1):
        if(darkness_coeff<0.0 or darkness_coeff>1.0):
            raise Exception(err_darkness_coeff) 

    if(is_list(image)):
        image_BGR=[]
        image_list=image
        for img in image_list:
            if(darkness_coeff==-1):
                darkness_coeff_t=1- random.uniform(0,1)
            else:
                darkness_coeff_t=1- darkness_coeff            
            image_BGR.append(change_light(img,darkness_coeff_t))
    else:
        if(darkness_coeff==-1):
             darkness_coeff_t=1- random.uniform(0,1)
        else:
            darkness_coeff_t=1- darkness_coeff  
        image_BGR= change_light(image,darkness_coeff_t)
    return image_BGR



if __name__ == "__main__":
    img = cv2.imread('test_augmentation/image1.jpg')
    for i in range(20):
        darkness_coeff = i * 0.05
        img_bright = brighten(img, darkness_coeff)
        img_dark = darken(img, darkness_coeff)
        cv2.imwrite("bright_%s.jpg" % i, img_bright)
        cv2.imwrite("dark_%s.jpg" % i, img_dark)

