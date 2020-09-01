import os, sys, time, threading, multiprocessing, shutil,cv2
from google_images_download import google_images_download

startTime=time.time()
def download_images(keyword,number):
    response = google_images_download.googleimagesdownload()   #class instantiation
    arguments = {"keywords":keyword,"limit":number}   #creating list of arguments
    paths = response.download(arguments)
    return;

print("Enter the name:")
keyword=input()
print("Enter the number:")
number=input()
download_images(keyword,number)
print("\nTotal Time %f sec"%(round(time.time() - startTime,4)))
print("Program Finished")