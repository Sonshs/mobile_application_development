
## EX1
# Thai Do Anh Son
# 1620056
#

-------------------------------------------

This Ex1 uses Python3 language and includes 2 part:
	+ Part 1: "quest1.py"
	+ Part 2: "quest2.py"

- In "quest1.py", we enter 1 coordinate then the App will send the request to Google and return the
address of that coordinate in Vietnamese. 
	+ When the App runs, it will ask you enter 2 value of the coordinate is "latitude" and "longitude" 
	as float type.
	+ If the coordinate is correct, the App will returns the address in Vietnamese.

- In "quest2.py", we use an url with 2 parameters included.
Parameters:
	+ Name of 2 parameter as order is "latlng1" and "latlng2".
	+ The first parameter is the coordinate of first place, and the second is the coordinate of second 
	place.
	+ Each parameter is a string. That string includes 2 value latitude and longitude separated by 
	a colon. Ex: "10.22,40.4123"
Data:
	+ From 2 parameter we get 4 values of 2 coordinates. 
	Follow https://www.movable-type.co.uk/scripts/latlong.html we can calculate the distance of 2 place.
	+ The data will be saved as Json and will be return when website using GET with these parameters.
Example:
	+ The coordinate of Ha Noi is: 21.0031177,105.8201408
	+ The coordinate of Ho Chi Minh is: 21.0031177,105.8201408
	+ The distance between 2 coordinates is: 1144097.1094376913
	
If the homepage is: http://127.0.0.1:5000 so we have the example link as follow:
http://127.0.0.1:5000/distance?latlng1=21.0031177,105.8201408&latlng2=10.746903,106.676292
	
	