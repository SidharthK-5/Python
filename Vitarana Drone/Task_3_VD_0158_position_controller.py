#!/usr/bin/env python


# Importing the required libraries

from vitarana_drone.msg import *
from pid_tune.msg import PidTune
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from sensor_msgs.msg import LaserScan
import rospy
import time
import tf
import math
import copy
PI=math.pi
r=None
k=None
t=None

class position():

    def __init__(self):
        rospy.init_node('position_control')      # initializing ros node with name drone_control


        self.gps_pos_setpoint= [0,0,0]
	self.gps_pos_setpoint_1=gps_cord()
	self.xy=plane()
	self.vector_point_1=plane()
	self.vector_point_2=plane()
	self.resultant=plane()
	self.tan_theta=0.0
	self.angle=0

	self.flight=None

	self.sensor_bottom=0.0

        self.path_pos=[0,0,0]
	self.gps_position_2=[0,0,0]
	self.gps_pos_setpoint= [0,0,0]
        self.gps_position = [0.0, 0.0, 0.0]
	self.setpoint3=[0,0,0]


        self.Kp = [170000, 170000, 25.11] #34.93
        self.Ki = [0, 0, 0.262]
        self.Kd = [500000, 500000,50] #34.93
 
	self.prev_values = [0,0,0]
	self.max_values = [1024, 1024, 1024, 1024]
	self.min_values = [0, 0, 0, 0]

	self.setpoint3=[0,0,0,0]
        self.setpoint4=[0,0,0,0]
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

        self.markerdetect=False
        self.pwm_cmd = prop_speed()
        self.pwm_cmd.prop1 = 0.0
        self.pwm_cmd.prop2 = 0.0
        self.pwm_cmd.prop3 = 0.0
        self.pwm_cmd.prop4 = 0.0

	self.Kp_1=5
	self.Kd_1=15
	self.Ki_1=0

        self.id_activate=Bool()
        # Publishers
	self.drone_command_pub = rospy.Publisher('/drone_cmd',edrone_cmd, queue_size=1)
	#self.gps_setpoint_pub = rospy.Publisher('/drone_cmd',, queue_size=1)
	#self.pwm_pub = rospy.Publisher('/edrone/pwm', prop_speed, queue_size=1)
	self.gps_error_zpub=rospy.Publisher('/z_error',ryp_error, queue_size=1)
        self.gps_error_latpub=rospy.Publisher('/lat_error',ryp_error, queue_size=1)
        self.gps_error_lonpub=rospy.Publisher('/lon_error',ryp_error, queue_size=1) 
	self.landing_pub=rospy.Publisher('landing',Float64, queue_size=1)
	self.to_path_pub=rospy.Publisher('to_path',gps_cord, queue_size=1)
	self.pass_id= rospy.Publisher('id', ryp_error , queue_size=1)
	self.to_activate = rospy.Publisher('condt', Bool, queue_size=1)
		

        # Subscribers
	#rospy.Subscriber('/edrone/range_finder_top', LaserScan, self.range_finder)
        #rospy.Subscriber('/edrone/gps', NavSatFix, self.drone_set_pos_callback)
        rospy.Subscriber('/edrone/gpsnew', NavSatFix, self.gps_callbacknew)

	#rospy.Subscriber('/pid_tuning_roll', PidTune, self.roll_set_pid)
        #rospy.Subscriber('/pid_tuning_pitch', PidTune, self.pitch_set_pid)
	rospy.Subscriber('/edrone/gps', NavSatFix, self.gps_callback)
	rospy.Subscriber('/gpsnew',gps_cord,self.path_callback)
	#rospy.Subscriber('/edrone/range_finder_bottom', LaserScan, self.range_bottom)
	rospy.Subscriber('/edrone/range_finder_bottom', LaserScan, self.range_bottom)
        rospy.Subscriber('/ismarker',Bool,self.ismarker)
        

    def range_bottom(self,msg):
	self.sensor_bottom=msg.ranges[0]
	#print("bottom sensor",self.sensor_bottom)
	
    def ismarker(self,msg):
        print("wow")
        self.markerdetect=msg.data

    def path_callback(self,msg):
	self.path_pos[0]=msg.latitude
	self.path_pos[1]=msg.longitude
	self.path_pos[2]=msg.altitude

    #def roll_set_pid(self,msg):
	#self.Kp[0]=msg.Kp*100
	#self.Kd[0]=msg.Kd*100
        #self.Ki[0]=msg.Ki*0.01
	#print("hai")
    #def pitch_set_pid(self,msg):
	#self.Kp[1]=msg.Kp*100
	#self.Kd[1]=msg.Kd*100
        #self.Ki[1]=msg.Ki*0.01
    def gps_callback(self, msg):

        self.gps_position[0] = msg.latitude
	self.gps_position[1] = msg.longitude
	self.gps_position[2] = msg.altitude
	#print(self.gps_position)


    def gps_callbacknew(self, msg):
        self.setpoint4[0] = msg.latitude
	self.setpoint4[1] = msg.longitude
	self.setpoint4[2] = msg.altitude

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
	self.gps_setpoint_passing()
        if(self.path_pos[2]!=1):	
	       self.to_path_pub.publish(self.gps_pos_setpoint_1)

	self.pos_error[2]=self.gps_position[2] - self.gps_pos_setpoint[2]
        self.pos_error[1]=(self.gps_position[1] - self.gps_pos_setpoint[1])
        self.pos_error[0]=(self.gps_position[0] - self.gps_pos_setpoint[0])
        self.iterm_latitude+=self.pos_error[0]
        self.iterm_longitude+=self.pos_error[1]
        self.iterm_altitude+=self.pos_error[2]

        self.pid_latitude=self.pos_error[0]*self.Kp[1] + (self.pos_error[0]-self.prev_pos_error[0]) * (self.sample_time) * self.Kd[1]
        self.pid_longitude=self.pos_error[1]*self.Kp[0] + (self.pos_error[1]-self.prev_pos_error[1]) * (self.sample_time) * self.Kd[0] 
        self.pid_throttle=self.pos_error[2]*self.Kp[2] + (self.pos_error[2]-self.prev_pos_error[2]) * (self.sample_time) * self.Kd[2]+(self.iterm_altitude*(self.Ki[2]))
	if( (self.gps_position[2]>self.gps_pos_setpoint[2]) and (self.prev_pos_error[2]-self.pos_error[2])>0.1 ):
	    #print("pid landing working")
	    #print((self.prev_pos_error[2]-self.pos_error[2]))
	    self.pid_landing=(25-self.sensor_bottom)*self.Kp_1 + (self.prev_sensor_bottom-self.sensor_bottom)*self.Kd_1 
	    #print("pid landing=",self.pid_landing)
	else:
	  if(self.gps_position[2]<self.gps_pos_setpoint[2]):
	    self.pid_landing=self.pid_landing/2
	  if(self.pid_landing<1):
	    self.pid_landing=0	
	    #print("self.pid_landing",self.pid_landing)
	    #print("self.pid_landing",self.pid_landing)
	    #print("self.pid_landing",self.pid_landing)

	self.landing_pub.publish(self.pid_landing)


	self.drone_cmd.rcThrottle=self.pid_throttle
        self.drone_cmd.rcRoll=-self.pid_latitude
        self.drone_cmd.rcPitch=-self.pid_longitude
        #print("i",self.iterm_latitude)
        #print(self.Ki[2],"int")
        #print("roll",self.drone_cmd.rcThrottle)
        #print(self.gps_position[0],"lat")
        if self.drone_cmd.rcRoll >10:
            self.drone_cmd.rcRoll=10
        if self.drone_cmd.rcRoll<-10:
            self.drone_cmd.rcRoll=-10
        if self.drone_cmd.rcPitch >10:
            self.drone_cmd.rcPitch=10
        if self.drone_cmd.rcPitch<-10:
            self.drone_cmd.rcPitch=-10

	self.prev_pos_error[2]=self.pos_error[2]
        self.prev_pos_error[1]=self.pos_error[1]
        self.prev_pos_error[0]=self.pos_error[0]
	self.prev_sensor_bottom=self.sensor_bottom
	
	#self.pwm_pub.publish(self.pwm_cmd)
	self.gps_error_zpub.publish(self.pid_throttle)
	self.landing_pub.publish(self.pid_landing)
        self.gps_error_latpub.publish(self.pos_error[0])
        self.gps_error_lonpub.publish(self.pos_error[1])
	#rospy.loginfo("running")

	self.drone_command_pub.publish(self.drone_cmd)

    def isinbox(self):
	if self.pos_error[0]>-0.000004517 and self.pos_error[0]<0.000004517 and self.pos_error[1]>-0.0000047487 and self.pos_error[1]<0.0000047487 and self.pos_error[2]>-0.2 and self.pos_error[2]<0.2:
	    return True

    def isinbox_1(self,k):
	if self.pos_error[0]>-0.000004517*k and self.pos_error[0]<0.000004517*k and self.pos_error[1]>-0.0000047487*k and self.pos_error[1]<0.0000047487*k and self.pos_error[2]>-0.2 and self.pos_error[2]<0.2:
	    return True

    def isinbox_2(self,k):
	if self.pos_error[0]>-0.000004517*k and self.pos_error[0]<0.000004517*k and self.pos_error[1]>-0.0000047487*k and self.pos_error[1]<0.0000047487*k and self.pos_error[2]>-0.2*k and self.pos_error[2]<0.2*k:
	    return True

        
    def run_pid(self):
	    global r		
	    self.pid_position() 
	    #print("gps setpoint",self.gps_pos_setpoint)
            r.sleep()

    def check_wave(self,msg):
	#print("inside check wave")
	#print("Msg",msg)
	if(self.flight==False):
		while(self.wavepoint(msg)!=True and self.flight==False):
			if(self.stabilise(self.gps_position_2)==True):
				continue
			else:
				return False
		#print("if else is running inside check_wave")
		if(self.stabilise(self.gps_position_2)==True):
				return True
		else:
				return False
		

	else:
	 if(self.flight==True):
		self.k=1
		self.t=1
		#print("working")
		if(self.stabilise(msg)==True):
			return True
		else:
			return False

    def stabilise(self,msg):
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
		
                                                            
    def stabilisem(self,msg,finish):
	flag=0
	t0=0
	while True:
		self.gps_pos_setpoint=msg
		if self.isinbox():
			t0=time.clock()
			while(self.isinbox_2(1)):
			    self.run_pid()
			    if(calc_time(t0)>0.5):
				flag=1
				break
                if self.markerdetect==True:
                    self.setpoint3=(self.gps_position)
                    finish=1
                    break
		if flag==1:
			return True

		self.run_pid()    

       
    def goanddetect(self,setp):
        finish=0
        for i in range(5):
            self.stabilisem([setp[0],setp[1],setp[2]+i*5],finish)
            if finish==1:
                #self.id_activate.data=True
                self.to_activate.publish(True)
		self.to_activate.publish(True)
		time.sleep(1)
                break
                                                              
    def stabilise_1(self,msg):
	flag=0
	t0=0
	while True:
		self.gps_pos_setpoint=msg
		if self.isinbox_1(3):
			t0=time.clock()
			while(self.isinbox_1(3)):
			    self.run_pid()
			    #print("path called")
			    if(calc_time(t0)>0.5):
				flag=1
				break
		if flag==1:
			break
		#print("path called")
		self.run_pid()
                                                                                  
                         
    def wavepoint(self,msg):
	#print("inside wavepoint")
	#print("msg",msg)
	self.gps_to_xy(self.vector_point_1,self.gps_position)
	self.gps_to_xy(self.vector_point_2,msg)
	self.xy.x=self.vector_point_2.x-self.vector_point_1.x
	self.xy.y=self.vector_point_2.y-self.vector_point_1.y
	#print("x= ",self.xy.x)
	#print("y= ",self.xy.y)
	if (magnitude(self.xy)>30):
		self.xy.x=( self.xy.x/magnitude(self.xy) )*3
		self.xy.y=( self.xy.y/magnitude(self.xy) )*3
		#print("self.xy.x",self.xy.x)
		#print("self.xy.y",self.xy.y)
		self.xy_to_gps(msg)
		self.k=4
		self.t=0.2
		return False
	else:
		#print("else of wave point running")
		self.k=1
		self.t=1
		self.xy_to_gps(msg)
		return True

    '''def wavepoint_height(self,msg):
	if (self.gps_position[2]-msg[2]>7):
		self.stabilise(
	else:
		#print("else of wave point running")
		self.k=1
		self.t=1
		self.xy_to_gps(msg)
		return True'''
	
		
                                           
    def xy_to_gps(self,msg):
	#print("xy to gps working")
	#print("msg",msg)
	self.resultant.x=self.vector_point_1.x+self.xy.x
	self.resultant.y=self.vector_point_1.y+self.xy.y
	self.gps_position_2[0]=(self.resultant.x/110692.0702932625) + 19
	self.gps_position_2[1]=(-self.resultant.y/105292.0089353767) + 72
	self.gps_position_2[2]=msg[2]
	print("gps position 2 = ",self.gps_position_2)


    def gps_to_xy(self,msg1,msg2):
	#print("gps to xy working")
	msg1.x=110692.0702932625 * (msg2[0] - 19)
	msg1.y=-105292.0089353767 * (msg2[1] - 72)
	print("x cord",msg1.x)
	print("y cord",msg1.y)
	
	
    def check(self,msg):
	self.gps_pos_setpoint=msg
	self.gps_setpoint_passing()
	self.to_path_pub.publish(self.gps_pos_setpoint_1)
	while(True):
	  if(self.path_pos[2]==1 and self.flight==False):
                print("path called")
		self.stabilise_1([self.path_pos[0],self.path_pos[1],self.gps_pos_setpoint[2]])
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
	
	
def calc_time(t0):
	t1=time.clock()
	elapsed_time=t1-t0
	return elapsed_time


