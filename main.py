import cv2 as cv
from processing_display_image import process_img, display_video_frame # Adds blurs to image, past library
from circles import * # Past libraries to detect and draw circles



if __name__ == "__main__":
    # Take Video
    capture = cv.VideoCapture("movingCan.mov")
    while True:
        # Process it frame by frame
        frame_exist, img = capture.read()

        if frame_exist: # Prevents code from crashing
            # Processing img, draws circles, displays image
            gray_img = process_img(img)
            circles = detect_circles(gray_img)
            img = draw_circle(img, circles)
            display_video_frame(img, "Video with Circles")
        else:
            break
    # Close the window
    capture.release()

    # De-allocate any associated memory usage
    cv.destroyAllWindows()