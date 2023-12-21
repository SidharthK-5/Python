#!/usr/bin/env python


# Importing the required libraries

from vitarana_drone.msg import *
from pid_tune.msg import PidTune
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
from std_msgs.msg import Bool
import rospy
import time
import tf
import math

PI=math.pi

class path_finder():

    def __init__(self):
        rospy.init_node('path_finder')      # initializing ros node with name drone_control


        self.sensor_data=[0,0,0,0,0]
	self.setpoint=[0,0,0]
	self.vector_point=plane()
    	self.vector_point_1=plane()
	self.vector_point_2=plane()
	self.current_gps_position=gps_cord()
	self.gps_pos_setpoint=gps_cord()
	self.gps_position=gps_cord()
	self.range_vec=plane()
	self.resultant=plane()
	self.xy=plane()
	self.act=False

	self.sensor_0=None
	self.sensor_1=None
	self.sensor_2=None
	self.sensor_3=None



	# Publishers
	self.drone_cord = rospy.Publisher('/gpsnew',gps_cord, queue_size=1)

        # Subscribers
        rospy.Subscriber('/edrone/gps', NavSatFix, self.gps_callback1)
	rospy.Subscriber('/edrone/range_finder_top', LaserScan, self.range_finder)
	#rospy.Subscriber('/to_path', Bool, self.activate)
	rospy.Subscriber('to_path', gps_cord , self.setpoint_finder)

    def setpoint_finder(self,msg):
	self.gps_pos_setpoint.latitude=msg.latitude
	self.gps_pos_setpoint.longitude=msg.longitude
	self.gps_pos_setpoint.altitude=msg.altitude



    def activate(self):
	store=self.vector()
	if(store==None):
		return False
	else:
	  if(store==1):
		self.sensor_0=True
		self.sensor_1=True
	  if(store==2):
		self.sensor_0=True
		self.sensor_3=True
	  if(store==3):
		self.sensor_3=True
		self.sensor_2=True
	  if(store==4):
		self.sensor_1=True
		self.sensor_2=True
	  if( (self.sensor_data[0]>1 and self.sensor_data[0]<5 and self.sensor_0) or (self.sensor_data[1]>1 and self.sensor_data[1]<5 and self.sensor_1) or (self.sensor_data[2]>1 and self.sensor_data[2]<5 and self.sensor_2) or  (self.sensor_data[3]>1 and self.sensor_data[3]<5 and self.sensor_3) ):
		return True

	return False
	
	

    def gps_callback1(self, msg):

        self.current_gps_position.latitude = msg.latitude
	self.current_gps_position.longitude = msg.longitude
	self.current_gps_position.altitude = msg.altitude

    def range_finder(self,msg):
	self.sensor_data[0]=msg.ranges[0]
        self.sensor_data[1]=msg.ranges[1]
        self.sensor_data[2]=msg.ranges[2]
        self.sensor_data[3]=msg.ranges[3]
        self.sensor_data[4]=msg.ranges[4]
	#print(self.sensor_data)


    def obstacle_avoid(self):
	#print("working")
	self.resultant.x=0
	self.resultant.y=0
	return_value=self.vector()
        if (self.sensor_data[0]>1 and self.sensor_data[0]<5) and (return_value==1 or return_value==2):
		self.resultant.y=(25-self.sensor_data[0]) 
		print("sensor front working")
        if (self.sensor_data[1]>1 and self.sensor_data[1]<5) and (return_value==1 or return_value==4):
                self.resultant.x=(25-self.sensor_data[1])
		print("sensor right working")
        if (self.sensor_data[2]>1 and self.sensor_data[2]<5) and (return_value==3 or return_value==4):
                self.resultant.y +=(-(25-self.sensor_data[2]))
		print("sensor back working")
        if (self.sensor_data[3]>1 and self.sensor_data[3]<5) and (return_value==2 or return_value==3):
		self.resultant.x +=(-(25-self.sensor_data[3]))
		print("sensor left working")
	'''if self.resultant.x>2:
		self.resultant.x=2
	if self.resultant.x<-2:
		self.resultant.x=-2
	if self.resultant.y>2:
		self.resultant.y=2
	if self.resultant.y<-2:
		self.resultant.y=-2'''
       

    def xy_to_gps(self):
	self.xy.x=self.xy.x+self.resultant.x
	self.xy.y=self.xy.y+self.resultant.y
	self.gps_position.latitude=(self.xy.x/110692.0702932625) + 19
	self.gps_position.longitude=(-self.xy.y/105292.0089353767) + 72
	self.gps_position.altitude=1
	#print(self.gps_position.altitude)

    def gps_to_xy(self):
	self.xy.x=110692.0702932625 * (self.current_gps_position.latitude - 19)
	self.xy.y=-105292.0089353767 * (self.current_gps_position.longitude - 72)

    def gps_to_xy_1(self,msg1,msg2):
	msg1.x=110692.0702932625 * (msg2.latitude - 19)
	msg1.y=-105292.0089353767 * (msg2.longitude - 72)

    def final_resultant(self,k):
	if self.resultant.x>0:
		self.resultant.x=k
	if self.resultant.x<0:
		self.resultant.x=-k
	if self.resultant.y>0:
		self.resultant.y=k
	if self.resultant.y<0:
		self.resultant.y=-k
	#print("x",self.resultant.x)
	#print("y",self.resultant.y)

    def final_resultant_1(self,k):
	print("resultant 1 working")
	if self.resultant.x==3:
		self.resultant.x=k
	if self.resultant.x==-3:
		self.resultant.x=-k
	if self.resultant.y==3:
		self.resultant.y=k
	if self.resultant.y==-3:
		self.resultant.y=-k
	#print("x",self.resultant.x)
	#print("y",self.resultant.y)


    def rotate90(self):
	temp=plane()
	temp.x=-self.resultant.y
	temp.y=self.resultant.x
	self.resultant.x=temp.x
	self.resultant.y=temp.y
	'''if(msg.x>0 and msg.y>0):
		temp.x=-msg.y
		temp.y=msg.x
	if(msg.x<0 and msg.y>0):
		temp.x=-msg.y
		temp.y=msg.x
	if(msg.x<0 and msg.y<0)
		temp.x=-msg.y
		temp.y=msg.x
	if(msg.x>0 and msg.y<0):
		temp.x=-msg.y
		temp.y=msg.x'''

    def rotate180(self):
	temp=plane()
	temp.x=-self.resultant.x
	temp.y=-self.resultant.y
	self.resultant.x=temp.x
	self.resultant.y=temp.y

    def rotate_neg90(self):
	temp=plane()
	temp.x=self.resultant.y
	temp.y=-self.resultant.x
	self.resultant.x=temp.x
	self.resultant.y=temp.y


    def vector(self):
	print("working")
        self.gps_to_xy_1(self.vector_point_1,self.current_gps_position)
	self.gps_to_xy_1(self.vector_point_2,self.gps_pos_setpoint)
	self.vector_point.x=self.vector_point_2.x - self.vector_point_1.x
	self.vector_point.y=self.vector_point_2.y - self.vector_point_1.y
	print("vector point x = ",self.vector_point.x)
	print("vector point y = ",self.vector_point.y)
	if(magnitude(self.vector_point)>0.3):
	  if(self.vector_point.x>0 and self.vector_point.y>0):
		print("1st quadrant")
		return 1
	  if(self.vector_point.x<0 and self.vector_point.y>0):
		print("2nd quadrant")
		return 2
	  if(self.vector_point.x<0 and self.vector_point.y<0):
		print("3rd quadrant")
		return 3
	  if(self.vector_point.x>0 and self.vector_point.y<0):
		print("4th quadrant")		
		return 4

	else:
		return None
	
	
	
def magnitude(msg):
	return math.sqrt(math.pow(msg.x,2) + math.pow(msg.y,2))




if __name__ == '__main__': 

    path=path_finder()
    r = rospy.Rate(16)  
    r.sleep()
    while True:
        #print(path.sensor_data)
	if(path.activate()):
             print("path activated")
	     path.obstacle_avoid()
	     print("magnitude",magnitude(path.resultant))
	     if magnitude(path.resultant) > 30 :
		path.final_resultant(3)
		path.rotate180()
	        path.gps_to_xy()
	        path.xy_to_gps()
	        path.drone_cord.publish(path.gps_position)
		r.sleep()
		path.rotate_neg90()
		path.final_resultant(6)		
             else:
		path.final_resultant(3)
                path.rotate90()

	     path.gps_to_xy()
	     path.xy_to_gps()
	     path.drone_cord.publish(path.gps_position)	
	else:
	     print("path planeer not activated")
	     path.gps_position.altitude=0
	     path.gps_position.latitude=0
	     path.gps_position.longitude=0
	     path.drone_cord.publish(path.gps_position)
	r.sleep()
	#print("path running")     


    



