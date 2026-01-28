import cv2
import time

face_cascade = cv2.CascadeClassifier('face cascade.xml')
eye_cascade = cv2.CascadeClassifier('eye cascade.xml')

cap = cv2.VideoCapture(0)

focus_time = 0
distract_time = 0

start_time = time.time()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            if len(eyes) >= 1:
                focus_time += 1
                status = "Focused"
            else:
                distract_time += 1
                status = "Distracted"
            
            cv2.putText(frame, status, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('Smart Study Focus Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

end_time = time.time()
total_time = int(end_time - start_time)

cap.release()
cv2.destroyAllWindows()

print("\nStudy Session Report")
print("Total Time (seconds):", total_time)
print("Focus Time (frames):", focus_time)
print("Distraction Time (frames):", distract_time)

focus_percentage = (focus_time / (focus_time + distract_time)) * 100
print("Focus Percentage:", round(focus_percentage,2), "%")
