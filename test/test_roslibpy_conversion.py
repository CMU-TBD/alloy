import roslibpy

from alloy.ros.roslibpy import image_to_numpy

def main():
    ros = roslibpy.Ros(host='localhost', port=9090)
    listener = roslibpy.Topic(ros, '/cameras/left_hand_camera/image', 'sensor_msgs/Image')

    def start_listening():
        listener.subscribe(receive_message)

    def receive_message(message):
        image_to_numpy(message)

    ros.on_ready(start_listening)
    ros.run_forever()

if __name__ == "__main__":
    main()    
