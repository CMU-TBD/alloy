import std_msgs.msg
import os
from rospkg import RosPack
import rospy

__all__ = [
    'create_ros_header',
    'resolve_res_path'
]

def create_ros_header(rospy, frame=""):
    """Creates ros header for a given rospy and frame

    parameters
    ----------
    rospy: rospy object
        You must pass in the rospy object as the time is relative to it.
    frame: string (optional)
        The frame of the header, if it's empty, it means the global frame

    returns
    -------
    std_msgs.msg.Header
        Header message
    """
    msg = std_msgs.msg.Header()
    msg.stamp = rospy.Time.now()
    msg.frame_id = frame

    return msg

def resolve_res_path(path, package_name=None, res_path=None):
    """
    Follow a list of rules to find this path.
    (1) If the path exist and it's a file, return True, path
    (2) package_name_dir/path
    (3) Extra filename and apply package_name/res/file_name

    parameters
    ----------
    path: string
        the complete path or just the filename
    package_name: string (optional)  
        ROS package name

    res_path: string (optional)  
        resource directory in ROS package

    returns
    -------
    string
        If the path exist, the actual path. None if unresolvable.
    """

    #Rule (1)
    if os.path.isfile(path):
        return path

    #Rule (2)
    if package_name:
        #try to find the ros package
        rp = RosPack()
        try:
            dirpath = rp.get_path(package_name)
        except ResourceNotFound as err:
            rospy.logwarn('unable find given rospackage in "resolve_path"')
            return None
        if res_path is None:
            res_path = 'res'
        filepath = os.path.join(dirpath,res_path,path)
        if os.path.isfile(filepath):
            return filepath
        else:
            return None
    else:
        return None

       
