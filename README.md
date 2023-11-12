<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <h1 align="center">Autonomous Docking and Underwater Treasure Search with BlueROV</h1>

  <p align="center">
    A project for the control of the BlueROV by Blue Robotics in a 10m by 10m by 6m water tank in Jaume I University, Spain. This project is submitted during the Robotics Challenge at Jaume I University.
    <br />
    <a href="https://www.univ-tln.fr/">
      <img src="ReadME/uji-logo.jpg" alt="UJI Logo" height="100">
    </a>
    .
    <a href="https://www.master-mir.eu/">
      <img src="ReadME/mir-logo.png" alt="MIR Logo" height="100">
    </a>
    <br />
    <a href="https://github.com/olanrewajufarooq/BlueROVCompetition">View Project Files »</a>
    <br />
  </p>
</div>

## Description

The BlueROV is a remotely operated underwater vehicle that has four vertical thrusters and four aximuthally-positioned horizontal thrusters. The robot has a couple of sensors integrated into it, including: depth sensor or pressure sensor, sonars and high-definition camera. The robot is usually conntected to the ground station using an optical fibre or any other suitable cable. This Robot was used in the Robotics Challenge in CIRTESU, Jaume I University.

The Robotics Challenge involves the localization and control of the BlueROV for autonomous docking, treasure search and static object inspection. However, in this repository only the first two tasks are implemented.

<p align="center">
  <img src="ReadME/bluerov.jpg" alt="Sparus Image">
  <br />Image of (Heavy Configuration) BlueROV
</p>

### Tasks Completed in the project include:

1. Generation of image data from video. 
2. Training of Object Detection model.
3. Deploying Object Detection model in ROS Environment
4. Visual Servoing (Robot control using continuous image feed).
5. Testing in a controlled environment

Videos are otained from the treasures that are desired to the hunted. These videos are converted to images in the `VideoToPic` folder using the `VideoToPic/vid_to_pic.py` file. Thereafter, the extracted images are processed on <a href="https://roboflow.com/">RoboFlow</a> - annotation, augmentation and bounding-box definitions, class definition, etc. Then, the model was trained on Yolov5 model using Google Colab. The codes for the remaining tasks are implemented in `catkin_ws/src/vision_sim` folder.

## Tools Used

- Python Programming
- RoboFlow
- Robot Operating System
- PyTorch
- OpenCV

## Usage

1. ROS Installation is required. The Unity Engine used is required (for simulation before testing in the pool).
2. Launch the Unity Simulation Engine which is connected to ROS using ROS-TCP-Endpoint
3. Execute the launch file using `rosrun vision_sim aruco_detection_from_camera.py` from a Linux terminal
4. You can stop the execution using `Ctrl + C` on the terminal.

## Results


https://github.com/olanrewajufarooq/BlueROVCompetition/assets/50842355/6021584c-df23-4c0d-9c55-3044a0c1fd8e


Docking of the BlueROV autonomously in the Unity Simulation Environment
<br>


https://github.com/olanrewajufarooq/BlueROVCompetition/assets/50842355/33dd7626-79ce-4118-b749-73415108f4a4


Treasure Search with the BlueROV in the Unity Simulation Environment
<br>


https://github.com/olanrewajufarooq/BlueROVCompetition/assets/50842355/edee1014-7632-4a55-b6df-d97d5353df45


Docking of the BlueROV autonomously in the Test Pool

<!-- CONTACT -->
## Contact Contributors

* Farooq Olanrewaju - olanrewajufarooq@yahoo.com, farooq-olanrewaju@etud.univ-tln.fr
* Md Sazidur
* AbdelHaleem Saad
* Maria Saleem

<strong>Supervisor</strong>: Prof. Pedro Sanz, <i>Jaume I University</i>; Prof V. Hugel, <i>Director COSMER Lab, Université de Toulon</i>.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/olanrewajufarooq/BlueROVCompetition.svg?style=for-the-badge
[contributors-url]: https://github.com/olanrewajufarooq/BlueROVCompetition/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/olanrewajufarooq/BlueROVCompetition.svg?style=for-the-badge
[forks-url]: https://github.com/olanrewajufarooq/BlueROVCompetition/network/members
[stars-shield]: https://img.shields.io/github/stars/olanrewajufarooq/BlueROVCompetition.svg?style=for-the-badge
[stars-url]: https://github.com/olanrewajufarooq/BlueROVCompetition/stargazers
[issues-shield]: https://img.shields.io/github/issues/olanrewajufarooq/BlueROVCompetition.svg?style=for-the-badge
[issues-url]: https://github.com/olanrewajufarooq/BlueROVCompetition/issues
[license-shield]: https://img.shields.io/github/license/olanrewajufarooq/BlueROVCompetition.svg?style=for-the-badge
[license-url]: https://github.com/olanrewajufarooq/BlueROVCompetition/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/olanrewajufarooq
