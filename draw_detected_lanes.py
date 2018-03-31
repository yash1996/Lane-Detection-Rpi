import sys
import numpy as np
import cv2
from keras.models import load_model
# Load Keras model
import picamera
from picamera.array import PiRGBArray
import numpy as np
import cv2
model = load_model('full_CNN_model.h5')
image_size=(320, 192)
camera = picamera.PiCamera()
camera.resolution = image_size
camera.framerate = 7 
camera.vflip = False
camera.hflip = False
rawCapture = PiRGBArray(camera, size=image_size)
#importing some useful packages
time.sleep(0.1)

# Class to average lanes with
class Lanes():
    def __init__(self):
        self.recent_fit = []
        self.avg_fit = []

def road_lines(image):
    """ Takes in a road image, re-sizes for the model,
    predicts the lane to be drawn from the model in G color,
    recreates an RGB image of a lane and merges with the
    original road image.
    """
    # Get image ready for feeding into models
    small_img = imresize(image, (80, 160, 3))
    small_img = np.array(small_img)
    small_img = small_img[None,:,:,:]

    # Make prediction with neural network (un-normalize value by multiplying by 255)
    prediction = model.predict(small_img)[0] * 255

    # Add lane prediction to list for averaging
    lanes.recent_fit.append(prediction)
    # Only using last five for average
    if len(lanes.recent_fit) > 5:
        lanes.recent_fit = lanes.recent_fit[1:]

    # Calculate average detection
    lanes.avg_fit = np.mean(np.array([i for i in lanes.recent_fit]), axis = 0)

    # Generate fake R & B color dimensions, stack with G
    blanks = np.zeros_like(lanes.avg_fit).astype(np.uint8)
    lane_drawn = np.dstack((blanks, lanes.avg_fit, blanks))

    # Re-size to match the original image
    lane_image = imresize(lane_drawn, (720, 1280, 3))

    # Merge the lane drawing onto the original image
    result = cv2.addWeighted(image, 1, lane_image, 1, 0)

    return result

lanes = Lanes()

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        img = road_lines(image)
        # show the frame
        #lines.project_on_road_debug(image)
        cv2.imshow("Rpi lane detection", lines.project_on_road_debug(image))
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate()
        rawCapture.seek(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break