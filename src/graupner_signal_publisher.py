#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt32MultiArray
import serial

def talker():
    pub = rospy.Publisher('graupner_signal', UInt32MultiArray, queue_size=10)
    rospy.init_node('graupner_signal_publisher', anonymous=True)
    rate = rospy.Rate(20)  # 20 Hz

    # Initialize serial port
    ser = serial.Serial('/dev/arduino_nano', 9600, timeout=1)

    while not rospy.is_shutdown():
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            values = line.split(',')
            if len(values) == 4:
                try:
                    msg = UInt32MultiArray()
                    msg.data = [int(values[0]), int(values[1]), int(values[2]), int(values[3])]
                    rospy.loginfo(msg)
                    pub.publish(msg)
                except ValueError:
                    rospy.logwarn("Received invalid data: %s", line)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
