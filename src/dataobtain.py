import os
import selenium
from selenium import webdriver 
import base64
import time
import urllib.request
from selenium.webdriver.common.by import By


DRIVER_PATH = '/usr/local/bin/chromedriver'

SAVE_FOLDER = 'quality_steak/'

GOOGLE_IMAGES = 'https://www.google.com/search?q=quality+raw+steak&tbm=isch&ved=2ahUKEwjjz9utu9T7AhWGLt8KHXtBBrkQ2-cCegQIABAA&oq=quality+raw+steak&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BggAEAcQHjoGCAAQCBAeOggIABAIEAcQHlDgEVjBFmDzG2gAcAB4AIABRIgBsAKSAQE1mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=84qGY6OKEobd_Ab7gpnICw&bih=754&biw=1536&rlz=1C1CHBF_enUS937US937'


driver = webdriver.Chrome(DRIVER_PATH)
driver.get(GOOGLE_IMAGES)

def scroll_to_end():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    print('scroll done')


counter = 0
for i in range(1,2):     
    scroll_to_end()
    image_elements = driver.find_elements(By.CLASS_NAME, 'rg_i')
    print(len(image_elements))
    for image in image_elements: 
        if (image.get_attribute('src') is not None):
            my_image = image.get_attribute('src').split('data:image/jpeg;base64,')
            filename = SAVE_FOLDER + 'helmet'+str(counter)+'.jpeg'
            if(len(my_image) >1): 
                with open(filename, 'wb') as f: 
                    f.write(base64.b64decode(my_image[1]))
            else: 
                print(image.get_attribute('src'))
                urllib.request.urlretrieve(image.get_attribute('src'), SAVE_FOLDER + 'helmet'+ str(counter)+'.jpeg')
            counter += 1