#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt32MultiArray
from quarterscalesimulation.msg import Force

# Global variables to store the received values
throttle_global = 0
steering_global = 0
switch_6_global = 0
switch_8_global = 0
lateral = 0

def graupner_callback(data):
    global throttle_global, steering_global, switch_6_global, switch_8_global, lateral
    throttle_global = data.data[0]
    steering_global = data.data[4]
    switch_6_global = data.data[2]
    switch_8_global = data.data[3]
    lateral = data.data[1]

def map_value_for_throttle(input_value, input_min=1100, input_max=1900, output_min=-6, output_max=6):
    return output_min + (input_value - input_min) * (output_max - output_min) / (input_max - input_min)

def map_value_for_steer(input_value, input_min=1100, input_max=1900, output_min=-1, output_max=1):
    return output_min + (input_value - input_min) * (output_max - output_min) / (input_max - input_min)

def emergency_control():
    rospy.init_node('emergency_control_node', anonymous=True)
    rospy.Subscriber('graupner_signal', UInt32MultiArray, graupner_callback)
    force_pub = rospy.Publisher('/mpc_force', Force, queue_size=1)
    
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        if switch_8_global > 1900:
            rospy.loginfo("Emergency mode activated")
            throttle = map_value_for_throttle(throttle_global)
            lateral_value = map_value_for_throttle(lateral)
            steer = map_value_for_steer(steering_global)
            random_force = [throttle, throttle, -lateral_value - steer, -lateral_value + steer]
            
            force_pub.publish(random_force)
        rate.sleep()

if __name__ == '__main__':
    try:
        emergency_control()
    except rospy.ROSInterruptException:
        pass
