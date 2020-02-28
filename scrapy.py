from bs4 import  BeautifulSoup
import requests
import csv
source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source  , 'lxml')
csv_file= open('mohasin.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video-link'])
for article in soup.find_all('article') :

      headLine = article.h2.a.test
      print(headLine)
      summary =article.find('div',class_='entry-content').p
      print(summary)


      #print(vidId)



      try:
            vid_src = article.find('iframe', class_='youtube-player')['src']
            print(vid_src)

            vidId = vid_src.split('/')[4]
            vidId = vidId.split('?')[0]
            yt_link = 'https://youtube.com/watch?v={}'.format(vidId)
      except Exception as e :
            yt_link= None
      print(print(yt_link))
      print()
      csv_writer.writerow([headLine,summary,yt_link])
csv_file.close()
