import os, sys, time, threading, multiprocessing, shutil,cv2
from google_images_download import google_images_download

def download_images(keyword,number):
    response = google_images_download.googleimagesdownload()   #class instantiation
    arguments = {"keywords":keyword,"limit":number}   #creating list of arguments
    paths = response.download(arguments)
    return;


startTime=time.time()

activeThreads = threading.activeCount()
print("Active Threads = ",activeThreads)

numberOfCores=multiprocessing.cpu_count()
print("Number Of Cores = ",numberOfCores)

N = 2
print("Number Of Threds per Cores = ",N,"\n")
print("Program Started....")

print("Enter the name:")
keyword=input()
print("Enter the number:")
number=input()
k=int(number)
for i in range(1,k+1):
    print ("File Processing %d "%(i))
    t = threading.Thread(target=download_images , args=(keyword,2,))
    t.start()
    while True:
        if threading.activeCount() - activeThreads + 1 <= N * numberOfCores:
            break
        time.sleep(1)

	
# Waiting to finish all Threads
while True:
    if threading.activeCount() == activeThreads:
        break
    else:
        print ("...Thread Left %d..."%(threading.activeCount() - activeThreads))
        time.sleep(1)
  
print("All Threads compeleted")
print("\nTotal Time %f sec"%(round(time.time() - startTime,4)))
print("Program Finished")