def magnitude(msg):
	return math.sqrt(math.pow(msg.x,2) + math.pow(msg.y,2))
            

if __name__ == '__main__':
    edrone = position()
    act=False
    r = rospy.Rate(edrone.sample_time)  
    iter_i=0
    id_list=[3,1,2]
    listofsetpoint=[[18.9993675932,72.0000569892,10.7],[18.9990965928,72.0000664814,10.75],[18.9990965925,71.9999050292,22.4]]
    r.sleep()
    edrone.pass_id.publish(id_list[iter_i])
    edrone.flight=True
    edrone.to_activate.publish(False)
    setpoint_2=[edrone.gps_position[0],edrone.gps_position[1],edrone.gps_position[2]+1]
    edrone.check(setpoint_2)
    setpoint=[0,0,0]
    for setpoint in listofsetpoint:
	#edrone.id_activate.data=False
        edrone.to_activate.publish(False)
        edrone.pass_id.publish(id_list[iter_i])
	iter_i+=1

	if(edrone.gps_position[2]<setpoint[2]):
		edrone.flight=True
		setpoint_2=[edrone.gps_position[0],edrone.gps_position[1],setpoint[2]+1]
		edrone.check(setpoint_2)
		setpoint_2=[setpoint[0],setpoint[1],setpoint[2]+1]
		edrone.flight=True
		edrone.check(setpoint_2)
		#print("second setpoint running")
		#print("second setpoint running")
		#print("second setpoint running")
		setpoint_2=[setpoint[0],setpoint[1],setpoint[2]+1-0.2]
		edrone.flight=True
		edrone.check(setpoint_2)
		act=True
		#print(setpoint_2)

	else:
		edrone.flight=True
		setpoint_2=[setpoint[0],setpoint[1],edrone.gps_position[2]]
		edrone.check(setpoint_2)
		setpoint_2=[setpoint[0],setpoint[1],setpoint[2]+1]
		edrone.flight=True
		edrone.check(setpoint_2)
    
		
	edrone.flight=True	
        edrone.goanddetect([setpoint[0],setpoint[1],setpoint[2]+1])
	edrone.to_activate.publish(True)
	edrone.flight=True
	setpoint_2=[edrone.setpoint3[0],edrone.setpoint3[1],edrone.setpoint3[2]]
	edrone.check(setpoint_2)
	edrone.flight=True
	setpoint_2=[edrone.setpoint4[0],edrone.setpoint4[1],edrone.setpoint3[2]]	
	edrone.check(setpoint_2)
	edrone.flight=True
	if(act==True):
            setpoint_2=[edrone.setpoint4[0],edrone.setpoint4[1],edrone.setpoint3[2]-3]
	    edrone.check(setpoint_2)
            setpoint_2=[edrone.setpoint4[0],edrone.setpoint4[1],edrone.setpoint3[2]-6]
            edrone.check(setpoint_2)
	else:		
    	    setpoint_2=[edrone.setpoint4[0],edrone.setpoint4[1],edrone.setpoint3[2]-6]
	    edrone.check(setpoint_2)


    setpoint_2=[edrone.setpoint4[0],edrone.setpoint4[1],setpoint[2]]
    edrone.flight=True
    edrone.check(setpoint_2)


		



