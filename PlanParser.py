from selenium import webdriver
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

driver = webdriver.Chrome('/Users/jaemin/PycharmProjects/IZPlanner/chromedriver')
driver.implicitly_wait(1)
driver.get('http://m.cafe.daum.net/official-izone/l0C7?boardType=Q')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

def plan():
    titleList = []
    subTitleList = []
    timeList = []
    detailLink = []

    itemList = []

    planDict = OrderedDict()
    planningJson = OrderedDict()


    # 요일 - 일정명,일정분류,일정시간,링크(일정상세시간)
    for planBox in soup.select('div.schedule_list > div'):
        #list clear
        titleList.clear()
        timeList.clear()
        subTitleList.clear()
        detailLink.clear()
        # weather search
        daydata = planBox.find('strong', {'class': 'txt_day'}).text
        day = daydata.replace('.', "일")
        # data Pasing

        for planLink in planBox.find_all('a',{'class' : 'tiara_button'}):
            detailLink.append(planLink.get('href'))
        for title in planBox.find_all('strong', {'class': 'tit_subject'}):
            titleList.append(title.text)
        for subTitle in planBox.find_all('em'):
            subTitleList.append(subTitle.text)
        for time in planBox.find_all('span', {'class': 'inner_tit'}):
            timeList.append(time.text)

        #data save to Json
        planDict['day'] = day
        planDict['title'] = titleList.copy()
        planDict['subTitle'] = subTitleList.copy()
        planDict['time'] = timeList.copy()
        planDict['link'] = detailLink.copy()
        itemList.append(dict(planDict))

    planningJson = itemList

    print(json.dumps(planningJson, ensure_ascii=False, indent="\t"))
    return planningJson

def detailPlan():
    detailDict = OrderedDict()
    for planBox in soup.select('div.schedule_list > div'):
        daydata = planBox.find('strong', {'class': 'txt_day'}).text
        day = daydata.replace('.', "일")
        for title in planBox.find_all('strong', {'class': 'tit_subject'}):
            link = planBox.find('a', {'class': 'tiara_button'})
            detailDict[day + " " + title.text] = link.get('href')
    return detailDict
    print(json.dumps(detailDict, ensure_ascii=False, indent="\t"))



