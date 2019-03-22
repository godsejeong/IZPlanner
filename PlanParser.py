from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

driver = webdriver.Chrome('/Users/jaemin/PycharmProjects/IZPlanner/chromedriver')
driver.implicitly_wait(1)
driver.get('http://m.cafe.daum.net/official-izone/l0C7?boardType=Q')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

titleList = []
subTitleList = []
timeList = []
planDict = OrderedDict()
PlanningJson = OrderedDict()
# 요일 - 일정명,일정분류,일정시간,링크(일정세시간)
for test in soup.select('div.schedule_list > div'):
    #List clear
    titleList.clear()
    timeList.clear()
    subTitleList.clear()
    # weather search
    daydata = test.find('strong', {'class': 'txt_day'}).text
    day = daydata.replace('.', "일")
    # data Pasing
    for title in test.find_all('strong', {'class': 'tit_subject'}):
        titleList.append(title.text)
    for subTitle in test.find_all('em'):
        subTitleList.append(subTitle.text)
    for time in test.find_all('span', {'class': 'inner_tit'}):
        timeList.append(time.text)
    #data save to Json
    planDict['title'] = titleList.copy()
    planDict['subTitle'] = subTitleList.copy()
    planDict['time'] = timeList.copy()
    PlanningJson[day] = dict(planDict)
print(json.dumps(PlanningJson, ensure_ascii=False, indent="\t"))
