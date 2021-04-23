import cv2
import boto3
import webbrowser
cap = cv2.VideoCapture(0)
ret,photo = cap.read()
cv2.imwrite("hritik.jpg",photo)
cap.release()
myphoto = "hritik.jpg"
s3= boto3.resource('s3')
bucket = "myai888"
s3.Bucket(bucket).upload_file(myphoto,"file.jpg")
rek = boto3.client('rekognition')
region = "us-east-1"
upimage='file.jpg'
rek = boto3.client('rekognition',region)
response = rek.detect_faces(
    
   Image = { 
      'S3Object': { 
         'Bucket': bucket,
         'Name': upimage,
      }
   },
    Attributes=['ALL']
)
print(response)
if response['FaceDetails'][0]['Smile']['Value']==False:
    webbrowser.open("https://www.youtube.com/watch?v=p-eS-_olx9M")
else:
    print("You are in good mood")