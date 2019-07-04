#!/usr/bin/env python
#Modified code from PyGame JoyStick Template & HRWROS ROS Publisher Node Template
## Node to publish joystick information
import rospy
import pygame
from std_msgs.msg import String #using string message type
    
def joystickPublisher():
    joy_publisher = rospy.Publisher('joy_info', String, queue_size = 30) #("topic name", msg type, queue_size)
    rospy.init_node('joy_info_publisher', anonymous=False) #("ros_node name", ...)
    rate = rospy.Rate(60) #args is topic frequency in hz

    #following loop uses pygame to identify joystick movement
    #publishes movement on X/Y axis as 0, 1, or -1
    while not rospy.is_shutdown():
        pygame.init()
        pygame.joystick.init()
        joy_info = [] #joy_info is topic being published


        for event in pygame.event.get(): # User did something
            #can be uncommented to read button press
            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
           ''' if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")'''
            
        #checks if there are multiple joysticks
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joy_info.append('Joystick'+ str(i))
            joystick.init()

            #checks number of axes of joystick
            axes = joystick.get_numaxes()
            #can uncomment for debugging (if number of axes are needed to be viewed)
            #print("Number of axes: {}".format(axes))
        
            #this functions checks whether joystick is activatied or not
            for i in range( axes ): 
                axis = joystick.get_axis( i )
                #can uncomment for debugging (will print values to terminal)
                #print("Axis {} value: {:>6.3f}".format(i, axis) )
                if i < 2:
                    if i == 1: #checks whether x or y axis
                        joy_info.append("Y-Axis Value: {:>6.3f}".format(axis))
                    else:
                        joy_info.append("X-Axis Value: {:>6.3f}".format(axis))
 
        joy_publisher.publish(str(joy_info)) #desired topic is published using this function
        rate.sleep() #rate.sleep() means topic is pubished at freq chosen earlier

if __name__ == '__main__':
    try:
        joystickPublisher()
    except rospy.ROSInterruptException:
        pass
