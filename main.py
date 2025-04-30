import cv2
from camera_detection.detect_camera import find_working_camera
from edge_detector.edge_detector_app import EdgeDetectorApp

def main():
    cap = find_working_camera()

    if cap is None:
        print("No available camera detected. Exiting...")
        return

    app = EdgeDetectorApp(cap)

    while True:
        ret, frame = app.cap.read()
        if not ret:
            break

        filtered = app.apply_filters(frame)
        cv2.imshow('Edge Detector', filtered)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('o'):
            app.mode = 'original'
        elif key == ord('x'):
            app.mode = 'sobel_x'
        elif key == ord('y'):
            app.mode = 'sobel_y'
        elif key == ord('m'):
            app.mode = 'magnitude'
        elif key == ord('s'):
            app.mode = 'sobel_threshold'
        elif key == ord('l'):
            app.mode = 'laplacian'
        elif key == ord('+'):
            app.sigma += 0.5
        elif key == ord('-'):
            app.sigma = max(0.5, app.sigma - 0.5)

    app.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
