import pyrealsense2 as rs
import cv2
import numpy as np

print("Bypassing LeRobot: Testing pure Intel drivers...")
pipeline = rs.pipeline()
config = rs.config()
config.enable_device("841512070981")
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)

try:
    pipeline.start(config)
    print("Pipeline started! Press 'q' to quit.")
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())
        cv2.imshow('Pure RealSense Test', color_image)

        if cv2.waitKey(1) == ord('q'):
            break
finally:
    pipeline.stop()
    cv2.destroyAllWindows()