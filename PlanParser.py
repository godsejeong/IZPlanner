import os
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

import DetailsTimeParser


def driver_setting():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-setuid-sandbox")

    driver = webdriver.Chrome(executable_path=r"/home/ubuntu/IZPlanner/chromedriver", chrome_options=options)
    driver.implicitly_wait(3)
    driver.get('http://m.cafe.daum.net/official-izone/l0C7?boardType=Q')

    return driver.page_source


def plan():
    global month

    soup = BeautifulSoup(driver_setting(), 'html.parser')

    month = datetime.today().month
    if month < 10:
        month = '0' + str(month)

    titleList = []
    subTitleList = []
    timeList = []
    detailLink = []

    itemList = []

    planDict = OrderedDict()
    planningJson = OrderedDict()

    # 요일 - 일정명,일정분류,일정시간,링크(일정상세시간)
    for planBox in soup.select('div.schedule_list > div'):
        # list clear
        titleList.clear()
        timeList.clear()
        subTitleList.clear()
        detailLink.clear()
        # weather search
        daydata = planBox.find('strong', {'class': 'txt_day'}).text

        day = month + '/' + daydata.split()[0].replace(".", '').strip()
        dow = daydata.split()[1]

        # data Pasing
        for planLink in planBox.find_all('a', {'class': 'tiara_button'}):
            detailLink.append(planLink.get('href'))
        for title in planBox.find_all('strong', {'class': 'tit_subject'}):
            titleList.append(title.text)
        for subTitle in planBox.find_all('em'):
            subTitleList.append(subTitle.text)
        for time in planBox.find_all('span', {'class': 'inner_tit'}):
            timeList.append(time.text)

        # data save to Json
        planDict['day'] = day
        planDict['dow'] = dow
        planDict['title'] = titleList.copy()
        planDict['subTitle'] = subTitleList.copy()
        planDict['time'] = timeList.copy()
        planDict['link'] = detailLink.copy()
        itemList.append(dict(planDict))

    planningJson = itemList

    print(json.dumps(planningJson, ensure_ascii=False, indent="\t"))
    return planningJson
    # driver.close()


def detailPlan():
    detailDict = OrderedDict()
    soup = BeautifulSoup(driver_setting(), 'html.parser')
    for planBox in soup.select('div.schedule_list > div'):
        daydata = planBox.find('strong', {'class': 'txt_day'}).text
        day = daydata.replace('.', "")
        link = planBox.find('a', {'class': 'tiara_button'})
        time = DetailsTimeParser.TimeParser.parser(link.get('href'))
        detailDict[day] = time
    print(detailDict)
    return detailDict
    print(json.dumps(detailDict, ensure_ascii=False, indent="\t"))
