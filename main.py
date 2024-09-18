from bs4 import BeautifulSoup
import requests
import re

def print_message_to_window():
    pass

def main():
    r = requests.get("https://job-boards.greenhouse.io/vannevarlabs")
    print('request code ' + str(r.status_code))
    soup = BeautifulSoup(r.text, "html.parser")
    
    curr_openings = soup.find_all('p', class_='body body--medium')

    for job in curr_openings:
        job = job.get_text().lower()

        if  re.search(r'$new grad$', str(job)):
            print_message_to_window()
        else:
            print('no new grad roles found')

if __name__ == "__main__":
    main()
