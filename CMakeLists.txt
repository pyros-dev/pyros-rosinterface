cmake_minimum_required(VERSION 2.8.3)
project(pyros_interfaces_ros)

# For ease of use, this CMakeLists allows to use this code from source, as if it were a normal catkin package.
# However no ROS/catkin debian package is provided for it.
# It is just a pip package that your packages should depend on (using rosdep pip dependency mechanism).
# We should follow closely https://github.com/gerkey/ros1_external_use

# Minimal Python module setup - catkin is assumed preinstalled along with ROS
# This assume catkin is installed along with a minimal ROS system.
find_package(catkin REQUIRED COMPONENTS
    catkin_pip
    rospy
    rosgraph
    roslaunch
    rostest
)

# defining current package as a package that should be managed by pip (not catkin - even though we make it usable with workspaces)
catkin_pip_setup()
catkin_package()

## Unit tests
if (CATKIN_ENABLE_TESTING)


    ##############################################################################
    # Nose Tests
    ##############################################################################

    # Careful this will not support parallel testing, due to multiprocess environment used in tests
    # because of ROS (node_init() can be called only once per process)
    # these should be run in separate process each to avoid global side effect during tests
    # TODO : find a way to force nose to run each test isolated ?
    catkin_add_nosetests(pyros_interfaces_ros/tests)
    catkin_add_nosetests(pyros_tests)

    ##############################################################################
    # Ros Tests
    ##############################################################################

    # find_package(catkin REQUIRED COMPONENTS rostest)

    # These rostests need to be run one by one ( because of rospy side effects)
    # Note : using pyros-setup should fix this...
    catkin_add_nosetests(pyros_interfaces_ros/rostests/testService.py)
    catkin_add_nosetests(pyros_interfaces_ros/rostests/testStringPublisher.py)
    catkin_add_nosetests(pyros_interfaces_ros/rostests/testStringSubscriber.py)
    catkin_add_nosetests(pyros_interfaces_ros/rostests/test_param_if_pool.py)
    catkin_add_nosetests(pyros_interfaces_ros/rostests/test_service_if_pool.py)
    catkin_add_nosetests(pyros_interfaces_ros/rostests/test_subscriber_if_pool.py)
    catkin_add_nosetests(pyros_interfaces_ros/rostests/test_publisher_if_pool.py)
    catkin_add_nosetests(pyros_interfaces_ros/rostests/testRosInterface.py)
    # TMP : Disabled because it can hang sometimes on jenkins.
    #catkin_add_nosetests(pyros_interfaces_ros/rostests/testPyrosROS.py)
    # Running with nose because rostest fails ( not sure why yet )

    # add_rostest(pyros_interfaces_ros/rostests/testStringTopic.test)
    # add_rostest(pyros_interfaces_ros/rostests/testService.test)

    # Testing rosinterface class integration in pyros
    # add_rostest(pyros_interfaces_ros/rostests/testRosInterface.test)


endif()
