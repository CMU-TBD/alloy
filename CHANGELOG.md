# Changelog


## [Unreleased]
#### Added
- **[ros]** Implemented same transformation function (`do_transform_point`,`do_transform_pose`) interface from tf2_geometry_msgs to bypass python3/PyKDL requirements
- **[math]** Conversion from transformation matrix to array.
- Test for ros methods

#### Changed
- Switch to manually declaring the exposed methods in `__init__.py`.
- Added ROS dependencies to github actions to allow ROS testing

## [0.2.1] - 2020-06-04
#### Changed
- Update README 

## [0.2.0] - 2020-06-04
#### Added
- A dedicted `CHANGLOG.md` to track the changes of the package.
- CI Intergration of Github Action
- **[spatial]** Added Polygon representation and calculate intersections between it and ray or lines.
- **[ros]** Convertion between geometry_msgs/Point and numpy.
- **[ros]** Added `ac_wait_for_server_wrapper` that wraps actionlib's simple wait_for_server command and let us know if its waiting.

#### Changed
- Migrated some test from unittest to pytest.
- Cleaned up formating in some sub packages.


## [0.1.0] - 02/28/2020
* Reorganized code to be in separate modules instead of all being in the same namespace.
* Python3 only implementation.
* Added unit test for all the code.
