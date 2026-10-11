import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("error:Face detecion model not loaded!")
    exit()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


if not cap.isOpened():
    print("Error: Camera not opened!")
    exit()


mode = 1

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot read frame!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    edges = cv2.Canny(gray, 100, 200)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        mode = 1
    elif key == ord('2'):
        mode = 2
    elif key == ord('3'):
        mode = 3
    elif key == ord('4'):
        mode = 4
    elif key == ord('5'):
        mode = 5

    if mode == 1:
        display = frame.copy()
    elif mode == 2:
        display = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    elif mode == 3:
        display = blur.copy()
    elif mode == 4:
        display = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif mode == 5:
        display = frame.copy()
            cv2.putText(display, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    cv2.putText(display, "1: Original  2: Grayscale", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(display, "3: Blur  4: Edges  5: Face Detection", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(display, "S: Save  Q: Exit", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Image Processing Studio", display)

    if key == ord('s'):
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved successfully!")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Program closed successfully!")
