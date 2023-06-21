# Sample GitLab Project

This sample project shows how a project in GitLab looks for demonstration purposes. It contains issues, merge requests and Markdown files in many branches,
named and filled with lorem ipsum.

You can look around to get an idea how to structure your project and, when done, you can safely delete this project.

[Learn more about creating GitLab projects.](https://docs.gitlab.com/ee/gitlab-basics/create-project.
-Camara_publisher => recieve the image from the udp port and publish it on ros
-Camarareader => Reads the camara from the udp port
-enviarimagenesdeRaspberry => reads the image from the camara in the raspberry and send it through the udp port
-mavlink_motore => move the motors using pymavlink
-SubscriberImage => example of how to read an image from the ros topic
-Subscriptorcmd_vel => subscribes to a ros comand velocity topic and move the motors using pymavlink
-yaw_depth_publisher => use pymavlink to get the yaw and depth, then it publish it in two float32 topics
