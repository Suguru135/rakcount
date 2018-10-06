#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from getpass import getpass

import rakuen
import time



if __name__ == "__main__":

    #ログイン
    id_str = input('名前: ')
    password_str = getpass('パス: ')
    
    #設定
    times = 1
    no_str = '6'
    name_str = 'びーびー'
    contents_str = 'test'
    filepath_str = '/home/pi/pg/python/rakcount/images/top.png'

    print('設定完了')

    #webdriverを準備
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/bin/chromedriver')
    driver.implicitly_wait(10)


    if rakuen.authenticate(driver, id_str, password_str):
        if rakuen.post(driver, no_str, name_str, password_str, contents_str, filepath_str):
            print('投稿')

        else:
           print("投稿失敗")

        time.sleep(2.5)

    else:
        print('認証失敗')
    


    #webdriverを閉じる
    driver.close()
    driver.quit()
	
	

