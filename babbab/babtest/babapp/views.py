from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime


driver = webdriver.Chrome('/babbab/babtest/babapp/chromedriver/chromedriver')       #chromedriver실행
driver.get('http://intec.icehs.kr/foodlist.do?m=060406&s=intec')                    #학교 급식실 사이트 불러오기
print("<<<Open Chrome>>>\n")

day_select = 'div.tb_base_box.tm_box > table > tbody > tr > th > span'              #일수가 저장된 태그 select문
menu_select = 'div.tb_base_box.tm_box > table > tbody > tr > td'                    #급식 메뉴가 저장된 태그 select문
source = '인천전자마이스터고-학생마당-급식실'   

today = datetime.datetime.now()                             #현재 날짜&시간 변수 생성
tomorrow = today + datetime.timedelta(days = 1)             #내일 날짜 변수 생성
tda = today + datetime.timedelta(days = 2)                  #모레 날짜 변수 생성

#[날짜(일)][0 = 언제 식사인지, 1 = 파싱한 날짜, 2 = [0 = 메뉴, 1 = 알레르기 표시]]

temp = [['\0', ['\0', '\0']],  # 1day           #파싱 중 사용되는 임시 배열
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],  # 10day
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],  # 20day
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],
        ['\0', ['\0', '\0']],  # 30day
        ['\0', ['\0', '\0']]]
menu1 = [["Breakfast", '\0', ['\0', '\0']],  # 1day             #조식 메뉴가 저장되는 배열
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],  # 10day
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],  # 20day
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],
         ["Breakfast", '\0', ['\0', '\0']],  # 30day
         ["Breakfast", '\0', ['\0', '\0']]]
menu2 = [["Lunch", '\0', ['\0', '\0']],  # 1day                 #중식 메뉴가 저장되는 배열   
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],  # 10day
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],  # 20day
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],
         ["Lunch", '\0', ['\0', '\0']],  # 30day
         ["Lunch", '\0', ['\0', '\0']]]
menu3 = [["Dinner", '\0', ['\0', '\0']],  # 1day                #석식 메뉴가 저장되는 배열
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],  # 10day
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],  # 20day
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],
         ["Dinner", '\0', ['\0', '\0']],  # 30day
         ["Dinner", '\0', ['\0', '\0']]]

count = 0

def button_click(when):             #조식, 중식, 석식 버튼을 누르는 함수
    if when == 1:
        driver.find_element_by_css_selector('#B').click()
    elif when == 2:
        driver.find_element_by_css_selector('#L').click()
    elif when == 3:
        driver.find_element_by_css_selector('#D').click()


def parsing():                      #현재 페이지의 html소스를 가져오는 함수
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    return soup


def trim(n):                        #html문에서 불필요한 데이터를 제거하는 함수
    menu_text = str(n).replace("<br/>","\n").replace("</td>","").replace("</ul>","")
    menu_text = menu_text.replace("<", "").replace(">", "").replace("td", "").replace("ul", "")
    menu_text = menu_text.replace('class="cal_sat"', "").replace('class="cal_sun"', "").replace('class="today"', "")

    return menu_text


print("Loading")

for i in range(1, 4):               #조식, 중식, 석식 차례대로 파싱&배열에 저장하는 반복문
    button_click(i)
    noticesDay = parsing().select(day_select)
    noticesMenu = parsing().select(menu_select)

    print(".....")

    for n in noticesDay:
        temp[count][0] = n.text
        count = count + 1

    count = 0

    for n in noticesMenu:
        temp[count][1] = trim(n).strip().replace("/","\n").replace("\n\n\n","").split('*')
        temp[count][1][0] = temp[count][1][0].replace("(고)","").replace("(완)","").\
                            replace("(완제품)","").replace("(완제)","").replace("(고중)","")

        for change in range(1, 11):
            change = change % 10
            temp[count][1][0] = temp[count][1][0].replace(str(change),"").replace(".","")

        count = count + 1

    count = 0

    if i == 1:
        for n in temp:
            menu1[count][1] = temp[count][0]
            menu1[count][2] = temp[count][1]
            count = count + 1
    elif i == 2:
        for n in temp:
            menu2[count][1] = temp[count][0]
            menu2[count][2] = temp[count][1]
            count = count + 1
    elif i == 3:
        for n in temp:
            menu3[count][1] = temp[count][0]
            menu3[count][2] = temp[count][1]
            count = count + 1

    count = 0


