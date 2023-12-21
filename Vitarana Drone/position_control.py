#!/usr/bin/env python
'''
# Team ID:          < 158 >
# Theme:            < vitarana_drone>
# Author List:      < shoaib razik,sidharth,vishnu,muhammed sinan k>
# Filename:         < position_controller.py >
# Functions:        < [delivery_coordinate_maker,return_coordinate_maker,ismarker,gps_callbacknew,gripper_check_callback,range_bottom,path_callback,
gps_callback,gps_setpoint_passing,pid_position,isinbox,isinbox_1,isinbox_2,run_pid,wavepoint,xy_to_gps, gps_to_xy stabilise,stabilise_hover,stabilise_path,check_wave,hover,stabilise_1,land_here,goanddetect,stabilisem,whole_process,to_dest,calc_time,magnitude]
 >
# Global variables: <None >
'''


# Importing the required libraries
from vitarana_drone.msg import *
from vitarana_drone.srv import *
from pid_tune.msg import PidTune
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import rospy
import time
import tf
import math
import csv 
import copy

PI=math.pi
r=None
k=None
t=None

with open('/home/muhammedsinank/catkin_ws/src/vitarana_drone/scripts/sequenced_manifest.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
def delivery_coordinate_maker():
        '''
Purpose:
---
< inorder to change grid boxes designation to gps coordinates >

Input Arguments:
---
None
Returns:
---
< delivery_dict >` :  [ < dictionary > ]
    < it returns a dictionary with grids ac keys and its coordinates as values >


Example call:
---
< dic=delivery_coordinate_maker()>
'''
	delivery_pt_names = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
	delivery_pt_values = []
	lat_addition = 1.5/110692.0702932625
	long_addition = 1.5/105292.0089353767
	
	key_val = 0
	for i in range(3):
		for j in range(3):
			delivery_pt_values.append(tuple([18.9998102845+(i*lat_addition),72.000142461+(j*long_addition),16.757981]))
			key_val += 1

	delivery_dict = dict(zip(delivery_pt_names,delivery_pt_values))
	return delivery_dict


def return_coordinate_maker():
  '''
Purpose:
---
< inorder to change grid boxes designation to gps coordinates(return grid) >

Input Arguments:
---
None
Returns:
---
< return_dict >` :  [ < dictionary > ]
    < it returns a dictionary with grids ac keys and its coordinates as values >


Example call:
---
< dic=return_coordinate_maker()>
'''
	return_pt_names = ['X1','X2','X3','Y1','Y2','Y3','Z1','Z2','Z3']
	return_pt_values = []
	lat_addition = 1.5/110692.0702932625
	long_addition = 1.5/105292.0089353767
	
	key_val = 0
	for i in range(3):
		for j in range(3):
			return_pt_values.append(tuple([18.9999367615+(i*lat_addition),72.000142461+(j*long_addition),16.757981]))
			key_val += 1

	return_dict = dict(zip(return_pt_names,return_pt_values))
	return return_dict
delivery_grid = delivery_coordinate_maker()
return_grid = return_coordinate_maker()
#print(delivery_grid)
#print(return_grid)
#print(data)
listofsetpoints=[]
deliverylist=[]
returnlist=[]
for i in data:
    if i[0]=='Delivery':
        deliverylist.append(i)
    else:
        returnlist.append(i)
for i in range(0,len(deliverylist)):
    deliverylist[i].pop(0)
for i in range(0,len(deliverylist)):
     
    deliverylist[i][1]=deliverylist[i][1].split(",")  
    new_list = [float(j) for j in deliverylist[i][1]]
    deliverylist[i][1]=new_list
for i in range(0,len(returnlist)):
    returnlist[i].pop(0)
for i in range(0,len(returnlist)):
    #returnlist[i][1]=returnlist[i][1].strip()
    returnlist[i][0]=returnlist[i][0].split(",")  
    new_list1 = [float(j) for j in returnlist[i][0]]
    returnlist[i][0]=new_list1
#print("deliverylist",deliverylist)
#print("returnlist",returnlist)
for i in deliverylist:
    i[0]=delivery_grid[i[0]]
for i in returnlist:
    i[1]=return_grid[i[1]]
   
#print("d",deliverylist)
#print("r",returnlist)
finald=[]
finalr=[]
for i in range(9):
    finald.append(deliverylist[i][0])
    finald.append(returnlist[i][0])
    finalr.append(deliverylist[i][1])
    finalr.append(returnlist[i][1])

print("del",finald)
print("ret",finalr)



class position():

    def __init__(self):
        rospy.init_node('position_control')      # initializing ros node with name drone_control


        self.gps_pos_setpoint= [0,0,0]
	self.setpoint4=[0,0,0]
	self.setpoint5=[0,0,0]
	self.gps_pos_setpoint_1=gps_cord()
	self.xy=plane()
	self.vector_point_1=plane()
	self.vector_point_2=plane()
	self.resultant=plane()
	self.tan_theta=0.0
	self.angle=0

	self.flight=None
	self.isgrip=False

	self.sensor_bottom=0.0

        self.path_pos=[0,0,0]
	self.gps_position_2=[0,0,0]
	self.gps_pos_setpoint= [0,0,0]
        self.gps_position = [0.0, 0.0, 0.0]
	self.act_landing=False

        self.Kp = [170000, 170000, 25.11] #34.93
        self.Ki = [0, 0, 0.262]
        self.Kd = [500000, 500000,50] #34.93
 
	self.prev_values = [0,0,0]
	self.max_values = [1024, 1024, 1024, 1024]
	self.min_values = [0, 0, 0, 0]

	
	# for storing curretn error
        self.pos_error=[0,0,0]

        # for storing previous error
        self.prev_pos_error=[0,0,0]

	# defining pid for 3 axes 
        self.pid_altitude=0
        self.pid_latitude=0
        self.pid_longitude=0
	self.pid_throttle=0
	self.pid_landing=0
	self.prev_pid_landing=0

	# integral term
        self.iterm_altitude=0
	self.iterm_latitude=0
	self.iterm_longitude=0
	self.iterm_landing=0
	
	#pasing z axis error
	#self.gps_error=Gps_error()

        self.sample_time = 16 #0.060  # in seconds

	self.drone_cmd=edrone_cmd()
	self.drone_cmd.rcRoll=0
	self.drone_cmd.rcPitch=0
	self.drone_cmd.rcYaw=0
	self.drone_cmd.rcThrottle=0


        self.pwm_cmd = prop_speed()
        self.pwm_cmd.prop1 = 0.0
        self.pwm_cmd.prop2 = 0.0
        self.pwm_cmd.prop3 = 0.0
        self.pwm_cmd.prop4 = 0.0

	self.Kp_1=10
	self.Kd_1=15
	self.Ki_1=0

	self.check_box=None

        # Publishers
	
	self.drone_command_pub = rospy.Publisher('/drone_cmd',edrone_cmd, queue_size=1)
	self.gps_error_zpub=rospy.Publisher('/z_error',ryp_error, queue_size=1)
        self.gps_error_latpub=rospy.Publisher('/lat_error',ryp_error, queue_size=1)
        self.gps_error_lonpub=rospy.Publisher('/lon_error',ryp_error, queue_size=1) 
	self.to_path_pub=rospy.Publisher('to_path',gps_cord, queue_size=1)
	self.to_activate = rospy.Publisher('condt', Bool, queue_size=1)
	self.buildinghight=rospy.Publisher('hight',Float64, queue_size=1)
	self.landing_pub=rospy.Publisher('landing',Float64, queue_size=1)
	rospy.Subscriber('/edrone/gps', NavSatFix, self.gps_callback)
	rospy.Subscriber('/gpsnew',gps_cord,self.path_callback)
	rospy.Subscriber('/edrone/range_finder_bottom', LaserScan, self.range_bottom)
	rospy.Subscriber('/edrone/gripper_check',String,self.gripper_check_callback)
	rospy.Subscriber('/edrone/gpsnew', NavSatFix, self.gps_callbacknew)
	rospy.Subscriber('/ismarker',Bool,self.ismarker)
	


	self.grip = rospy.ServiceProxy('/edrone/activate_gripper',Gripper,bool)


    def ismarker(self,msg):
	'''
	Purpose:
	---
	<  call back function to know if marker has been detected >

	Returns:
	---
	< markerdetect >` :  [ < boolian> ]
	    < truth value>



	Example call:
	---
	<self.ismarker(msg) >
	'''
        print("wow")
        self.markerdetect=msg.data

    def gps_callbacknew(self, msg):
	'''
	Purpose:
	---
	<  call back function to know gps positions given by pathplanner>

	Returns:
	---
	< setpoint4 >` :  [ < list> ]
	    <stores gps coordinates to setpoint 4>



	Example call:
	---
	<self.gps_callback(msg) >
        '''
        self.setpoint4[0] = msg.latitude
	self.setpoint4[1] = msg.longitude
	self.setpoint4[2] = self.gps_position[2]

    def gripper_check_callback(self,msg):
        '''
	Purpose:
	---
	<  call back function to check if parcell has been gripped>

	Returns:
	---
	< self.check_box >` :  [ boolean ]
	    <stores true if gripped>

	Example call:
	---
	<gripper_check_callback(msg) >
        '''
	self.check_box=msg.data

    def range_bottom(self,msg):
        '''
	Purpose:
	---
	<  call back function to know value of bottomsensor value>

	Returns:
	---
	< self.sensor_bottom >` :  [ float]
	    <stores sensor value into variable>

	Example call:
	---
	<range_bottom(msg) >
        '''
	self.sensor_bottom=msg.ranges[0]
	
	

    def path_callback(self,msg):
         '''
	Purpose:
	---
	<  call back function to store coordinates given by pathpalnner>

	Returns:
	---
	< self.pathpos >` :  [ <list>]
	    <stores gps given by pathplanner>

	Example call:
	---
	<path_callback(msg) >
        '''
	self.path_pos[0]=msg.latitude
	self.path_pos[1]=msg.longitude
	self.path_pos[2]=msg.altitude

   
    def gps_callback(self, msg):
        '''
	Purpose:
	---
	<  call back function to know current gps coordinates>

	Returns:
	---
	<  self.gps_position >` :  [ <list>]
	    <stores gps coordinates>

	Example call:
	---
	<gps_callback(msg) >
        '''
        self.gps_position[0] = msg.latitude
	self.gps_position[1] = msg.longitude
	self.gps_position[2] = msg.altitude
	

    def gps_setpoint_passing(self):
        
	self.gps_pos_setpoint_1.latitude=self.gps_pos_setpoint[0]
	self.gps_pos_setpoint_1.longitude=self.gps_pos_setpoint[1]
	self.gps_pos_setpoint_1.altitude=self.gps_pos_setpoint[2]
	

	

    
        # --------------------Set the remaining co-ordinates of the drone from msg----------------------------------------------

    '''def drone_set_pos_callback(self, msg):
        self.drone_pos_setpoint[0] = msg.latitude
	self.drone_pos_setpoint[1] = msg.longitude
	self.drone_pos_setpoint[2] = msg.altitude'''

    '''def throttle_set_pid(self, throttle):
        self.Kp[2] = throttle.Kp * 0.01 #0.001#0.06  # This is just for an example. You can change the ratio/fraction value accordingly
        self.Ki[2] = throttle.Ki * 0.008
        self.Kd[2] = throttle.Kd * 0.03'''


        # ---------------------------------------------------------------------------------------------------------------


    # ----------------------------------------------------------------------------------------------------------------------

    def pid_position(self):
        '''
	Purpose:
	---
	< to do pid controll of position>

	Example call:
	---
	<self.pid_position()>
        '''
	self.pos_error[2]=self.gps_position[2] - self.gps_pos_setpoint[2]
        self.pos_error[1]=(self.gps_position[1] - self.gps_pos_setpoint[1])
        self.pos_error[0]=(self.gps_position[0] - self.gps_pos_setpoint[0])
        self.iterm_latitude+=self.pos_error[0]
        self.iterm_longitude+=self.pos_error[1]
        self.iterm_altitude+=self.pos_error[2]

        self.pid_latitude=self.pos_error[0]*self.Kp[1] + (self.pos_error[0]-self.prev_pos_error[0]) * (self.sample_time) * self.Kd[1]
        self.pid_longitude=self.pos_error[1]*self.Kp[0] + (self.pos_error[1]-self.prev_pos_error[1]) * (self.sample_time) * self.Kd[0] 
	self.pid_throttle=self.pos_error[2]*self.Kp[2] + (self.pos_error[2]-self.prev_pos_error[2]) * (self.sample_time) * self.Kd[2]+(self.iterm_altitude*(self.Ki[2]))
	if self.act_landing==True:
	  if( (self.gps_position[2]>self.gps_pos_setpoint[2]) and (self.prev_pos_error[2]-self.pos_error[2])>0.1 ):
	    self.pid_landing=(25-self.sensor_bottom)*self.Kp_1 + (self.prev_sensor_bottom-self.sensor_bottom)*self.Kd_1
	    print("pid landing=",self.pid_landing)

	  else:
	    if(self.gps_position[2]<self.gps_pos_setpoint[2] and abs(self.gps_position[2]-self.gps_pos_setpoint[2])>1 ):
	        self.pid_landing=self.pid_landing/2
	    if(self.pid_landing<1):
	        self.pid_landing=0	

	self.drone_cmd.rcThrottle=self.pid_throttle
        self.drone_cmd.rcRoll=-self.pid_latitude
        self.drone_cmd.rcPitch=-self.pid_longitude
	if (self.path_pos[2]==1 and self.flight==False):
	  if self.drone_cmd.rcRoll >2:
             self.drone_cmd.rcRoll=13
          if self.drone_cmd.rcRoll<-2:
             self.drone_cmd.rcRoll=-13
          if self.drone_cmd.rcPitch >2:
             self.drone_cmd.rcPitch=13
          if self.drone_cmd.rcPitch<-2:
             self.drone_cmd.rcPitch=-13
	else:
          if self.drone_cmd.rcRoll >5:
             self.drone_cmd.rcRoll=5
          if self.drone_cmd.rcRoll<-5:
             self.drone_cmd.rcRoll=-5
          if self.drone_cmd.rcPitch >5:
             self.drone_cmd.rcPitch=5
          if self.drone_cmd.rcPitch<-5:
             self.drone_cmd.rcPitch=-5

	self.prev_pos_error[2]=self.pos_error[2]
        self.prev_pos_error[1]=self.pos_error[1]
        self.prev_pos_error[0]=self.pos_error[0]
	self.prev_sensor_bottom=self.sensor_bottom
	self.gps_error_zpub.publish(self.pid_throttle)
	self.landing_pub.publish(self.pid_landing)
        self.gps_error_latpub.publish(self.pos_error[0])
        self.gps_error_lonpub.publish(self.pos_error[1])
	rospy.loginfo("running")

	self.drone_command_pub.publish(self.drone_cmd)

    def isinbox(self):
	'''
	Purpose:
	---
	< to know if drone is in threshold of a setpoint>

	Returns:
	---
	<Boolean >` :  [ < Boolean> ]
	Example call:
	---
	< self.isinbox()>
	'''
	if self.pos_error[0]>-0.000004517 and self.pos_error[0]<0.000004517 and self.pos_error[1]>-0.0000047487 and self.pos_error[1]<0.0000047487 and self.pos_error[2]>-0.2 and self.pos_error[2]<0.2:
	    return True

    def isinbox_1(self,k):
       '''
	Purpose:
	---
	< to know if drone is in threshold of a setpoint with adjustable threshold>
        Input Arguments:
	---
	<k>` :  [ <float> ]
	    < it increases the threshold >

	Returns:
	---
	<Boolean >` :  [ < Boolean> ]
	Example call:
	---
	< self.isinbox_1()>
	'''
	if self.pos_error[0]>-0.000004517*k and self.pos_error[0]<0.000004517*k and self.pos_error[1]>-0.0000047487*k and self.pos_error[1]<0.0000047487*k and self.pos_error[2]>-0.2 and self.pos_error[2]<0.2:
	    return True


    def isinbox_2(self,k):
        '''
	Purpose:
	---
	< to know if drone is in threshold of a setpoint with adjustable threshold>
        Input Arguments:
	---
	<k>` :  [ <float> ]
	    < it increases the threshold >

	Returns:
	---
	<Boolean >` :  [ < Boolean> ]
	Example call:
	---
	< self.isinbox_2()>
	'''
	if self.pos_error[0]>-0.000004517*k and self.pos_error[0]<0.000004517*k and self.pos_error[1]>-0.0000047487*k and self.pos_error[1]<0.0000047487*k and self.pos_error[2]>-0.2*(k/1.2) and self.pos_error[2]<0.2*(k/1.2):
	    return True

        
    def run_pid(self):	
        '''
	Purpose:
	---
	< to run pid controller in a loop>
	Example call:
	---
	< self.run_pid>
	'''	
	    self.pid_position() 
	    print("gps setpoint",self.gps_pos_setpoint)
            r = rospy.Rate(self.sample_time)
	    r.sleep()
                                                                                 
                         
    def wavepoint(self,msg):
         '''
	Purpose:
	---
	<function to dictate wave point coordinates for the drone to follow(by knowing where we are now and where we should be)>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<wavepoint(msg) >
        '''
	print("inside wavepoint")
	print("msg",msg)
	self.gps_to_xy(self.vector_point_1,self.gps_position)
	self.gps_to_xy(self.vector_point_2,msg)
	self.xy.x=self.vector_point_2.x-self.vector_point_1.x
	self.xy.y=self.vector_point_2.y-self.vector_point_1.y
	print("x= ",self.xy.x)
	print("y= ",self.xy.y)
	k=10
	if (magnitude(self.xy)>k):
		self.xy.x=( self.xy.x/magnitude(self.xy) )*k
		self.xy.y=( self.xy.y/magnitude(self.xy) )*k
		print("self.xy.x",self.xy.x)
		print("self.xy.y",self.xy.y)
		self.xy_to_gps(msg)
		self.k=4
		self.t=0.2
		return False
	else:
		print("else of wave point running")
		self.k=1
		self.t=1
		self.xy_to_gps(msg)
		return True
	
                                           
    def xy_to_gps(self,msg):
        '''
	Purpose:
	---
	< to convert cartetian coordinates to gps coordinates>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < list of coordinates to convert to gps is provided >

	Returns:
	---
	< self.gps_position_2>` :  [ <list> ]
	Example call:
	---
	< self.xy_to_gps(msg)>
        '''
	print("xy to gps working")
	print("msg",msg)
	self.resultant.x=self.vector_point_1.x+self.xy.x
	self.resultant.y=self.vector_point_1.y+self.xy.y
	self.gps_position_2[0]=(self.resultant.x/110692.0702932625) + 19
	self.gps_position_2[1]=(-self.resultant.y/105292.0089353767) + 72
	self.gps_position_2[2]=msg[2]
	print("gps position 2 = ",self.gps_position_2)


    def gps_to_xy(self,msg1,msg2):
         '''
	Purpose:
	---
	< to convert gps coordinates to cartesian coordinates>
        Input Arguments:
	---
	<msg_2>` :  [ <list> ]
	    < list of coordinates to convert to cartesian is provided >
        <msg_1>` :  [ <list> ]
	    < list of coordinates converted to cartesian >

	Returns:
	---
	< self.gps_position_2>` :  [ <list> ]
	Example call:
	---
	< self.gps_to_xy(msg)>
        '''
	print("gps to xy working")
	msg1.x=110692.0702932625 * (msg2[0] - 19)
	msg1.y=-105292.0089353767 * (msg2[1] - 72)
	print("x cord",msg1.x)
	print("y cord",msg1.y)


    def stabilise(self,msg):
        '''
	Purpose:
	---
	<inorder to go and stabilise given a setpoint>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<stabilise(msg) >
        '''
	flag=0
	t0=0
	while True:
		self.gps_pos_setpoint=msg
		if self.isinbox_1(self.k):
			t0=time.clock()
			while(self.isinbox_1(self.k)):
			    self.run_pid()
			    if(calc_time(t0)>self.t):
				flag=1
				break
		if flag==1:
			return True
		if (self.path_pos[2]==1 and self.flight==False):
			return False

		self.run_pid()


    def stabilise_hover(self,msg):
         '''
	Purpose:
	---
	<inorder to go and stabilise given a setpoint during going up>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<stabilise_hover(msg) >
        '''
	flag=0
	t0=0
	while True:
		self.gps_pos_setpoint=msg
		if self.isinbox_2(self.k):
			t0=time.clock()
			while(self.isinbox_2(self.k)):
			    self.run_pid()
			    if(calc_time(t0)>self.t):
				flag=1
				break
		if flag==1:
			return True
		if (self.path_pos[2]==1 and self.flight==False):
			return False

		self.run_pid()


    def stabilise_path(self,msg):
        '''
	Purpose:
	---
	<inorder to go and stabilise given a setpoint (by pathplanner)>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<stabilise_path(msg) >
        '''
	flag=0
	t0=0
	while True:
		self.gps_pos_setpoint=msg
		self.run_pid()
		if ( (self.path_pos[2]==1 or self.path_pos[2]==2) and self.flight==False):
			break


	
    def 
(self,msg):
	self.gps_pos_setpoint=msg
	self.gps_setpoint_passing()
	self.to_path_pub.publish(self.gps_pos_setpoint_1)
	while(True):
	  if(self.path_pos[2]==1 and self.flight==False):
                print("path called")
                print("path called")
                print("path called")
                print("path called")
		self.stabilise_path( [self.path_pos[0],self.path_pos[1],msg[2] ] )
		continue
			 
	  else:
		checking=None
		checking=self.check_wave(msg)
  		if(checking==True):
			break
		if(checking==False):
			continue
	print("exiting check")
	print("exiting check")
	print("exiting check")
	print("exiting check")
	print("exiting check")


    def check_wave(self,msg):
         '''
	Purpose:
	---
	<inorder to adjust to setpoints given by wavepoint and to stabilise there if >
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<check_wave(msg) >
        '''
	print("inside check wave")
	print("Msg",msg)
	if(self.flight==False):
		while(self.wavepoint(msg)!=True and self.flight==False):
			if(self.stabilise(self.gps_position_2)==True):
				continue
			else:
				return False
		print("if else is running inside check_wave")
		if(self.stabilise(self.gps_position_2)==True):
				return True
		else:
				return False
		

	else:
	 if(self.flight==True):
	    if (msg[2] - self.gps_position[2])>0:
		self.hover(msg)
		return True
	    else:
		self.land_here(msg)
		return True

    def hover(self,msg):
        '''
	Purpose:
	---
	<inorder to adjust to a given height >
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<hover(msg) >
        '''
	while(True):
		print("hover working")
		print("hover working")
		print("hover working")
		print("hover working")

		if (msg[2]-self.gps_position[2] )>6:
			self.k=4
			self.t=0.2
			self.stabilise_hover( [msg[0],msg[1],self.gps_position[2]+5] )
			continue
		else:
			self.k=1
			self.t=1
			self.stabilise(msg)
			break		





    def stabilise_1(self,msg):
        '''
	Purpose:
	---
	<inorder to go and stabilise given a setpoint while landing>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<stabilise_1(msg) >
        '''
	flag=0
	t0=0
	while True:
		self.gps_pos_setpoint=msg
		if self.isinbox_2(4) and (self.sensor_bottom >=0.24):
			t0=time.clock()
			while(self.isinbox_2(4)):
			    self.run_pid()
			    if(calc_time(t0)>1):
				flag=1
				break
		if flag==1:
			break
			
		if ( self.sensor_bottom < 0.35) and (self.gps_position[2] - msg[2])<0.5:
			self.k=1
			self.t=1
			self.stabilise( [ msg[0],msg[1],self.gps_position[2] ])
			break
		self.run_pid()

    def land_here(self,msg):
        '''
	Purpose:
	---
	<inorder to land and stabilise given landing spot>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<stabilise_1(msg) >
        '''
	self.flight=True
	print(self.gps_position[2]-msg[2])
	print(self.gps_position[2]-msg[2])
	print(self.gps_position[2]-msg[2])
	print(self.gps_position[2]-msg[2])
	print(self.gps_position[2]-msg[2])
	print(self.gps_position[2]-msg[2])
	while (True):
	    if (self.gps_position[2]-msg[2] )>3:
		self.k=6
		self.t=0.1
                ran=self.gps_position[2]-msg[2]-2
                currentheight=copy.deepcopy(self.gps_position[2])
                now=0
                i=1
                while now < ran:
                    self.stabilise( [msg[0],msg[1],currentheight-i*1.75] )
                    i+=1
                    now+=i*1.75
		
	    elif (self.gps_position[2]>msg[2]) and self.isgrip==True:
		print("else of land here working")
		print("else of land here working")
		print("else of land here working")
		print("else of land here working")
		print("else of land here working")
	        self.k=1
		self.t=1
		self.stabilise([msg[0],msg[1],msg[2]+0.1])
		return True		
	    else:
		if self.sensor_bottom <5 and self.isgrip==False:
			dist=self.sensor_bottom-0.23 
			print("dist=== ",dist)
		        self.k=1
		        self.t=1
			self.act_landing=True
			self.stabilise_1(msg)
			self.act_landing=False
			return True
		else:
	            while (True):
		        if (self.gps_position[2]-msg[2] )>3:
		            self.k=6
		            self.t=0.1
                            ran=self.gps_position[2]-msg[2]-2
                            currentheight=copy.deepcopy(self.gps_position[2])
                            now=0
                            i=1
                            while now < ran:
                                self.stabilise( [msg[0],msg[1],currentheight-i*1.75] )
                                i+=1
                                now+=i*1.75
		        else:
			    self.k=1
			    self.t=1
			    self.stabilise([msg[0],msg[1],msg[2]+0.1])
			    return True


    def goanddetect(self,msg):
        '''
	Purpose:
	---
	<inorder to go up and detect marker>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<goanddetect(msg) >
        '''
        for i in range(1,6):
            if(self.stabilisem([msg[0],msg[1],msg[2]+5*i]) ):
                self.buildinghight.publish(msg[2])
		print("got marker destination")
		print("got marker destination")
		print("got marker destination")
		print("got marker destination")
		print(self.setpoint3)
		self.to_activate.publish(True)
                break
	    else:
		print("marker not got")
		print("marker not got")
		print("marker not got")
		print("marker not got")
		continue

    def stabilisem(self,msg):
         '''
	Purpose:
	---
	<inorder to go and stabilise given a setpoint while landing>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < to know where to go >

	Example call:
	---
	<stabilisem(msg) >
        '''
	flag=0
	t0=0
	while True:
		self.gps_pos_setpoint=msg
		if self.isinbox():
			t0=time.clock()
			while(self.isinbox_2(4)):
			    self.run_pid()
			    if(calc_time(t0)>0.2):
				flag=1
				break
		if flag==1:
			return False

                if self.markerdetect==True:
                    self.setpoint3=copy.copy(self.gps_position)
		    print(self.setpoint3)
		    print(self.setpoint3)
                    return True

		self.run_pid()

    def whole_process(self,msg1,msg2,r):
         '''
	Purpose:
	---
	<master function which organises and calls all other functions>
        Input Arguments:
	---
	<msg1>` :  [ <list> ]
	    < start point >
        <msg2>` :  [ <list> ]
	    < destination point >

	Example call:
	---
	<whole_process(msg) >
        '''
	self.to_dest(msg1)
	while(True):
	  if self.check_box=="True":
	    self.isgrip=self.grip(True)
	    print("self.is_grip  ",self.isgrip)
	    print("self.is_grip  ",self.isgrip)
	    print("self.is_grip  ",self.isgrip)
	    print("self.is_grip  ",self.isgrip)
	    break

	  else:

		self.flight=True
		self.check(msg1)
		continue
	if r==0:
	   self.to_dest([msg2[0],msg2[1],msg2[2]+1])
	   self.goanddetect(msg2)
	   print("going to marker")
	   print("going to marker")
	   print("going to marker")
	   print("going to marker")
	   self.k=1
	   self.t=1
	   self.flight=True
	   self.stabilise(self.setpoint3)
	   self.setpoint5[0]=self.setpoint4[0]
	   self.setpoint5[1]=self.setpoint4[1]
	   print(self.setpoint3)
	   self.flight=False
	   self.stabilise([self.setpoint5[0],self.setpoint5[1],self.setpoint3[2] ])
	   self.flight=True
	   self.check( [ self.setpoint5[0] , self.setpoint5[1] , msg2[2] ])
	   self.isgrip=self.grip(False)

	if r==1:
	   self.to_dest([msg2[0],msg2[1],msg2[2]+0.5])
	   self.isgrip=self.grip(False)
		
	
    def to_dest(self,msg):
         '''
	Purpose:
	---
	<if a destination is given adjust height accordingly and goes there>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < destination point >
	Example call:
	---
	<to_dest(msg) >
        '''
	if(self.gps_position[2]<msg[2] and abs(self.gps_position[2]-msg[2])>0.2):
		self.flight=True
		setpoint_2=[edrone.gps_position[0],edrone.gps_position[1],msg[2]+1.5]
		self.check(setpoint_2)
		self.flight=False
		setpoint_2=[msg[0],msg[1],msg[2]+1]
		self.check(setpoint_2)
		self.flight=True
		setpoint_2=[msg[0],msg[1],msg[2]]
		self.check(setpoint_2)
	else:
    		self.flight=True
                h=copy.deepcopy(edrone.gps_position[2]+1)
    		setpoint_2=copy.deepcopy([edrone.gps_position[0],edrone.gps_position[1],h+2])
    		self.check(setpoint_2)
		self.flight=False
		setpoint_2=[msg[0],msg[1],h+2]
		self.check(setpoint_2)
		self.flight=True
		setpoint_2=[msg[0],msg[1],msg[2]]
		self.check(setpoint_2)
	
	
	
def calc_time(t0):
         '''
	Purpose:
	---
	<to calculate time>
        Input Arguments:
	---
	<t0>` :  [ <float> ]
	    < current time>
        
	Returns:
	---
	<elapsed_time >` :  [ < float> ]
	    < elapsed time>

	Example call:
	---
	<calc_time(msg) >
        '''
	t1=time.clock()
	elapsed_time=t1-t0
	return elapsed_time


def magnitude(msg):
         '''
	Purpose:
	---
	<to calculate magnitude of vector>
        Input Arguments:
	---
	<msg>` :  [ <list> ]
	    < vector>
        
	Returns:
	---
	<value >` :  [ < float> ]
	    < vector_magnitude>

	Example call:
	---
	< magnitude(msg) >
        '''
	return math.sqrt(math.pow(msg.x,2) + math.pow(msg.y,2))
            

if __name__ == '__main__':
    edrone = position()
    r = rospy.Rate(edrone.sample_time)  
    r.sleep()
    setpoint7=copy.copy(edrone.gps_position)
    print(setpoint7)
    j=0
    while(j>=0):
	remainder=j%2
	edrone.whole_process( finald[j] , finalr[j] , remainder )
	j+=1
    edrone.stabilise([setpoint7[0],setpoint7[1],edrone.gps_position[2] ])
    edrone.stabilise([setpoint7[0],setpoint7[1],setpoint7[2] ])
    print("end")
    print("end")
    print("end")
    print("end")

    


