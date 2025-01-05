import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def load_config():
    return {
        "login_url": "登录网址",   #替换为校园网登录页面网址
        "username": "账号",  #替换为你的账号
        "password": "密码"    #替换为你的密码
    }

def auto_login():
    config = load_config()
    
    options = Options()
    options.add_argument('--headless') 
    
    service = Service(r"D:\Desktop\ayit\msedgedriver.exe")   #这里替换为你的路径
    driver = webdriver.Edge(service=service, options=options)
    
    try:
        driver.get(config['login_url'])
        
        try:
            if "您已经成功登录" in driver.page_source:
                print("已经登录！")
                return
        except:
            pass
        
        try:
            username_input = driver.find_element(By.CSS_SELECTOR, "input[class='edit_lobo_cell'][type='text']")
            username_input.send_keys(config['username'])
        
            password_input = driver.find_element(By.CSS_SELECTOR, "input[class='edit_lobo_cell'][type='password']")
            password_input.send_keys(config['password'])
        
            login_button = driver.find_element(By.CSS_SELECTOR, "input[class='edit_lobo_cell'][type='button']")
            login_button.click()
        
            print("登录成功！")
        
        except Exception as e:
            print(f"登录过程出错：{str(e)}")
            
    except Exception as e:
        print(f"浏览器操作失败：{str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    auto_login() 