for n in range(0,31):               #급식이 없는 경우 (급식 없음)으로 대체
    if menu1[n][2][0] == "":
        menu1[n][2][0] = "(학교 홈페이지의 장애로 인해 급식을 가져올 수 없습니다.)"
    if menu2[n][2][0] == "":
        menu2[n][2][0] = "(학교 홈페이지의 장애로 인해 급식을 가져올 수 없습니다.)"
    if menu3[n][2][0] == "":
        menu3[n][2][0] = "(학교 홈페이지의 장애로 인해 급식을 가져올 수 없습니다.)"    

print("\nCOMPLETE!\n")
driver.quit()                       #chromedriver 종료


def index(request):                 #사이트에 데이터를 return하는 함수

    html =\
        '<html>' \
        '<head>' \
        '<title>인마고BAB</title>' \
        '</head>' \
        '<body>' \
        '<div style="border:5px solid; padding:15px; background-color:black;">'\
        '<h1 class="title"style = "color:white;font-size:40px;">&nbsp; 인마고 급식 알리미 B.A.B.</h1>'\
        '</div>' \
        '<p class = "source"' \
        'style = "font-size:30px;color:Gray;text-align:left;margin-left: 1em;font-weight:bold"' \
        'a:link {color:#007cd0;text-decoration:none}'\
        'a:visited {color:#007cd0;text-decoration:none}' \
        'a:active {color:#007cd0;text-decoration:none}' \
        'a:hover {color:#0099ff;text-decoration:none} ">'\
        '<A href = "http://inmagobab.ml" style="text-decoration:none">메인화면</A>&nbsp; &nbsp; &nbsp;'\
        '<A href = "source" style="text-decoration:none">출처</A>&nbsp; &nbsp; &nbsp;'\
        '<A href = "info" style="text-decoration:none">개발정보</A>&nbsp; &nbsp; &nbsp;'\
        '<A href = "month" style="text-decoration:none">이달의식단</A></br>'\
        '<hr>' \
        '<h1 class ="title"style = "font-size:28px;color:SlateBlue;margin-left: 0.8em;"> 오늘 급식 (%s월%s일)</h1>' \
        '<td>' \
        '<p class ="breakfast"><time style="font-weight:bold;margin-left: 1.5em;">조식 : </time><men>%s</men></p>' \
        '<p class ="lunch"><time style="font-weight:bold;margin-left: 1.5em;">중식 : </time><men>%s</men></p>' \
        '<p class ="dinner"><time style="font-weight:bold;margin-left: 1.5em;">석식 : </time><men>%s</men></p>' \
        '</td>' \
        '<hr>' \
        '<h1 class ="title"style = "font-size:28px;color:SlateBlue;margin-left: 0.8em;">내일 급식 (%s월%s일)</h1>' \
        '<tm>' \
        '<p class ="breakfast"><time style="font-weight:bold;margin-left: 1.5em;">조식 : </time><men>%s</men></p>' \
        '<p class ="lunch"><time style="font-weight:bold;margin-left: 1.5em;">중식 : </time><men>%s</men></p>' \
        '<p class ="dinner"><time style="font-weight:bold;margin-left: 1.5em;">석식 : </time><men>%s</men></p>' \
        '</tm>' \
        '<hr>' \
        % (today.month, today.day, menu1[today.day-1][2][0], menu2[today.day-1][2][0], menu3[today.day-1][2][0],
            tomorrow.month, tomorrow.day, menu1[today.day][2][0], menu2[today.day][2][0], menu3[today.day][2][0])

    return HttpResponse(html) #(사이트)출력


