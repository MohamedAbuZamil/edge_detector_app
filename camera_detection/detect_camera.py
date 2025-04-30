import cv2

def find_working_camera(max_cameras=5):
   
    for camera_index in range(max_cameras):
        cap = cv2.VideoCapture(camera_index)
        if cap.isOpened():
            print(f"Found working camera : {camera_index}")
            return cap
        cap.release()
    print("No camera found.")
    return None
