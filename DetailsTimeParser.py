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
            driver = webdriver.Chrome(executable_path=r"/home/ubuntu/IZPlanner/chromedriver",chrome_options=options)
            driver.implicitly_wait(1)
            driver.get("http://m.cafe.daum.net" + str(url))
	    
        except AttributeError:
            return "WrongUrl"
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        time = soup.find_all('div',{'class' : 'info_schedule'})[1].text

        detailTime = time.replace("시간", '').replace('일', '일\n')
        print(detailTime.strip())
        return detailTime.strip()
	
