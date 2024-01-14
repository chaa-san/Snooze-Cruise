from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import pygame
pygame.mixer.init()

# Load the sound file
sound_file = "small_sound.mp3"
sound = pygame.mixer.Sound(sound_file)

from twilio.rest import Client

# Your Twilio Account SID, Auth Token, and Twilio Phone Number
account_sid = 'AC499c160c9c7854228cf56a804159bc7b'
auth_token = '88806e101a314a3dad957cfc2d00318d'
twilio_phone_number = '+15488811834'

# The number you want to call
#to_phone_number = '+14372544148'
to_phone_number = '+15488811834'

# Create a Twilio client
client = Client(account_sid, auth_token)




def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear
	
thresh = 0.25
frame_check = 40
sleep_check = 100
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag=0
while True:
	ret, frame=cap.read()
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	subjects = detect(gray, 0)
	for subject in subjects:
		shape = predict(gray, subject)
		shape = face_utils.shape_to_np(shape)#converting to NumPy Array
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		ear = (leftEAR + rightEAR) / 2.0
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
		if ear < thresh:
			flag += 1
			print (flag)
			if flag >= frame_check:
				cv2.putText(frame, "****************ALERT!****************", (10, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				cv2.putText(frame, "****************ALERT!****************", (10,325),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				# Play the sound
				sound.play()
				#print ("Drowsy")

			if flag >= sleep_check:
				# Call Emergency
				# Make a phone call
				call = client.calls.create(
					to=to_phone_number,
					from_=twilio_phone_number,
					url='http://demo.twilio.com/docs/voice.xml'  
					# A URL with TwiML instructions (replace with your own instructions)
				)

				print(f"Call SID: {call.sid}")
		
		else:
			flag = 0
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
cv2.destroyAllWindows()
cap.release() 