def month(request):

    babmonth=\
        '<html>' \
        '<head>' \
        '<title>이달의 식단</title>' \
        '</head>' \
        '<body>'\
        '<div style="border:5px solid; padding:15px; background-color:black;">'\
        '<h1 class="title"style = "color:white;font-size:40px">&nbsp; 인마고 급식 알리미 B.A.B.</h1>'\
        '</div>'\
        '<p class = "source"style = "font-size:30px;color:Gray;text-align:left;margin-left: 1em;font-weight:bold"'\
        'a:link {color:#007cd0;text-decoration:none}' \
        'a:visited {color:#007cd0;text-decoration:none}' \
        'a:active {color:#007cd0;text-decoration:none}'\
        'a:hover {color:#0099ff;text-decoration:none}">' \
        '<A href = "http://inmagobab.ml" style="text-decoration:none">메인화면</A>&nbsp; &nbsp; &nbsp;'\
        '<A href = "source" style="text-decoration:none">출처</A>&nbsp; &nbsp; &nbsp;'\
        '<A href = "info" style="text-decoration:none">개발정보</A>&nbsp; &nbsp; &nbsp;'\
        '<A href = "month" style="text-decoration:none">이달의식단</A></br>'\
        '<hr>' \
        '<h2 class="bf_title"style = "font-size:24px;margin-left: 1.2em">11월 조식</h2>' \
        '<bf style = "font-size:15px">' \
        '<p class="1" style = "margin-left: 2em"><day style="font-weight:bold">1일 : </day><men>%s</men></p>' \
        '<p class="2" style = "margin-left: 2em"><day style="font-weight:bold">2일 : </day><men>%s</men></p>' \
        '<p class="3" style = "margin-left: 2em"><day style="font-weight:bold">3일 : </day><men>%s</men></p>' \
        '<p class="4" style = "margin-left: 2em"><day style="font-weight:bold">4일 : </day><men>%s</men></p>' \
        '<p class="5" style = "margin-left: 2em"><day style="font-weight:bold">5일 : </day><men>%s</men></p>' \
        '<p class="6" style = "margin-left: 2em"><day style="font-weight:bold">6일 : </day><men>%s</men></p>' \
        '<p class="7" style = "margin-left: 2em"><day style="font-weight:bold">7일 : </day><men>%s</men></p>' \
        '<p class="8" style = "margin-left: 2em"><day style="font-weight:bold">8일 : </day><men>%s</men></p>' \
        '<p class="9" style = "margin-left: 2em"><day style="font-weight:bold">9일 : </day><men>%s</men></p>' \
        '<p class="10" style = "margin-left: 2em"><day style="font-weight:bold">10일 : </day><men>%s</men></p>' \
        '<p class="11" style = "margin-left: 2em"><day style="font-weight:bold">11일 : </day><men>%s</men></p>' \
        '<p class="12" style = "margin-left: 2em"><day style="font-weight:bold">12일 : </day><men>%s</men></p>' \
        '<p class="13" style = "margin-left: 2em"><day style="font-weight:bold">13일 : </day><men>%s</men></p>' \
        '<p class="14" style = "margin-left: 2em"><day style="font-weight:bold">14일 : </day><men>%s</men></p>' \
        '<p class="15" style = "margin-left: 2em"><day style="font-weight:bold">15일 : </day><men>%s</men></p>' \
        '<p class="16" style = "margin-left: 2em"><day style="font-weight:bold">16일 : </day><men>%s</men></p>' \
        '<p class="17" style = "margin-left: 2em"><day style="font-weight:bold">17일 : </day><men>%s</men></p>' \
        '<p class="18" style = "margin-left: 2em"><day style="font-weight:bold">18일 : </day><men>%s</men></p>' \
        '<p class="19" style = "margin-left: 2em"><day style="font-weight:bold">19일 : </day><men>%s</men></p>' \
        '<p class="20" style = "margin-left: 2em"><day style="font-weight:bold">20일 : </day><men>%s</men></p>' \
        '<p class="21" style = "margin-left: 2em"><day style="font-weight:bold">21일 : </day><men>%s</men></p>' \
        '<p class="22" style = "margin-left: 2em"><day style="font-weight:bold">22일 : </day><men>%s</men></p>' \
        '<p class="23" style = "margin-left: 2em"><day style="font-weight:bold">23일 : </day><men>%s</men></p>' \
        '<p class="24" style = "margin-left: 2em"><day style="font-weight:bold">24일 : </day><men>%s</men></p>' \
        '<p class="25" style = "margin-left: 2em"><day style="font-weight:bold">25일 : </day><men>%s</men></p>' \
        '<p class="26" style = "margin-left: 2em"><day style="font-weight:bold">26일 : </day><men>%s</men></p>' \
        '<p class="27" style = "margin-left: 2em"><day style="font-weight:bold">27일 : </day><men>%s</men></p>' \
        '<p class="28" style = "margin-left: 2em"><day style="font-weight:bold">28일 : </day><men>%s</men></p>' \
        '<p class="29" style = "margin-left: 2em"><day style="font-weight:bold">29일 : </day><men>%s</men></p>' \
        '<p class="30" style = "margin-left: 2em"><day style="font-weight:bold">30일 : </day><men>%s</men></p>' \
        '</bf>' \
        '<hr>' \
        '<h2 class="lc_title"style = "font-size:24px;margin-left: 1.2em">11월 중식</h2> ' \
        '<lc style = "font-size:15px">' \
        '<p class="1" style = "margin-left: 2em"><day style="font-weight:bold">1일 : </day><men>%s</men></p>' \
        '<p class="2" style = "margin-left: 2em"><day style="font-weight:bold">2일 : </day><men>%s</men></p>' \
        '<p class="3" style = "margin-left: 2em"><day style="font-weight:bold">3일 : </day><men>%s</men></p>' \
        '<p class="4" style = "margin-left: 2em"><day style="font-weight:bold">4일 : </day><men>%s</men></p>' \
        '<p class="5" style = "margin-left: 2em"><day style="font-weight:bold">5일 : </day><men>%s</men></p>' \
        '<p class="6" style = "margin-left: 2em"><day style="font-weight:bold">6일 : </day><men>%s</men></p>' \
        '<p class="7" style = "margin-left: 2em"><day style="font-weight:bold">7일 : </day><men>%s</men></p>' \
        '<p class="8" style = "margin-left: 2em"><day style="font-weight:bold">8일 : </day><men>%s</men></p>' \
        '<p class="9" style = "margin-left: 2em"><day style="font-weight:bold">9일 : </day><men>%s</men></p>' \
        '<p class="10" style = "margin-left: 2em"><day style="font-weight:bold">10일 : </day><men>%s</men></p>' \
        '<p class="11" style = "margin-left: 2em"><day style="font-weight:bold">11일 : </day><men>%s</men></p>' \
        '<p class="12" style = "margin-left: 2em"><day style="font-weight:bold">12일 : </day><men>%s</men></p>' \
        '<p class="13" style = "margin-left: 2em"><day style="font-weight:bold">13일 : </day><men>%s</men></p>' \
        '<p class="14" style = "margin-left: 2em"><day style="font-weight:bold">14일 : </day><men>%s</men></p>' \
        '<p class="15" style = "margin-left: 2em"><day style="font-weight:bold">15일 : </day><men>%s</men></p>' \
        '<p class="16" style = "margin-left: 2em"><day style="font-weight:bold">16일 : </day><men>%s</men></p>' \
        '<p class="17" style = "margin-left: 2em"><day style="font-weight:bold">17일 : </day><men>%s</men></p>' \
        '<p class="18" style = "margin-left: 2em"><day style="font-weight:bold">18일 : </day><men>%s</men></p>' \
        '<p class="19" style = "margin-left: 2em"><day style="font-weight:bold">19일 : </day><men>%s</men></p>' \
        '<p class="20" style = "margin-left: 2em"><day style="font-weight:bold">20일 : </day><men>%s</men></p>' \
        '<p class="21" style = "margin-left: 2em"><day style="font-weight:bold">21일 : </day><men>%s</men></p>' \
        '<p class="22" style = "margin-left: 2em"><day style="font-weight:bold">22일 : </day><men>%s</men></p>' \
        '<p class="23" style = "margin-left: 2em"><day style="font-weight:bold">23일 : </day><men>%s</men></p>' \
        '<p class="24" style = "margin-left: 2em"><day style="font-weight:bold">24일 : </day><men>%s</men></p>' \
        '<p class="25" style = "margin-left: 2em"><day style="font-weight:bold">25일 : </day><men>%s</men></p>' \
        '<p class="26" style = "margin-left: 2em"><day style="font-weight:bold">26일 : </day><men>%s</men></p>' \
        '<p class="27" style = "margin-left: 2em"><day style="font-weight:bold">27일 : </day><men>%s</men></p>' \
        '<p class="28" style = "margin-left: 2em"><day style="font-weight:bold">28일 : </day><men>%s</men></p>' \
        '<p class="29" style = "margin-left: 2em"><day style="font-weight:bold">29일 : </day><men>%s</men></p>' \
        '<p class="30" style = "margin-left: 2em"><day style="font-weight:bold">30일 : </day><men>%s</men></p>' \
        '</lc>' \
        '<hr>' \
        '<h2 class="dn_title"style = "font-size:24px;margin-left: 1.2em">11월 석식</h2> ' \
        '<dn style = "font-size:15px">' \
        '<p class="1" style = "margin-left: 2em"><day style="font-weight:bold">1일 : </day><men>%s</men></p>' \
        '<p class="2" style = "margin-left: 2em"><day style="font-weight:bold">2일 : </day><men>%s</men></p>' \
        '<p class="3" style = "margin-left: 2em"><day style="font-weight:bold">3일 : </day><men>%s</men></p>' \
        '<p class="4" style = "margin-left: 2em"><day style="font-weight:bold">4일 : </day><men>%s</men></p>' \
        '<p class="5" style = "margin-left: 2em"><day style="font-weight:bold">5일 : </day><men>%s</men></p>' \
        '<p class="6" style = "margin-left: 2em"><day style="font-weight:bold">6일 : </day><men>%s</men></p>' \
        '<p class="7" style = "margin-left: 2em"><day style="font-weight:bold">7일 : </day><men>%s</men></p>' \
        '<p class="8" style = "margin-left: 2em"><day style="font-weight:bold">8일 : </day><men>%s</men></p>' \
        '<p class="9" style = "margin-left: 2em"><day style="font-weight:bold">9일 : </day><men>%s</men></p>' \
        '<p class="10" style = "margin-left: 2em"><day style="font-weight:bold">10일 : </day><men>%s</men></p>' \
        '<p class="11" style = "margin-left: 2em"><day style="font-weight:bold">11일 : </day><men>%s</men></p>' \
        '<p class="12" style = "margin-left: 2em"><day style="font-weight:bold">12일 : </day><men>%s</men></p>' \
        '<p class="13" style = "margin-left: 2em"><day style="font-weight:bold">13일 : </day><men>%s</men></p>' \
        '<p class="14" style = "margin-left: 2em"><day style="font-weight:bold">14일 : </day><men>%s</men></p>' \
        '<p class="15" style = "margin-left: 2em"><day style="font-weight:bold">15일 : </day><men>%s</men></p>' \
        '<p class="16" style = "margin-left: 2em"><day style="font-weight:bold">16일 : </day><men>%s</men></p>' \
        '<p class="17" style = "margin-left: 2em"><day style="font-weight:bold">17일 : </day><men>%s</men></p>' \
        '<p class="18" style = "margin-left: 2em"><day style="font-weight:bold">18일 : </day><men>%s</men></p>' \
        '<p class="19" style = "margin-left: 2em"><day style="font-weight:bold">19일 : </day><men>%s</men></p>' \
        '<p class="20" style = "margin-left: 2em"><day style="font-weight:bold">20일 : </day><men>%s</men></p>' \
        '<p class="21" style = "margin-left: 2em"><day style="font-weight:bold">21일 : </day><men>%s</men></p>' \
        '<p class="22" style = "margin-left: 2em"><day style="font-weight:bold">22일 : </day><men>%s</men></p>' \
        '<p class="23" style = "margin-left: 2em"><day style="font-weight:bold">23일 : </day><men>%s</men></p>' \
        '<p class="24" style = "margin-left: 2em"><day style="font-weight:bold">24일 : </day><men>%s</men></p>' \
        '<p class="25" style = "margin-left: 2em"><day style="font-weight:bold">25일 : </day><men>%s</men></p>' \
        '<p class="26" style = "margin-left: 2em"><day style="font-weight:bold">26일 : </day><men>%s</men></p>' \
        '<p class="27" style = "margin-left: 2em"><day style="font-weight:bold">27일 : </day><men>%s</men></p>' \
        '<p class="28" style = "margin-left: 2em"><day style="font-weight:bold">28일 : </day><men>%s</men></p>' \
        '<p class="29" style = "margin-left: 2em"><day style="font-weight:bold">29일 : </day><men>%s</men></p>' \
        '<p class="30" style = "margin-left: 2em"><day style="font-weight:bold">30일 : </day><men>%s</men></p>' \
        '</dn>' \
        '</body>' \
    %(menu1[0][2][0].replace("\n", "/"), menu1[1][2][0].replace("\n", "/"), menu1[2][2][0].replace("\n", "/"),
      menu1[3][2][0].replace("\n", "/"), menu1[4][2][0].replace("\n", "/"), menu1[5][2][0].replace("\n", "/"),
      menu1[6][2][0].replace("\n", "/"), menu1[7][2][0].replace("\n", "/"), menu1[8][2][0].replace("\n", "/"),
      menu1[9][2][0].replace("\n", "/"), menu1[10][2][0].replace("\n", "/"), menu1[11][2][0].replace("\n", "/"),
      menu1[12][2][0].replace("\n", "/"), menu1[13][2][0].replace("\n", "/"), menu1[14][2][0].replace("\n", "/"),
      menu1[15][2][0].replace("\n", "/"), menu1[16][2][0].replace("\n", "/"), menu1[17][2][0].replace("\n", "/"),
      menu1[18][2][0].replace("\n", "/"), menu1[19][2][0].replace("\n", "/"), menu1[20][2][0].replace("\n", "/"),
      menu1[21][2][0].replace("\n", "/"), menu1[22][2][0].replace("\n", "/"), menu1[23][2][0].replace("\n", "/"),
      menu1[24][2][0].replace("\n", "/"), menu1[25][2][0].replace("\n", "/"), menu1[26][2][0].replace("\n", "/"),
      menu1[27][2][0].replace("\n", "/"), menu1[28][2][0].replace("\n", "/"), menu1[29][2][0].replace("\n", "/"),
      menu2[0][2][0].replace("\n", "/"), menu2[1][2][0].replace("\n", "/"), menu2[2][2][0].replace("\n", "/"),
      menu2[3][2][0].replace("\n", "/"), menu2[4][2][0].replace("\n", "/"), menu2[5][2][0].replace("\n", "/"),
      menu2[6][2][0].replace("\n", "/"), menu2[7][2][0].replace("\n", "/"), menu2[8][2][0].replace("\n", "/"),
      menu2[9][2][0].replace("\n", "/"), menu2[10][2][0].replace("\n", "/"), menu2[11][2][0].replace("\n", "/"),
      menu2[12][2][0].replace("\n", "/"), menu2[13][2][0].replace("\n", "/"), menu2[14][2][0].replace("\n", "/"),
      menu2[15][2][0].replace("\n", "/"), menu2[16][2][0].replace("\n", "/"), menu2[17][2][0].replace("\n", "/"),
      menu2[18][2][0].replace("\n", "/"), menu2[19][2][0].replace("\n", "/"), menu2[20][2][0].replace("\n", "/"),
      menu2[21][2][0].replace("\n", "/"), menu2[22][2][0].replace("\n", "/"), menu2[23][2][0].replace("\n", "/"),
      menu2[24][2][0].replace("\n", "/"), menu2[25][2][0].replace("\n", "/"), menu2[26][2][0].replace("\n", "/"),
      menu2[27][2][0].replace("\n", "/"), menu2[28][2][0].replace("\n", "/"), menu2[29][2][0].replace("\n", "/"),
      menu3[0][2][0].replace("\n", "/"), menu3[1][2][0].replace("\n", "/"), menu3[2][2][0].replace("\n", "/"),
      menu3[3][2][0].replace("\n", "/"), menu3[4][2][0].replace("\n", "/"), menu3[5][2][0].replace("\n", "/"),
      menu3[6][2][0].replace("\n", "/"), menu3[7][2][0].replace("\n", "/"), menu3[8][2][0].replace("\n", "/"),
      menu3[9][2][0].replace("\n", "/"), menu3[10][2][0].replace("\n", "/"), menu3[11][2][0].replace("\n", "/"),
      menu3[12][2][0].replace("\n", "/"), menu3[13][2][0].replace("\n", "/"), menu3[14][2][0].replace("\n", "/"),
      menu3[15][2][0].replace("\n", "/"), menu3[16][2][0].replace("\n", "/"), menu3[17][2][0].replace("\n", "/"),
      menu3[18][2][0].replace("\n", "/"), menu3[19][2][0].replace("\n", "/"), menu3[20][2][0].replace("\n", "/"),
      menu3[21][2][0].replace("\n", "/"), menu3[22][2][0].replace("\n", "/"), menu3[23][2][0].replace("\n", "/"),
      menu3[24][2][0].replace("\n", "/"), menu3[25][2][0].replace("\n", "/"), menu3[26][2][0].replace("\n", "/"),
      menu3[27][2][0].replace("\n", "/"), menu3[28][2][0].replace("\n", "/"), menu3[29][2][0].replace("\n", "/"))

    return HttpResponse(babmonth)


