from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import requests
import os
import re

img_path = "OIP.jpg"

def print_to_window(img_path):
    if os.name == 'nt':
        print(os.getcwd())
        print(img_path)
        os.startfile(img_path)

def add_text_to_image(img_path):
        image = Image.open(img_path)
        
        # Create a Draw object
        draw = ImageDraw.Draw(image)

        font_path = "C:\\Windows\\Fonts\\arial.ttf"
        font_size = 20
        font = ImageFont.truetype(font_path, font_size)

        # Positioning the text
        text_position = (50, 30)

        # Draw the text
        draw.text(text_position, "New Grad Role Released!", fill="black", font=font)

        # Save the modified image
        image.save("new_grad.jpg")

def main():
    r = requests.get("https://job-boards.greenhouse.io/vannevarlabs")
    print('request code ' + str(r.status_code))
    soup = BeautifulSoup(r.text, "html.parser")
    
    curr_openings = soup.find_all('p', class_='body body--medium')

    for job in curr_openings:
        job = job.get_text().lower()
        print(job)

        if  re.search(r'$new grad$', str(job)):
            add_text_to_image(img_path)
            print_to_window("new_grad.jpg")
        else:
            print('no new grad roles found')

if __name__ == "__main__":
    main()
