from selenium import webdriver
from bs4 import BeautifulSoup


class TimeParser:
    global driver
    global options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    def parser(url):
        try:
            driver = webdriver.Chrome(executable_path=r"/home/ubuntu/IZPlanner/chromedriver", chrome_options=options)
            driver.implicitly_wait(1)
            driver.get("http://m.cafe.daum.net" + str(url))

        except AttributeError:
            return "WrongUrl"
        timelist = []
        html = driver.page_source
        i = 0
        soup = BeautifulSoup(html, 'html.parser')
        for time in soup.find_all('div', {'class': "info_schedule"}):
            text = time.text
            # print(text)
            if "요일" in text:
                detailTime = text.replace("시간", '').replace('요일', '요일\n')
                print(detailTime)
                timelist.append(detailTime.strip())

        i += 1
        print(timelist)
        return timelist
