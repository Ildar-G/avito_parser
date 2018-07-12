from selenium import webdriver
import time
from PIL import Image
from pytesseract import image_to_string

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.navigate()

    def take_shot(self):
        self.driver.save_screenshot('avito.png')

    def tel_recon(self):
        image = Image.open('tel.png')
        print(image_to_string(image))


    def crop(self, location, size):
        image = Image.open('avito.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image.crop((x,y-130, x+width, y+height-125)).save('tel.png')
        self.tel_recon()







    def navigate(self):
        self.driver.get('https://www.avito.ru/sankt-peterburg/noutbuki/ultrabuk_c_tachskrinom_fujitsu_lifebook_u745_1203997965?slocation=653240')

        #button = self.driver.find_element_by_xpath('//button[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        #/html/body/div[4]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div/div/a

        button = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div/div/a')
        button.click()
        time.sleep(0.4)

        self.take_shot()
        image =self.driver.find_element_by_xpath('/html/body/div[12]/div[3]/div/div/div[1]/img')
        location = image.location # X Y position
        size = image.size #размер {'w":, 'h':}

        self.crop(location, size)




def main():
    b = Bot()



if __name__ == '__main__':
    main()