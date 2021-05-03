from requests_html import HTMLSession #used to grab url and parse html 
from bs4 import BeautifulSoup
from tkinter import Label #allows us to control the GUI in terms of text and positioning of elements
from tkinter import Tk 
from PIL import ImageTk, Image

requests = HTMLSession() # allows us to parse through html

#function that fetches the weather information from the queried url
def weatherStatus(): 
    
    weatherType = soup.find('div', class_="wob_dcp").text #find the specified div and class and save the text to the waetherType variable
    location = soup.find('div',class_="wob_loc mfMhoc").text #find the specified div and class and save the text to the location variable
    temp = soup.find('span', class_="wob_t TVtOme").text+'°F' #find the specified span and class and save the text to the temp variable
    time = soup.find('div', class_="wob_dts").text  #find the specified span and class and save the text to the temp variable
    
    locationTypography.config(text=location) #Populates locaton element on gui
    tempTypography.config(text=temp) #Populates temperature element on gui
    weatherTypeLabel.config(text=weatherType) #Populates weathertpe element on gui
    timelabel.config(text=time) #Populates time elementon gui

    tempTypography.after(120000,weatherStatus)#updates the weather inforamtion every 2 minutes
    timelabel.after(900000,weatherStatus)#looks to update the time inforamtion every 15 minutes 
    master.update()

locationInput_town= input('Enter City: ') # user inputs City
locationInput_State= input('Enter State: ') # user inputs State
locationInput_country= input('Enter Country: ') # user inputs State
url = "https://www.google.com/search?q="+locationInput_town+'+'+locationInput_State+'+'+locationInput_country+'+'+"weather" #url for search query
page =requests.get(url) #fetch html page to parse
soup =BeautifulSoup(page.content, "html.parser") #html page to parse through
weatherType2 = soup.find('div', class_="wob_dcp").text
## GUI is created to display the weather
master = Tk()
master.title("Weather App")
master.config(bg = "white")

## weather image/icon are saved on a local drive and are used based on weather type 
partlycloudy= Image.open("C:/Users/rv239/Desktop/ITI/Spring 2021/OOP Projects/Final Project/partlycloudy.png") # open weather image from specific location on local drive
partlycloudy= partlycloudy.resize((135,135)) #adjust the weather image size
partlycloudy= ImageTk.PhotoImage(partlycloudy) 

cloudy= Image.open("C:/Users/rv239/Desktop/ITI/Spring 2021/OOP Projects/Final Project/cloudy.jpg") # open weather image from specific location on local drive
cloudy= cloudy.resize((135,150)) #adjust the weather image size
cloudy= ImageTk.PhotoImage(cloudy) 

rain= Image.open("C:/Users/rv239/Desktop/ITI/Spring 2021/OOP Projects/Final Project/rain.jpg") # open weather image from specific location on local drive
rain= rain.resize((135,135)) #adjust the weather image size
rain= ImageTk.PhotoImage(rain) 

snow= Image.open("C:/Users/rv239/Desktop/ITI/Spring 2021/OOP Projects/Final Project/snow.png") # open weather image from specific location on local drive
snow= snow.resize((135,135)) #adjust the weather image size
snow= ImageTk.PhotoImage(snow) 

Sunny= Image.open("C:/Users/rv239/Desktop/ITI/Spring 2021/OOP Projects/Final Project/Sunny.jpg") # open weather image from specific location on local drive
Sunny= Sunny.resize((135,135)) #adjust the weather image size
Sunny= ImageTk.PhotoImage(Sunny) 

windy= Image.open("C:/Users/rv239/Desktop/ITI/Spring 2021/OOP Projects/Final Project/windy.jpg") # open weather image from specific location on local drive
windy= windy.resize((135,135)) #adjust the weather image size
windy= ImageTk.PhotoImage(windy) 

#Location design
locationTypography = Label(master, font=("Calibri bold",20),bg ="white") # text design bg=background
locationTypography.grid(row=0, sticky = "N", padx=100) #location on the Guiin a table like foramt, sticky = compass direction of widget 
#times design
timelabel = Label(master, font = ("Calibri", 11),bg = "white") # text design 
timelabel.grid(row=1,sticky="N", padx = 20) #location on the Gui 
#temperature design
tempTypography = Label(master, font = ("Calibri bold", 50),bg = "white") # text design 
tempTypography.grid(row=1,sticky="W", padx = 20) #location on the Gui 

#image design depends on type of weather
if weatherType2 == 'Sunny':
    Label(master, image=Sunny,bg="white").grid(row=1,sticky="E") # insert the image of the weather icon on the east side
elif weatherType2 =='Windy':
    Label(master, image=windy,bg="white").grid(row=1,sticky="E") # insert the image of the weather icon on the east side
elif weatherType2 =='Cloudy':
    Label(master, image=cloudy,bg="white").grid(row=1,sticky="E") # insert the image of the weather icon on the east side
elif weatherType2 =='Partly Cloudy':
    Label(master, image=partlycloudy,bg="white").grid(row=1,sticky="E") # insert the image of the weather icon on the east side
elif weatherType2 =='Snow':
    Label(master, image=snow,bg="white").grid(row=1,sticky="E") # insert the image of the weather icon on the east side
else:
    Label(master, image=rain,bg="white").grid(row=1,sticky="E") # insert the image of the weather icon on the east side



#weather type design
weatherTypeLabel = Label(master, font=("Calibri bold", 15),bg="white") # text design 
weatherTypeLabel.grid(row = 1, sticky = "SW", padx= 40) #location on the Gui
weatherStatus() #calls funtion
master.mainloop()

