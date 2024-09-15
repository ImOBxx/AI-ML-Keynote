import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

name = "Abhishek Banerjee"
gender = "Male"
age = "25"  


font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.0  
font_thickness = 2
text_color = (0, 255, 0)  

while True:
    
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"Name: {name}", (x, y+h+30), font, font_scale, text_color, font_thickness)
        cv2.putText(frame, f"Gender: {gender}", (x, y+h+60), font, font_scale, text_color, font_thickness)
        cv2.putText(frame, f"Age: {age}", (x, y+h+90), font, font_scale, text_color, font_thickness)

    cv2.imshow('img', frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()















































































































