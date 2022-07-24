import requests

import Jc_sequence as Jc
from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from urllib.request import urlopen
import urllib.request
import os

def start(): #0번
    global browser
    global stacked_data
    print('시작합니다.')
    browser = webdriver.Chrome('chromedriver.exe')
    stacked_data=[]
    return

def get_url(url): #1번
    global browser
    print('주소 띄우기.')
    browser.get(url)
    return

def wait_time(times): #2번
    global browser
    print('{}초 대기 . . . .'.format(times))
    times=float(times)
    t.sleep(times)
    return browser

def find_elem(value): #3번
    global browser
    global find_target
    print('객체찾기.')
    value = value.split(',')
    value[0] = value[0][2:-1]
    value[1] = value[1][2:-2]
    types=value[0]
    target=value[1]
    if types == 'selector':
        find_target=browser.find_element(By.CSS_SELECTOR,target)
    elif types == 'Xpath':
        find_target=browser.find_element(By.XPATH,target)
    elif types == 'class' :
        find_target=browser.find_element(By.CLASS_NAME,target)
    elif types == 'id':
        find_target=browser.find_element(By.ID,target)
    elif types == 'link_text':
        find_target=browser.find_element(By.LINK_TEXT,target)
    elif types == 'p_link_text':
        find_target=browser.find_element(By.PARTIAL_LINK_TEXT,target)
    else:
        print('types 오류발생.')
    return

def find_elems(value): #4번
    global browser
    global find_target
    print('객체들찾기.')
    value = value.split(',')
    value[0] = value[0][2:-1]
    value[1] = value[1][2:-1]
    value[2] = value[2].replace('[', '').replace('\'','').strip()
    value[3] = value[3].replace(']', '').replace('\'','').strip()
    types=value[0]
    target=value[1]
    start_num=int(value[2])
    end_num=int(value[3])
    if types == 'selector':
        find_target=browser.find_elements(By.CSS_SELECTOR,target)
    elif types == 'Xpath':
        find_target=browser.find_elements(By.XPATH,target)
    elif types == 'class' :
        find_target=browser.find_elements(By.CLASS_NAME,target)
    elif types == 'id':
        find_target=browser.find_elements(By.ID,target)
    elif types == 'link_text':
        find_target=browser.find_elements(By.LINK_TEXT,target)
    elif types == 'p_link_text':
        find_target=browser.find_elements(By.PARTIAL_LINK_TEXT,target)
    else:
        print('types 오류발생.')
        return

    print(find_target)
    if end_num > (len(find_target)-1):
        print('인덱싱 범위 초과')
        return 
    elif start_num==0 and end_num==0:
        print('전체검색')
        return
    elif start_num == end_num :
        print('특정 인덱스 검색')
        find_target=find_target[start_num]
        return
    elif start_num <= end_num:
        print('슬라이싱 검색')
        find_target=find_target[start_num:end_num]
        return
    else:
        print('인덱싱 오류 발생')



def save_datas(): # 5번
    global stacked_data

    file=open('cnt2.txt','r',encoding='UTF-8')
    cnt=int(file.read())
    file.close()
    file=open('save_datas_{}.txt'.format(cnt),'w',encoding='UTF-8')
    for i in range(len(stacked_data)):
        file.write(stacked_data[i])
    file.close()
    cnt+=1
    file=open('cnt2.txt','w',encoding='UTF-8')
    file.write(str(cnt))
    file.close()
    print('txt저장')

def save_images(value): #5_2번
    global search
    global find_target
    global browser

    print('구글 이미지 저장')

    if not os.path.isdir("{}/".format(search)):
        os.makedirs("{}/".format(search))
    images = find_target
    IMGURL = value
    count = 1

    for image in images:

        image.click()
        t.sleep(2)
        imgUrl = browser.find_element(By.XPATH,
            IMGURL).get_attribute('src')
        # requests.Request(imgUrl,headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlretrieve(imgUrl, "{}\{}_{}.jpg".format(search,search,str(count)))
        print("Image saved: {}_{}.jpg".format(search,count))
        count += 1

def release_datas(): # 5_3번
    global stacked_data
    print('데이터 청소')
    stacked_data=[]

def stack_data(): # 5_4번
    global find_target
    global stacked_data
    print('데이터 쌓기')

    for i in range(len(find_target)):
        if '\n' in find_target[i].text:
            a = find_target[i].text.replace('\n', '\t')
        else:
            a = find_target[i].text
        stacked_data.append(a+'\n')

