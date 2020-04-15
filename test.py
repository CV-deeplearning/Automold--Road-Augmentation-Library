import Automold as am
import cv2

img = cv2.imread('test_augmentation/image1.jpg')
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


for i in range(20):
    # 测试亮度变化
    #brightness_coeff = i * 0.05
    #bright_img = am.brighten(img, brightness_coeff)
    #bright_img = cv2.cvtColor(bright_img, cv2.COLOR_RGB2BGR)
    #cv2.imwrite("test_imgs/bright_%s.jpg" % i, bright_img)
       
    # 测试暗度变化
    #darkness_coeff = i * 0.05
    #dark_img = am.darken(img, darkness_coeff)
    #dark_img = cv2.cvtColor(dark_img, cv2.COLOR_RGB2BGR)
    #cv2.imwrite("test_imgs/dark_%s.jpg" % i, dark_img)


    # 测试雪量变化
    #snow_coeff = i * 0.05
    #snow_img = am.add_snow(img, snow_coeff)
    #snow_img = cv2.cvtColor(snow_img, cv2.COLOR_RGB2BGR)
    #cv2.imwrite("test_imgs/snow_%s.jpg" % i, snow_img)


    # 测试速度变化
    #speed_coeff = i * 0.05
    #speed_img = am.add_speed(img, speed_coeff)
    #speed_img = cv2.cvtColor(speed_img, cv2.COLOR_RGB2BGR)
    #cv2.imwrite("test_imgs/speed_%s.jpg" % i, speed_img)



    # 测试雾量变化
    #fog_coeff = (i+1) * 0.05
    #fog_img = am.add_fog(img, fog_coeff=fog_coeff)
    #fog_img = cv2.cvtColor(fog_img, cv2.COLOR_RGB2BGR)
    #cv2.imwrite("test_imgs/fog_%s.jpg" % i, fog_img)


    # 测试下雨变化
    if i < 7:
        rain_type = "drizzle"
    elif i > 14:
        rain_type = "torrential"
    else:
        rain_type = "heavy"
    rain_img = am.add_rain(img, rain_type=rain_type)
    rain_img = cv2.cvtColor(rain_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("test_imgs/rain_%s.jpg" % i, rain_img)
    
