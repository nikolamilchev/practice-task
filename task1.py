from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, InvalidSessionIdException,WebDriverException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://ati.su/")
element = driver.find_element_by_css_selector('li._1BtH6-0-0-361:nth-child(2) > a:nth-child(1)')
element.click()
assert "Поиск транспорта для перевозки груза бесплатно и без регистрации | ATI.SU" in driver.title, 'переход не произошел'
element_out=driver.find_element_by_css_selector('#input-geo-from')
element_out.send_keys('Беларусь')
time.sleep(1)
element_out.send_keys(Keys.ENTER)
element_in=driver.find_element_by_css_selector('#input-geo-to')
element_in.send_keys('Россия')
time.sleep(1)
element_in.send_keys(Keys.ENTER)

element_click=driver.find_element_by_css_selector('._1dpk_-2-0-680 > div:nth-child(1)')
element_click.click()
time.sleep(1)
check=False
try:
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/div[3]/div/div[4]/div[1]/table')
    check=True
except WebDriverException:
    print('не  появились результаты поисковой выдачи ')
    driver.close()
    driver.quit()
if check:
    count=driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/div[3]')
    element_to_go=driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/span[6]/span')#переход
    element_to_go.click()
    time.sleep(1)
    driver.find_elements(By.TAG_NAME, 'button')[-1].find_element_by_xpath("//*[contains(text(), 'Показать контакты')]").click()
    time.sleep(1)

    try:
        iframe = driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/iframe')
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]')
    except NoSuchElementException:
        print('не появился попап регистрации пользователя')

    driver.close()#функция закрытия вкладки
    isClosed = False
    try:
       s=driver.title
    except InvalidSessionIdException:
        isClosed = True

    if isClosed:
        driver.quit()