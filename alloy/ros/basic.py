import std_msgs.msg


__all__ = [
    'create_ros_header'
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