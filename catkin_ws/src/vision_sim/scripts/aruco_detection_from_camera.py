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
    intrinsic_camera = np.array(((1000, 0, 480/2),(0,1000, 640/2),(0,0,1)))
    distortion = np.array((0.,0,0,0))

    # intrinsic_camera = np.array(((933.15867, 0, 657.59),(0,933.1586, 400.36993),(0,0,1)))
    # distortion = np.array((-0.43948,0.18514,0,0))
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        img_width, img_height, _ = frame.shape
        # print(img_width, img_height)
        # break
        
        output, pose = pose_estimation(frame, intrinsic_camera, distortion)
        
        #define control for robot 
        key_list = pose.keys()
        
        key_list = pose.keys()
        print(key_list)
        if len(key_list) == 0:
            print('---------object detection------')

            print("Detect the docker using ObjDetection")

        else:
            
            if 0 in key_list:
                kp_surge = 0.5
                curr_x = pose[0][1][2]
                curr_y = pose[0][1][0]
                curr_z = pose[0][1][1]
                
                des_x = 0
                des_y = 0
                des_z = 0

                thres = 0.005
                err_x = curr_x - des_x
                err_y = curr_y - des_y
                err_z = curr_z - des_z

                if np.abs(err_x) <= thres:
                    err_x = 0
                if np.abs(err_y) <= thres:
                    err_y = 0
                if np.abs(err_z) <= thres:
                    err_z = 0
            
            else:

                # kp_surge = 0.01
                if 1 in key_list: #TL
                    err_x = pose[1][1][2]
                    err_y = pose[1][1][0] + 0.09
                    err_z = pose[1][1][1] + 0.05
                elif 2 in key_list: #TR
                    err_x = pose[2][1][2]
                    err_y = pose[2][1][0] - 0.05
                    err_z = pose[2][1][1] + 0.05
                elif 3 in key_list: #BL
                    err_x = pose[3][1][2]
                    err_y = pose[3][1][0] + 0.09
                    err_z = pose[3][1][1]
                elif 4 in key_list: #BR
                    err_x = pose[4][1][2]
                    err_y = pose[4][1][0] - 0.05
                    err_z = pose[4][1][1]
                
            kp = 0.5
            surge_control = "forward" if err_x > 0 else "backward" 
            sway_control = "right" if err_y > 0 else "left"
            heave_control = "up" if err_z > 0 else "down"

            if 0 in key_list:
                print(f"Control: SURGE: {surge_control}, SWAY: {sway_control}, HEAVE: {heave_control}")



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
