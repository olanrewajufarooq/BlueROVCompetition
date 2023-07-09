# CMake generated Testfile for 
# Source directory: /home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn
# Build directory: /home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_libmavconn_gtest_mavconn-test "/home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn/test_results/libmavconn/gtest-mavconn-test.xml" "--return-code" "/home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test --gtest_output=xml:/home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn/test_results/libmavconn/gtest-mavconn-test.xml")
set_tests_properties(_ctest_libmavconn_gtest_mavconn-test PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/catkin/cmake/test/gtest.cmake;98;catkin_run_tests_target;/opt/ros/noetic/share/catkin/cmake/test/gtest.cmake;37;_catkin_add_google_test;/home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn/CMakeLists.txt;109;catkin_add_gtest;/home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn/CMakeLists.txt;0;")
subdirs("gtest")
