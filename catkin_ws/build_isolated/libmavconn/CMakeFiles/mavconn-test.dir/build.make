# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/farooq/.local/lib/python3.8/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/farooq/.local/lib/python3.8/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn

# Include any dependencies generated for this target.
include CMakeFiles/mavconn-test.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/mavconn-test.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/mavconn-test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/mavconn-test.dir/flags.make

CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o: CMakeFiles/mavconn-test.dir/flags.make
CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o: /home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn/test/test_mavconn.cpp
CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o: CMakeFiles/mavconn-test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o -MF CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.d -o CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o -c /home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn/test/test_mavconn.cpp

CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn/test/test_mavconn.cpp > CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.i

CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn/test/test_mavconn.cpp -o CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.s

# Object files for target mavconn-test
mavconn__test_OBJECTS = \
"CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o"

# External object files for target mavconn-test
mavconn__test_EXTERNAL_OBJECTS =

/home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test: CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o
/home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test: CMakeFiles/mavconn-test.dir/build.make
/home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test: gtest/lib/libgtest.so
/home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test: /home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn.so
/home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test: /usr/lib/x86_64-linux-gnu/libboost_system.so.1.71.0
/home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test: CMakeFiles/mavconn-test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mavconn-test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/mavconn-test.dir/build: /home/farooq/Documents/BlueROVCompetition/catkin_ws/devel_isolated/libmavconn/lib/libmavconn/mavconn-test
.PHONY : CMakeFiles/mavconn-test.dir/build

CMakeFiles/mavconn-test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/mavconn-test.dir/cmake_clean.cmake
.PHONY : CMakeFiles/mavconn-test.dir/clean

CMakeFiles/mavconn-test.dir/depend:
	cd /home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn /home/farooq/Documents/BlueROVCompetition/catkin_ws/src/mavros/libmavconn /home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn /home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn /home/farooq/Documents/BlueROVCompetition/catkin_ws/build_isolated/libmavconn/CMakeFiles/mavconn-test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/mavconn-test.dir/depend