def info(request):  #inmagobab.ml/info로 접근해오면 information이라는 html을 출력한다.
    information = "<html><body><title>information</title>" \
                    '<div style="border:5px solid; padding:15px; background-color:black;">'\
                    '<h1 class="title"style = "color:white;font-size:40px;">&nbsp; 인마고 급식 알리미 B.A.B.</h1>'\
                    "</div>"\
                    '<p class = "source"' \
                    'style = "font-size:30px;color:Gray;text-align:left;margin-left: 1em;font-weight:bold"'\
                    'a:link {color:#007cd0;text-decoration:none}' \
                    'a:visited {color:#007cd0;text-decoration:none}' \
                    'a:active {color:#007cd0;text-decoration:none}'\
                    'a:hover {color:#0099ff;text-decoration:none}">' \
                    '<A href = "http://inmagobab.ml" style="text-decoration:none">메인화면</A>&nbsp; &nbsp; &nbsp;' \
                    '<A href = "source" style="text-decoration:none">출처</A>&nbsp; &nbsp; &nbsp;'\
                    '<A href = "info" style="text-decoration:none">개발정보</A>&nbsp; &nbsp; &nbsp;'\
                    '<A href = "month" style="text-decoration:none">이달의식단</A></br>'\
                    '<hr>' \
                    "<p style = font-size:20px;></br>&nbsp; &nbsp; 인천전자마이스터고등학교 급식 알리미입니다.</br></br>" \
                    "&nbsp; &nbsp; 학교 사정에 따라 메뉴는 변동될 수 있습니다.</br></br>"\
                    "&nbsp; &nbsp; 개발자 : 허성진, 김상철, 조승섭</p></body> </html>"

    return HttpResponse(information)


