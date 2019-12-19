import requests
import re
import pandas as pd
from bs4 import BeautifulSoup




#loading  data frames
sa_trending = pd.read_csv('saudi_youtube_trending_videos.csv',index_col=0)
kw_trending = pd.read_csv('kuwait_youtube_trending_videos.csv',index_col=0)
bh_trending = pd.read_csv('bahrain_youtube_trending_videos.csv',index_col=0)
om_trending = pd.read_csv('oman_youtube_trending_videos.csv',index_col=0)
ua_trending = pd.read_csv('emirates_youtube_trending_videos.csv',index_col=0)
qa_trending = pd.read_csv('qatar_youtube_trending_videos.csv',index_col=0)



# afunction to fitch video category
def get_category(herf):
    
    youtube = "https://www.youtube.com"
    page = requests.get(youtube+herf)
    sub_soup = BeautifulSoup(page.text, 'html.parser')
    div = sub_soup.find('meta',attrs={'itemprop':'genre'})
    return div.attrs['content']




    
def get_data(df,url):

#request the webpage
    response = requests.get(url)

#html perser                                                                                                                                               
    soup = BeautifulSoup(response.text, 'html.parser')

#getting all videos divs
    div = soup.find_all('div',class_= "yt-lockup-content")


    i = df.shape[0]
    for raw in div:
        #checking that the vidoe is not alredy in the dataframe
        video_id = raw.a.attrs['href'].split('=')[1]
        if len(df[df['video_id'].str.contains(video_id)]) == 0 and len(raw.li.find_next_sibling('li').text.split(' ')) < 3:
    
            #add video id
            df.loc[i,'video_id'] = video_id
       
            #fitching and adding vidoe name
            df.loc[i,'video_name'] = raw.a.attrs['title']
        
            #fitching and adding channel name,
            df.loc[i,'channel_name'] = raw.find('a',class_="yt-uix-sessionlink spf-link").text

            #fitching and adding duration of vidoe
            df.loc[i,'duration'] = int(raw.span.text.split(':')[1])
    
            #fitching and adding number of views
            
            df.loc[i,'views'] = int(raw.li.find_next_sibling('li').text.split(' ')[0].replace(',',''))

            #fitching category of a video
            df.loc[i,'category'] = get_category(raw.a.attrs['href'])
        
            i = i+1
   
        #just updated number of views in vidoe in dataframe
        elif  len(df[df['video_id'].str.contains(video_id)]) > 0:
            df.loc[df['video_id'] == video_id,'views']= int(raw.li.find_next_sibling('li').text.split(' ')[0].replace(',',''))    
  


    return df






#the main job of the program "SCRAPING YOUTUBE DATA"
sa_trending = get_data(sa_trending,'https://www.youtube.com.sa/feed/trending')
kw_trending = get_data(kw_trending,'https://www.youtube.com.kw/feed/trending')
bh_trending = get_data(bh_trending,'https://www.youtube.com.bh/feed/trending')
om_trending = get_data(om_trending,'https://www.youtube.com.om/feed/trending')
ua_trending = get_data(ua_trending,'https://www.youtube.com/feed/trending?gl=AE')
qa_trending = get_data(qa_trending,'https://www.youtube.com.qa/feed/trending')






# save dataframes
sa_trending.to_csv('saudi_youtube_trending_videos.csv')
kw_trending.to_csv('kuwait_youtube_trending_videos.csv')
bh_trending.to_csv('bahrain_youtube_trending_videos.csv')
om_trending.to_csv('oman_youtube_trending_videos.csv')
ua_trending.to_csv('emirates_youtube_trending_videos.csv')
qa_trending.to_csv('qatar_youtube_trending_videos.csv')
