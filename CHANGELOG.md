# Changelog


## [Unreleased]
#### Added
- A dedicted `CHANGLOG.md` to track the changes of the package.
- CI Intergration of Github Action
- Added `ac_wait_for_server_wrapper` that wraps actionlib's simple wait_for_server command and let us know if its waiting.
- **[spatial]** Added Polygon representation and calculate intersections between it and ray or lines.
- **[ros]** Convertion between geometry_msgs/Point and numpy.

#### Changed
- Migrated some test from unittest to pytest.
- Cleaned up formatiing in some sub packages.


## [0.1.0] - 02/28/2020
* Reorganized code to be in separate modules instead of all being in the same namespace.
* Python3 only implementation.
* Added unit test for all the code.
