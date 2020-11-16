import sys
from SQLite_Client import SqliteClient
from Flickr_Client import FlickrClient

import matplotlib.image as img 
import matplotlib.pyplot as plt 
from scipy.cluster.vq import whiten 
from scipy.cluster.vq import kmeans 
import pandas as pd 

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def task(keyword,count):
	key = "1326c2f1c67fe0ad5efb8389c7e9e588"
	secret = "41c46f9dd96e76f2"
	flickrClient = FlickrClient(key,secret)
	sqliteClient = SqliteClient(dbName = "ImageStore")
	urls = []
	urls = flickrClient.download(keyword,count)
	startString = flickrClient.retreive(urls)

	for i in range(len(urls)):
		fileName = startString+str(i)+'.jpg'
		blob = convertToBinaryData(fileName)
		dominant_colors = getDominantColorClusters(fileName)
		sqliteClient.insertBLOB(blob)


def getDominantColorClusters(file):

	input_image = img.imread(file)
	r = [] 
	g = [] 
	b = [] 
	for row in input_image: 
	    for temp_r, temp_g, temp_b in row: 
	        r.append(temp_r) 
	        g.append(temp_g) 
	        b.append(temp_b) 
	   
	batman_df = pd.DataFrame({'red' : r, 
	                          'green' : g, 
	                          'blue' : b}) 
	  
	batman_df['scaled_color_red'] = whiten(batman_df['red']) 
	batman_df['scaled_color_blue'] = whiten(batman_df['blue']) 
	batman_df['scaled_color_green'] = whiten(batman_df['green']) 
	  
	cluster_centers, _ = kmeans(batman_df[['scaled_color_red', 
	                                    'scaled_color_blue', 
	                                    'scaled_color_green']], 3) 
	  
	dominant_colors = [] 
	  
	red_std, green_std, blue_std = batman_df[['red', 
	                                          'green', 
	                                          'blue']].std() 
	  
	for cluster_center in cluster_centers: 
	    red_scaled, green_scaled, blue_scaled = cluster_center 
	    dominant_colors.append(( 
	        red_scaled * red_std / 255, 
	        green_scaled * green_std / 255, 
	        blue_scaled * blue_std / 255
	    )) 
	  
	print(dominant_colors)
	# To visualize the dominant colors in the image
	# plt.imshow([dominant_colors]) 
	# plt.show()
	return dominant_colors


if __name__ == '__main__':

	keyword = ""
	count = 100
	if len(sys.argv)>=2:
		keyword = sys.argv[1]
		count = int(sys.argv[2])

	task(keyword,count)


	
