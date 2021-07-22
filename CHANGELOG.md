# Changelog

## [Unreleased]
- **[Fixed]** bug where poseStamped wasn't return in `to_pose_stamped`
- **[Added]** `alloy.interaction.dialog` that provides useful methods to preprocess dialog/interactions.

## [0.2.5] - 2021-05-27
- **[Added]** extracting quaternion from matrix.
- **[Added]** *[ros]* generic convertor `to_pose` and `to_pose_stamped`

## [0.2.4] - 2021-03-30
- **[Changed]** *[ros]* you can pass time stamp to the header creator.
- **[Fixed]** Path issue that cause `spatial` not showing up in pypi distributions.

## [0.2.3] - 2021-03-08
- **[Added]** *[math]* Added `rpy_to_quaternion`.
- **[Added]** *[spatial]* Additional test for points in box & check for current size.
- **[Fixed]** *[spatial]* Box now has a the correct center when created with min/max points.
- **[Fixed]** *[spatial]* Box now has static method `inflate_box` that returns a new box with inflated parameters.

## [0.2.2] - 2020-08-03
- **[Added]** *[ros]* Implemented same transformation function (`do_transform_point`,`do_transform_pose`) interface from tf2_geometry_msgs to bypass python3/PyKDL requirements
- **[Added]** *[math]* Conversion from transformation matrix to array.
- **[Added]** Test for ros methods
- **[Added]** *[tools]* A function `convert_word_list_to_num_str` that converts a list of literal numbers ('four two') to number string ('42').

#### Changed
- **[Changed]** Switch to manually declaring the exposed methods in `__init__.py`.
- **[Changed]** Added ROS dependencies to github actions to allow ROS testing

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
