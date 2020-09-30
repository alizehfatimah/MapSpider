# MapSpider
Bot created using Python BeautifulSoup to retrieve map images for different selected values.

The client requested to create a bot which could be used to download images from a given URL for different input values on the page. The spider was built for an Ubuntu system, version 18.04 bionic. 

How to use:
1)	Open terminal, update python version to 3.8:
sudo apt install python3.8
2)	Install necessary libraries
sudo apt-get install python-urllib3
sudo apt-get install python3-bs4
3)	Change directory to working folder and run following command:
python mapspider.py
4)	Image will be in the working folder (the folder where the .py file is)

Note: 
Python urllib and urllib2 libraries are not available for this version of Ubuntu, so urllib3 had to be used. 

