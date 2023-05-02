from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def test_selenium():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://127.0.0.1/mgr/sign.html")
    driver.find_element(By.ID,"password").send_keys("88888888")
    driver.find_element(By.ID,"username").send_keys("byhy")
    driver.find_element(By.CLASS_NAME,"btn").click()
    #检测左侧菜单前三项是不是为客户，药品，订单
    lists_ul=driver.find_element(By.CLASS_NAME,"sidebar-menu")
    lists_li=lists_ul.find_elements(By.TAG_NAME,"li")
    # lists_a=lists_li.find_elements(By.TAG_NAME,"a")
    # for i in lists_a:
    #     print(i)
    lists_a=[]
    for li in range(len(lists_li)):
        lists_a[li]=li
    print(lists_a)
    sleep(3)
if __name__ == '__main__':
    test_selenium()


