# Install script for directory: /home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/install/stage")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RELEASE")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/stage/worlds/bitmaps" TYPE FILE FILES
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/889_05.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/SFU_1200x615.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/SRI-AIC-kwing.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/autolab.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/cave.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/cave_compact.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/cave_filled.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/frieburg.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/ghost.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/hospital.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/hospital_section.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/human_outline.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/mbicp.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/rink.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/sal2.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/simple_rooms.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/space_invader.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/submarine.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/submarine_small.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/table.png"
    "/home/liam-bouffard/Desktop/rob599_mobile_robotics/stage_ws/src/Stage/worlds/bitmaps/uoa_robotics_lab.png"
    )
endif()

