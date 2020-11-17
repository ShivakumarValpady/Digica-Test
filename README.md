# Digica-Test

1) Task 1 in python on Data Preprocessing is self explanatory.  

2) Task 2 - Flickr API, SQLite Database 

    * It consists of 3 files - Flickr_CLient.py, SQLite_Client.py, task.py. 
    * In Flickr_Client.py, a class with three functions are written. 
         * In the first function '__init__, variables and functions are initialised.  
         * In the second function 'download', if keyword is not given, 100 most recent urls are stored in a list. If Keyword is present, the url of that particular image is appended to the list. The function returns the list of the urls.  
         * In the third function 'retrieve', The name of image is appended with a number and the images are retrieved/downloaded with the new name. The function returns the name of the files. 
         
   * In SQLite_Client.py, a class with four functions are written. 
      * In the first function '__init__', variables and functions are initialised. 
      * In the second function 'createDatabase', it checks whether a connection to database is established or not, if not, it sends and error message. 
      * In the third function 'createTable', a sqlite table is created after establishing a connection to the database, or else an error message is displayed. 
      * In the fourth function 'insertBLOB', an image is stored in the table in the datatype 'BLOB'. The table contains the images. 
      
   * In task.py, 3 functions are written. 
      * All the necessary librarires and files are imported.
      * The first function reads the BLOB data and converts to binary data. 
      * In the second function 'task', the urls are stores and the images are downloaded. For each of the urls present, its image is converted to binary data, file name is changed by adding a number to keep track of it, dominant color of the image is found out, and the image(blob data) isinserted to table. 
      * In the third function 'getDominantColorClusters', the dominant colors of the image are returned in the form of an list of tuples. This is done using K means clustering, with 3 clusters.
      
      
#### NOTE #### : In the given time duration, I could complete only these tasks. A last portion is left remaining. 

#### TO-DO ####: The intensity values of the most dominant colors are returned for now. I had to filter out the images using the range of values for red color. Out of the obtained remaining images, I had to find out which image had the maximum intensity of red color value and return it.  This would have been my approach, if there was enough time left, like extra 30 mins. 

Thank you.
