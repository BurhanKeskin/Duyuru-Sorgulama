from bs4 import BeautifulSoup
import requests

from datetime import date
import locale

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

TargerURL = "https://www.bilecik.edu.tr/main/arama/4"
request = requests.get(TargerURL)
Soup = BeautifulSoup(request.text, "html.parser")
AnnouncementCards = Soup.find_all('div', attrs={"class":"card-body p-2"})

for announcement in AnnouncementCards:

    announcementLink = "https://www.bilecik.edu.tr" + announcement.find('h6', {"class":"card-title"}).a['href']
    announcementTitle = announcement.find('h6', {"class":"card-title"}).a.text 
    announcementDate = announcement.find('small', {"class":"text-muted"}).text

    
    if(announcementDate.strip() == Date):
        AnnouncementTitles.append(announcementTitle)
        AnnouncementLinks.append(announcementLink)
    else:
        print("Bugün yayınlanan bir duyuru bulunamadı.")
        break    

for title,link in zip(AnnouncementTitles,AnnouncementLinks):
    print(title + "\n" + link + "\n")
    


