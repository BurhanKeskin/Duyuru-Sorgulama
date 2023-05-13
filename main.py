from bs4 import BeautifulSoup
import requests

from datetime import date
import locale

# Yerel zaman dilimini Türkiye için ayarladım
# I've set the local time zone for Turkey
locale.setlocale(locale.LC_TIME, "tr_TR")

# Bugünün tarihini değişkene atadım.
# I've assigned the today's date into the variable 
currentDate = date.today().strftime("%d %B %Y")
# ayrıca bugünü kelime olarakta değişkene atadım.
# also I've assigned the today into the variable as string
currentDay = date.today().strftime("%A")




print(f"{currentDate} {currentDay}")

AnnouncementLinks = []
AnnouncementTitles = []


