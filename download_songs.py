#!/usr/bin/python3

from bs4 import BeautifulSoup
import subprocess
import os

"""
  TODO: Make this code work for Revival album - which could be a category for some sort

"""


def download_songs(link, album):
  os.mkdir(album)
  html = subprocess.run(['curl', '-s', link], stdout = subprocess.PIPE, encoding = 'utf-8')
  html_content = html.stdout
  with open('links.html', 'w') as f:
    f.write(html_content)
  f.close()
  
  with open('links.html', 'r') as f:
    html_doc = f.read()
    
  soup = BeautifulSoup(html_doc, 'html.parser')
  new_ol = [ol for ol in soup.find_all('ol')]
  new_ol = str(new_ol[0])
  ol_soup = BeautifulSoup(new_ol, 'html.parser')

  with open('links.txt', 'w') as f:
    for li in ol_soup.find_all('a', href = True):
      f.write(str(li['href']))
      f.write('\n')
    f.close()
    
  os.remove('links.html')
  os.chdir(album)
  subprocess.run(['wget', '-i', '../links.txt'])
  os.remove('../links.txt')
  
  
if __name__ == "__main__":
  link = input('Enter the album link : ')
  album = input('Enter Album Name : ')
  download_songs(link, album)
