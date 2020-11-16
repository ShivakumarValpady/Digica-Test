import flickrapi
import urllib.request
import uuid
import sqlite3


class FlickrClient:

 	def __init__(self,key,secret):
 		self.key = key
 		self.secret = secret
 		self.flickr=flickrapi.FlickrAPI(key, secret, cache=True)

 	def download(self,keyword="",count=100):
 		per_page = min(500,count)
 		page = count/500
 		sortbasedOn = "date-posted-desc"
 		if keyword:
 			sortbasedOn = "relevance"
 		photos = self.flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=per_page,  
                     sort=sortbasedOn)

 		urls = []
 		for i, photo in enumerate(photos):
 			url = photo.get('url_c')
 			urls.append(url)
 			if i > count:
 				break
 		
 		return urls

 	def retreive(self,urls):
 		name = uuid.uuid4().hex
 		for i,url in enumerate(urls):
 			if url:
	 			fileName = name+str(i)+'.jpg'
	 			print(fileName,url)
	 			urllib.request.urlretrieve(url, fileName)
 		return name