def source(request):
    source = "<html><body><title>source</title>" \
                '<div style="border:5px solid; padding:15px; background-color:black;">'\
                '<h1 class="title"style = "color:white;font-size:40px;">&nbsp; 인마고 급식 알리미 B.A.B.</h1>'\
                "</div>"\
                '<p class = "source"'\
                'style = "font-size:30px;color:Gray;text-align:left;margin-left: 1em;font-weight:bold"'\
                'a:link {color:#007cd0;text-decoration:none}' \
                'a:visited {color:#007cd0;text-decoration:none}' \
                'a:active {color:#007cd0;text-decoration:none}'\
                'a:hover {color:#0099ff;text-decoration:none}">' \
                '<A href = "http://inmagobab.ml" style="text-decoration:none">메인화면</A>&nbsp; &nbsp; &nbsp;' \
                '<A href = "source" style="text-decoration:none">출처</A>&nbsp; &nbsp; &nbsp;'\
                '<A href = "info" style="text-decoration:none">개발정보</A>&nbsp; &nbsp; &nbsp;'\
                '<A href = "month" style="text-decoration:none">이달의식단</A></br>'\
                '<hr>' \
                '&nbsp; &nbsp; &nbsp;' \
                '<A href = "http://intec.icehs.kr/boardCnts/list.do?boardID=12438&m=060403&s=intec#contents"' \
                'style="text-decoration:none">인천전자마이스터고등학교 - 급식실 - 이달의 식단</A></br>'\
                '</body> </html>'

    return HttpResponse(source)


