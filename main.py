from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\Web Development\Corona Notification\icon.ico",
        timeout = 30
    )

def getData(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    # notifyMe("Sharmaji", "Lets stop the spread of this virus together")
    myHtmlData = getData("https://www.mohfw.gov.in/")

    
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())
    myDataStr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]

    itemList = myDataStr.split("\n\n")

    states = ['Uttar Pradesh']
    for item in itemList[0:35]:
        dataList = item.split('\n')
        if dataList[1] in states:
            print(dataList) 
            nTitle = "Cases of COVID-19"
            nText = f"{dataList[1]}: Active: {dataList[2]}\n Cured: {dataList[3]}\n Deaths: {dataList[4]}\n Total Confirmed: {dataList[5]}"
            notifyMe(nTitle, nText)
            time.sleep(5)