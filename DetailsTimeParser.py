from selenium import webdriver
from bs4 import BeautifulSoup


class TimeParser:
    def parser(url):
        try:
            driver = webdriver.Chrome('/Users/jaemin/PycharmProjects/IZPlanner/chromedriver')
            driver.implicitly_wait(1)
            driver.get("http://m.cafe.daum.net" + str(url))
        except AttributeError:
            return "WrongUrl"
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        time = soup.select('div.info_schedule')[1].text
        detailTime = time.replace("시간", '').replace('일', '일\n')
        print(detailTime.strip())
        return detailTime.strip()
