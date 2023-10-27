import os
import phonenumbers
from phonenumbers import geocoder

os.system("clear")
os.system("pkg install figlet")
os.system("pkg install ruby")
os.system("pkg install gem")
os.system("gem install lolcat")

os.system("clear")

os.system("figlet number|lolcat")
os.system("figlet Track |lolcat")
print ("\033[1;37m________________________________________")
print ("\033[1;31m   Tool by-:")
print ("\033[1;36m      Termux hacking") 
print ("\033[1;37m________________________________________")
print ("")
number = input("\033[1;31m[*]\033[1;33mEnter Your  phone number \033[1;31m 》》\033[1;34m:")


check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number, " : ", number_location)


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print ("")
print ("\033[1;31m[*]\033[1;33mService provider : ",carrier.name_for_number(service_provider, "en"))
