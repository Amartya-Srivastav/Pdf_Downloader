# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.tutorialspoint.com/python3/python_tutorial.pdf"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# links = soup.find_all('a')
#
# i = 0
# for link in links:
#     if '.pdf' in link.get('href', []):
#         i += 1
#         print("Downloading file: ", i)
#         response = requests.get(link.get('href'))
#         pdf = open("pdf" + str(i) + ".pdf", 'wb')
#         pdf.write(response.content)
#         pdf.close()
#         print("File ", i, " downloaded")
#
# print("All PDF files downloaded")

import os
import requests

urls = ["https://www.tutorialspoint.com/python3/python_tutorial.pdf"]

output = "E:\\DOWNLOADS"
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(output, os.path.basename(url))
        with open(file_path, 'wb') as f:
            f.write(response.content)



