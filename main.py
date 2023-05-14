from keep_alive import keep_alive

from bs4 import BeautifulSoup
import requests

from datetime import date
import locale
import time

# Yerel zaman dilimini Türkiye için ayarladım
# I've set the local time zone for Turkey
locale.setlocale(locale.LC_TIME, "tr_TR")

# Bugünün tarihini değişkene atadım.
# I've assigned the today's date into the variable 
currentDate = date.today().strftime("%d.%B.%Y")
# ayrıca bugünü kelime olarakta değişkene atadım.
# also I've assigned the today into the variable as string
currentDay = date.today().strftime("%A")

Date = currentDate + " " + currentDay
Date1 = "12.05.2023 Cuma"

AnnouncementLinks = []
AnnouncementTitles = []

SendedAnnouncementLinks = []
SendedAnnouncementTitles = []

TargerURL = "https://www.bilecik.edu.tr/main/arama/4"
request = requests.get(TargerURL)
Soup = BeautifulSoup(request.text, "html.parser")
AnnouncementCards = Soup.find_all('div', attrs={"class":"card-body p-2"})

while True:

    for announcement in AnnouncementCards:

        announcementLink = "https://www.bilecik.edu.tr" + announcement.find('h6', {"class":"card-title"}).a['href']
        announcementTitle = announcement.find('h6', {"class":"card-title"}).a.text 
        announcementDate = announcement.find('small', {"class":"text-muted"}).text

        if(announcementDate.strip() == Date1):
            if((announcementTitle not in AnnouncementTitles) and (announcementLink not in AnnouncementLinks)):
                AnnouncementTitles.append(announcementTitle)
                AnnouncementLinks.append(announcementLink)
        else:
            break  

    for title,link in zip(AnnouncementTitles, AnnouncementLinks):

        if((title not in SendedAnnouncementTitles) and (link not in SendedAnnouncementLinks)):
            print(title + "\n" + link + "\n")
            SendedAnnouncementTitles.append(title)
            SendedAnnouncementLinks.append(link)
            
    time.sleep(10)         
    

    


