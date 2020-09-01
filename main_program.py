import os, sys, time, threading, multiprocessing, shutil,cv2
from google_images_download import google_images_download


inputDirName='f:\\downloads\\garden'
outputDirName='f:\\output1'

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

# Check inputDirName directory exist or not
if os.path.exists(inputDirName) == False:
    print("!! Error: ", inputDirName, " directory doesn't exist")
    exit(0)



# to append images name in a list
files=[]
for r,d,f in os.walk(inputDirName):
    for file in f:
        if '.jpg' or '.jpeg' in file:
            files.append(os.path.join(r,file))


startTime=time.time()

activeThreads = threading.activeCount()
print("Active Threads = ",activeThreads)

numberOfCores=multiprocessing.cpu_count()
print("Number Of Cores = ",numberOfCores)

# Num of Threads per core.
# Eg. if core=4, then total threads = 8
N = 1
print("Number Of Threds per Cores = ",N,"\n")

count=1   
#Function to convert into B/W
def convert_to_bw(file_name):
    original_image=cv2.imread(file_name)
    grayFile=cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    global count
    name='f:/output1/frame'+str(count)+'.jpg'
    count=count+1
    cv2.imwrite(name,grayFile)


# Main Program
print("Program Started....")
i=1
for f in files:
    print ("File Processing %d (%s)"%(i,f))
    t = threading.Thread(target=convert_to_bw , args=(f,))
    t.start()
    i=i+1
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

#convert_to_bw(files[0])



