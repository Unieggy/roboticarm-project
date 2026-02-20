import cv2
from lerobot.cameras.realsense.configuration_realsense import RealSenseCameraConfig
from lerobot.cameras.realsense.camera_realsense import RealSenseCamera
from lerobot.cameras.configs import ColorMode, Cv2Rotation

def main():
    print("Initializing RealSense camera...")
    
    # Configure the camera settings
    # NOTE: Replace "YOUR_SERIAL_NUMBER" with the output from `lerobot-find-cameras realsense`
    config = RealSenseCameraConfig(
        serial_number_or_name="841512070981",
        fps=30,
        width=640,
        height=480,
        color_mode=ColorMode.RGB,
        use_depth=False, 
        rotation=Cv2Rotation.NO_ROTATION
    )

    # Instantiate and connect the camera
    camera = RealSenseCamera(config)
    camera.connect()
    
    print("Camera connected! Select the video window and press 'q' to quit.")

    try:
        while True:
            # Capture the live frame
            frame = camera.read()
            
            # LeRobot captures in RGB, but OpenCV displays in BGR format
            display_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Show the frame in a window
            cv2.imshow("Mike's RealSense Test", display_frame)
            
            # Wait 1ms and check if the user pressed 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Closing camera feed...")
                break
                
    finally:
        # Safely disconnect hardware and close windows
        camera.disconnect()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()