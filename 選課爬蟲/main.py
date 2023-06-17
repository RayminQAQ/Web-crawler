"""
Program: 選課爬蟲，專門為台科大選課系統設計
Author: Raymin
Notice: 修改的地方有兩個，一個是帳號、一個是要選課的課碼
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import ddddocr

class CourseSelect:
    def __init__(self, ID: str, Password: str, course: str, Browser : str): 
        self.ID = ID
        self.Password = Password
        self.login_url = Browser
        self.course = course # 選課識別碼位置 or 課碼
        
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.now = time.time()
        self.timeLimit = ()

    def LoginAccount(self) -> None: 
        self.driver.get(self.login_url)
        self.driver.find_element(By.NAME, 'UserName').send_keys(self.ID)
        self.driver.find_element(By.NAME, 'Password').send_keys(self.Password)
        time.sleep(2) # for bypassing robot authenticate or user input in 10 sec
        self.driver.find_element(By.ID, 'btnLogIn').click()

    def openPage(self) -> None:
        try:
            self.driver.find_element(By.LINK_TEXT, "初選選課").click()
            self.driver.find_element(By.LINK_TEXT, "電腦抽選後選課").click()
        except:
            print("bug when trying openPage")
        
    def Select(self) -> None:
        for data in self.course:
            try:
                self.driver.find_element(By.NAME, "CourseText").send_keys(data)
                self.driver.find_element(By.ID, "SingleAdd").click()
                time.sleep(0.5)
                # alert = self.driver.switch_to_alert()
                # alert_text = alert.text
            except:
                print("bug when trying CourseSelect")

    def inTime(self) -> bool:
        if self.now - time.time() < self.timeLimit:
            return True
        else:
            return False

    def run(self, run_time: int) -> None:
        self.LoginAccount()
        time.sleep(10)
        self.openPage()
        
        self.timeLimit = run_time
        while True:
            self.Select()

            """
            if self.inTime():
                self.Select()
            else:
                break    
            """
        
    
if __name__ == '__main__':
    # 帳號 密碼 課碼
    account = "帳號"
    password = "密碼"
    course = ["FE1471702"]
    app = CourseSelect(account, password, course,"https://stuinfosys.ntust.edu.tw/NTUSTSSOServ/SSO/Login/CourseSelection?ReturnUrl=CourseSelection")
    app.run(100)
