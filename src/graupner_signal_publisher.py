#!/usr/bin/env python

import rospy
from graupner_signal_publisher.msg import GraupnerSignal
import serial

def talker():
    pub = rospy.Publisher('graupner_signal', GraupnerSignal, queue_size=10)
    rospy.init_node('graupner_signal_publisher', anonymous=True)
    rate = rospy.Rate(20)  # 20 Hz

    # Initialize serial port
    ser = serial.Serial('/dev/arduino', 9600, timeout=1)

    while not rospy.is_shutdown():
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            values = line.split(',')
            if len(values) == 4:
                try:
                    msg = GraupnerSignal()
                    msg.throttle = int(values[0])
                    msg.steering = int(values[1])
                    msg.switch_3 = int(values[2])
                    msg.switch_8 = int(values[3])
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
