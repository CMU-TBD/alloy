"""Convert Functions for roslibpy
"""

import numpy as np
import base64
import matplotlib.pyplot as plt

def image_to_numpy(image_msg_dict, desire_encoding='passthrough'):
    """
    Convert sensor_msgs/Image (in dict form) to a numpy array
    only works with bgra8
    """
    if image_msg_dict['encoding'] != 'bgra8':
        raise NotImplementedError("Unable to convert other image besides bgra8")

    buffer = base64.b64decode(image_msg_dict['data'])
    data_arr = np.frombuffer(buffer, np.uint8)
    data_arr = np.reshape(data_arr,(image_msg_dict['height'],image_msg_dict['width'],4))

    if desire_encoding == 'bgr8':
        data_arr = data_arr[:,:,0:3] 

    return data_arr

# def numpy_to_image(image_numpy):
#     """
#     Convert a numpy array to sensor_msgs/Image (in dict form)
#     only works with bgra8
#     """
#     if image_msg_dict['encoding'] != 'bgra8':
#         raise NotImplementedError("Unable to convert other image besides bgra8")

#     buffer = base64.b64decode(image_msg_dict['data'])
#     data_arr = np.frombuffer(buffer, np.uint8)
#     data_arr = np.reshape(data_arr,(image_msg_dict['height'],image_msg_dict['width'],4))

#     if desire_encoding == 'bgr8':
#         data_arr = data_arr[:,:,0:3] 
#     
#     return data_arr