# --------------------------------------------------------------------------------------------------------------
def keyboard(request):  # 카카오톡에서 /keyboard로 접근 시 '사용법' 버튼을 띄워준다.
    return JsonResponse(
        {
            'type': 'text',
            'buttons': ['사용법']
        }
    )

@csrf_exempt
def message(request):  # 카카오톡 사용자의 입력을 받아 /message로 접속해오면 버튼의 내용에 따라 다른 결과를 출력한다.
    json_str = ((request.body).decode('utf-8'))  # 바이트열로 받아온 입력값을 유니코드로 디코딩한다.
    received_json = json.loads(json_str)  # json형식의 입력값을 json.loads()함수를 이용하여 파이썬 형식으로 바꿔준다.
    content_name = received_json['content']  # 배열 형식의 received_json에서 content(입력값)을 content_name에 넣어준다.
    type_name = received_json['type']  # 배열에서 type을 추출해 사용자가 보낸 값의 속성을 구별한다.(text, photo등)

    if content_name == "오늘급식":  # 사용자가 '오늘급식'이라고 입력했을 경우
        todaybab = '%d월%d일의 급식입니다.\n\n조식 : \n%s\n\n중식 : \n%s\n\n석식: \n%s' % \
                   (today.month, today.day, menu1[today.day - 1][2][0], menu2[today.day - 1][2][0], menu3[today.day - 1][2][0])
        return JsonResponse(
            {
                'message': {
                    'text': todaybab
                },
            }
        )

    elif content_name == "내일급식":  # 사용자가 '내일급식'이라고 입력했을 경우
        tomorrowbab = '%d월%d일의 급식입니다.\n\n조식 : \n%s\n\n중식 : \n%s\n\n석식 : \n%s' % \
                      (today.month, tomorrow.day, menu1[tomorrow.day - 1][2][0], menu2[tomorrow.day - 1][2][0], menu3[tomorrow.day - 1][2][0])
        return JsonResponse(
            {
                'message': {
                    'text': tomorrowbab
                },
            }
        )

    elif content_name == '모레급식':  # 사용자가 '모레급식'이라고 입력했을 경우
        tdabab = '%d월%d일의 급식입니다.\n\n조식 : \n%s\n\n중식 : \n%s\n\n석식 : \n%s' % \
                 (today.month, tda.day, menu1[tda.day - 1][2][0], menu2[tda.day - 1][2][0], menu3[tda.day - 1][2][0])
        return JsonResponse(
            {
                'message': {
                    'text': tdabab
                },
            }
        )

    elif content_name == '사용법':  # 사용자가 '사용법'이라고 입력했을 경우
        helpbab = "명령어 : '오늘급식', '내일급식', '모레급식'"
        return JsonResponse(
            {
                'message': {
                    'text': helpbab
                },
            }
        )

    else:  # 오류 또는 사용자가 잘못된 값을 입력했을 경우
        mess = "오류 또는 잘못된 값을 입력하셨습니다."

        if type_name == 'photo':
            mess = "사진 기능은 제공하지 않습니다!"
        elif type_name == 'video':
            mess = "동영상 기능은 제공하지 않습니다!"
        elif type_name == 'audio':
            mess = "녹음파일 기능은 제공하지 않습니다!"
        return JsonResponse({
            'message': {
                'text': mess
            },
        })
