

#test if ros exist
try:
    import rospy
    import basic
    #import everything else if possible
    from basic import *

    __all__ = []
    __all__ += basic.__all__

except ImportError:
    raise RuntimeError('Unable to find ROS specific libraries, you maybe trying to reference this sub-module on a none ROS machine')



