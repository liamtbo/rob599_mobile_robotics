cmake_minimum_required(VERSION 3.20)
project(tutorial_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)


# ----- for custom msg and srv ---------
# find_package: "locate this package and make it's build info available"
find_package(geometry_msgs REQUIRED) # my custom .msg and .srv files reference types from geometry_msgs
# code generator: rads .msg, .srv, .action and generates python classes, c++ structs ....
# rosidl_generate_interfaces below wouldn't exists without this
find_package(rosidl_default_generators REQUIRED) 

# CMake will read these files, validate syntax, gen language binding, install them
rosidl_generate_interfaces(${PROJECT_NAME} # project name is tutorial_interfaces
  "msg/Num.msg"
  "msg/Sphere.msg"
  "srv/AddThreeInts.srv"
  DEPENDENCIES geometry_msgs # "my interface depends on interfaces from geometry_msgs"
)



# ---------------------

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
