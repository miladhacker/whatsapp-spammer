from selenium import webdriver
 

class spamer:
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
            self.login()
        except:
            print('ERROR : There is no drive, install the driver')
    def login(self):
        driver = self.driver
        url = 'https://web.whatsapp.com/'
        try:
            driver.get(url)
            input('Scan the QR code and press enter')
            self.send()
        except:
            print('ERROR : Check the internet. The Internet is not connected')
    def send(self):
        driver = self.driver
        while True:
            while True:
                try:
                    name = input('Enter the name of the person you want to send the message to: ')
                    driver.find_element_by_xpath('//span[@title="{}"]'.format(name)).click()
                    break
                except:
                    print('ERROR : This name does not exist, enter a new name')
                    pass
            msg = input('Enter the message: ')
            while True:
                try:
                    count = int(input('How many times is the message sent : '))
                    break
                except:
                    print('ERROR : Enter numbers, do not enter letters')
                    pass
            for i in range(0,count):
                driver.find_element_by_class_name('_3uMse').send_keys(msg)
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
            while True:
                q = input('Do you want to use a robot?(y=yes , n=no) : ')
                if q.lower() == 'y':
                    break
                elif q.lower() == 'n':
                    print('by by')
                    break
                else:
                    pass
            if q.lower() == 'n':
                break
            elif q.lower() == 'y':
                pass
spamer()