#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt32MultiArray
import serial

def talker():
    pub = rospy.Publisher('graupner_signal', UInt32MultiArray, queue_size=10)
    rospy.init_node('graupner_signal_publisher', anonymous=True, log_level=rospy.ERROR)  # Set log level to ERROR to reduce logging
    rate = rospy.Rate(20)  # 20 Hz

    # Initialize serial port
    ser = serial.Serial('/dev/arduino', 38400, timeout=1)

    while not rospy.is_shutdown():
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('latin1').strip()
                values = line.split('|')
                if len(values) == 4:
                    try:
                        # Extract values after the colon and convert to int
                        throttle = int(values[0].split(':')[1].strip())
                        steering = int(values[1].split(':')[1].strip())
                        switch_3 = int(values[2].split(':')[1].strip())
                        switch_8 = int(values[3].split(':')[1].strip())
                        
                        msg = UInt32MultiArray()
                        msg.data = [throttle, steering, switch_3, switch_8]
                        pub.publish(msg)
                    except ValueError:
                        rospy.logwarn("Received invalid data: %s", line)
            except UnicodeDecodeError:
                rospy.logwarn("Received non-UTF-8 data")
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