def check_datas(): # 6번
    global stacked_data

    print(len(stacked_data))

def send_keys(value): # 7번
    global find_target
    global  search

    print('문자 입력')
    print(value)

    search=value
    find_target.send_keys(search)

def key_tab(): # 8번
    global find_target
    find_target.send_keys(Keys.TAB)

def key_space(): # 9번
    global find_target
    find_target.send_keys(Keys.SPACE)

def key_enter(): # 10번
    global find_target
    print('enter')
    find_target.send_keys(Keys.ENTER)

def click(): # 11번
    global find_target
    global browser

    find_target.click()

def double_click(): # 12번
    global find_target
    global browser

    webdriver.ActionChains(browser).double_click(find_target).perform()

def move_mouse(): # 13번
    global find_target
    global browser

    webdriver.ActionChains(browser).move_to_element(find_target).perform()

def clickAndhold(): # 14번
    global find_target
    global browser

    webdriver.ActionChains(browser).click_and_hold(find_target).perform()

def release(): # 15번
    global find_target
    global browser

    webdriver.ActionChains(browser).release().perform()

def scrollHeight(): # 16번
    global browser

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scrollTo(value): # 17번
    global browser

    px=int(value)
    browser.execute_script("window.scrollTo(0, {})".format(px))

def moveScroll(): # 18번
    global find_target
    global browser

    action = ActionChains(browser)
    action.move_to_element(find_target).perform()

def pageDown(): #19번
    global find_target
    global browser

    browser.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

def scrollEnd(): #20번
    global find_target
    global browser

    SCROLL_PAUSE_TIME = 1

    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        t.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            t.sleep(1.5)
            try:
                find_target.click()
                print('검색 더 하기 클릭')
                webdriver.ActionChains(browser).release().perform()
            except:
                break
        last_height = new_height

def module(num,value,ndex_cnt):
    global repeat_start
    global repeat_end

    if num == '0':
        start()
    elif num == '1':
        get_url(value)
    elif num == '2':
        wait_time(value)
    elif num == '3':
        find_elem(value)
    elif num == '4':
        find_elems(value)
    elif num == '5':
        save_datas()
    elif num == '5_2':
        save_images(value)
    elif num == '5_3':
        release_datas()
    elif num == '5_4':
        stack_data()
    elif num == '6':
        check_datas()
    elif num == '7':
        send_keys(value)
    elif num == '8':
        key_tab()
    elif num == '9':
        key_space()
    elif num == '10':
        key_enter()
    elif num == '11':
        click()
    elif num == '12':
        double_click()
    elif num == '13':
        move_mouse()
    elif num == '14':
        clickAndhold()
    elif num == '15':
        release()
    elif num == '16':
        scrollHeight()
    elif num == '17':
        scrollTo(value)
    elif num == '18':
        moveScroll()
    elif num == '19':
        pageDown()
    elif num == '20':
        scrollEnd()
    elif num == '21':  # 반복시작
        print('반복시작 체크')
        repeat_start = ndex_cnt
    elif num == '22':  # 반복 끝
        if not repeat_start:
            pass
        else:
            print('반복끝 체크. 반복알고리즘 시작.')
            repeat_cnt=int(value)
            repeat_end = ndex_cnt
            r_range=int(repeat_end)-int(repeat_start)
            lineR = Jc.read_my_sequence()
            lineR = lineR[1:]

            if repeat_cnt==0:
                Rkey = True
                while Rkey:
                    for i in range(r_range-1):
                        ndex_cntR = i
                        valueR = lineR[i+int(repeat_start)+1][1]
                        numR = lineR[i+int(repeat_start)+1][2]
                        try:
                            module(numR, valueR, ndex_cntR)
                        except:
                            print('반복종료')
                            Rkey=False
                            break
            else:
                for m in range(repeat_cnt):
                    for i in range(r_range-1):
                        ndex_cntR = i
                        valueR = lineR[i+int(repeat_start)+1][1]
                        numR = lineR[i+int(repeat_start)+1][2]
                        try:
                            module(numR, valueR, ndex_cntR)
                        except:
                            print('반복종료')
                            break
    else:
        pass

def start_Macro():
    global browser
    global repeat_start
    global repeat_end

    repeat_end=''
    repeat_start=''
    lines = Jc.read_my_sequence()
    lines = lines[1:]
    print(lines)
    for i in range(len(lines)):
        ndex_cnt=i
        value=lines[i][1]
        num=lines[i][2]
        print(num)
        module(num,value,ndex_cnt)

if __name__ == '__main__':
    pass