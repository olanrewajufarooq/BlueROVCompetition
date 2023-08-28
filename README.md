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

The Sparus autonomous underwater vehicle, developed by IQUA Robotics, is specialized for shallow waters up to 200 meters deep. It features a rear configuration with two horizontal thrusters and a central vertical thruster, enabling precise maneuverability. The vehicle is equipped with an antenna for wireless communication, a Doppler Velocity Log (DVL) and an Ultra-Short Baseline (USBL) system for accurate navigation, an Inertial Measurement Unit (IMU) for orientation, and depth sensors for depth measurement. The vehicle's modeling approach is tailored to optimize control by effectively utilizing its parameters, ensuring reliable and precise performance in its designated tasks underwater.

<p align="center">
  <img src="ReadME/sparus.png" alt="Sparus Image">
  <br />Image of IQUA Robotics Sparus
</p>

### Tasks Completed in the project include:

1. Generation of image data from video. 
2. Training of Object Detection model.
3. Deploying Object Detection model in ROS Environment
4. Visual Servoing (Robot control using continuous image feed).
5. Testing in a controlled environment

The original simulator is in the `SparusSim` folder (although there are a couple of problems in the original simulator which have been corrected in the `SimSolution` folder) while the solutions from the modelling and testing are implemented in the `SimSolution` folder. Tasks 1-3 are initially developped in the `SparusIICalculations.mlx` file. While tasks 1-4 are implemented in the files: `SimSolution/parameters.m` and `SimSolution/RovModel.m`. The validation is evaluated by running the simulator in `SimSolution/Sparus_3D_advance_model.mdl` while the data obtained are plotted using the codes in `SimSolution/plotting.m`.

## Tools Used

- Pyhon Programming
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
