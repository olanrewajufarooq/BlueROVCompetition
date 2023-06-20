

#!/usr/bin/env python3
import cv2
import numpy as np

def pose_estimation(frame, matrix_coefficients, distortion_coefficients):
    pose = {}
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_100)
    aruco_params = cv2.aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame,
        aruco_dict,
        parameters=aruco_params,
        cameraMatrix=matrix_coefficients,
        distCoeff=distortion_coefficients)

    if len(corners) > 0:
        for i in range(0, len(ids)):
           
            rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients,
                                                                       distortion_coefficients)

            # Draw ID on the frame
            marker_id = str(ids[i][0])
            marker_center = tuple(np.mean(corners[i][0], axis=0).astype(int))
            cv2.putText(frame, marker_id, marker_center, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            pose[ids[i][0]]= (rvec.squeeze(),tvec.squeeze())
            print(f"id = {ids[i][0]}")
            print(f"rvec = {rvec}")
            print(f"tvec = {tvec}")
            # print(markerPoints)
            cv2.aruco.drawDetectedMarkers(frame, corners) 

            cv2.aruco.drawAxis(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 0.01)
    return frame,pose


if __name__ == '__main__':
    # import the opencv library
    intrinsic_camera = np.array(((933.15867, 0, 657.59),(0,933.1586, 400.36993),(0,0,1)))
    distortion = np.array((-0.43948,0.18514,0,0))
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        output, _ = pose_estimation(frame, intrinsic_camera, distortion)
        # Display the resulting frame
        cv2.imshow('frame', output)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # After the loop release the cap object
    vid.release()
        # Destroy all the windows
    cv2.destroyAllWindows()
