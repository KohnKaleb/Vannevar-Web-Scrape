# Vannevar-Web-Scrape

### The progam scrapes the Vannevar Labs job listing on greenhouse and prints a picture of the Vannevar Logo with text letting me know to apply when a new grad role has been posted. I have the task scheduled to run every couple hours so the website is scraped a few times a day.

# requirements
 - make sure to pip install any required modules such as Pillow, BeautifulSoup or Requests (ex. pip install requests)
 - run the program by nagivating into the root directory and running 'python main.py'
 - This program requires a Windows Operating system to correctly function

# Tips
 - I used the Task Scheduler on Windows to run the task at whatever frequency that is desired
 - to generate a executable file out of your main.py file you can run the following commands:
    1. pip install pyinstaller
    2. pyinstaller --onefile main.py
