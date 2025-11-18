import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            lm = face.landmark

            # Eyebrow landmark IDs
            left_eyebrow_point = lm[105]
            right_eyebrow_point = lm[334]

            # Convert to pixel coordinates
            mid_x = int((left_eyebrow_point.x + right_eyebrow_point.x) / 2 * frame.shape[1])
            mid_y = int((left_eyebrow_point.y + right_eyebrow_point.y) / 2 * frame.shape[0])
         

            # Draw red dot only
            cv2.circle(frame, (mid_x, mid_y), 6, (0, 0, 255), -1)

    cv2.imshow("Eyebrow Dot", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()