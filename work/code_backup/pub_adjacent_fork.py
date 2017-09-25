#!/usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseWithCovariance
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist
from math import sin,cos,asin,acos,atan2
import tf
global adjacent_goal
global fork_posex
flag1=True
dist=0.2 #1.5
rospy.init_node("adjacent_pallet")
relative_palltet_pose_sub=rospy.Subscriber("fine_pallet_pose",PoseStamped,pallet_pose_callback)
goal_pub=rospy.Publisher("move_base_simple/goal",PoseStamped,queue_size=1)
vel_pub=rospy.Publisher("cmd_vel",Twist,queue_size=1)
current_fork_pose_sub=rospy.Subscriber("odometry/filtered/pose",PoseWithCovarianceStamped,fork_pose_callback)

def pallet_pose_callback(pose):
	angle=atan2(pose.pose.orientation.z,pose.pose.orientation.w)*2
	posx=pose.pose.position.x
	posy=pose.pose.position.y

	quad=(
			pose.pose.orientation.x,
			pose.pose.orientation.y,
			pose.pose.orientation.z,
			pose.pose.orientation.w
		)
		
	meuler=tf.transformations.euler_from_quaternion(quad)
	mroll=meuler[0]
	mpitch=meuler[1]
	myaw=meuler[2]+3.14
	newquad=tf.transformations.quaternion_from_euler(mroll,mpitch,myaw)

	mtrans=np.mat([[cos(angle),-sin(angle),posx],
				[sin(angle),cos(angle),posy],
				[0,0,1]])

	mpos=np.mat([[-dist],
					 [0],
					 [1]])

	newpos=mtrans*mpos
		#print(newpos)

	adjacent_goal=newpos.A[0][0]

def fork_pose_callback(pose):
	fork_posex=pose.pose.position.x
	if fork_posex<adjacent_goal & flag1
		flag1=False
		vel_trans=Twist()
		vel_trans.linear.x=0.1
		vel_trans.linear.y=0.0
		vel_trans.angular.z=0.0
		vel_trans.angular.w=1.0
		vel_pub.publish(Twist)
	if fork_posex>=adjacent_goal
		vel_trans.linear.x=0.0
		vel_pub.publish(Twist)

		



		

	

   

def pallet_pose_callback(pose):
	global is_running
	if not is_running:
		is_running=True
		angle=atan2(pose.pose.orientation.z,pose.pose.orientation.w)*2
		posx=pose.pose.position.x
		posy=pose.pose.position.y

		quad=(
			pose.pose.orientation.x,
			pose.pose.orientation.y,
			pose.pose.orientation.z,
			pose.pose.orientation.w
		)
		
		meuler=tf.transformations.euler_from_quaternion(quad)
		mroll=meuler[0]
		mpitch=meuler[1]
		myaw=meuler[2]+3.14
		newquad=tf.transformations.quaternion_from_euler(mroll,mpitch,myaw)

		mtrans=np.mat([[cos(angle),-sin(angle),posx],
				[sin(angle),cos(angle),posy],
				[0,0,1]])

		mpos=np.mat([[-dist],
					 [0],
					 [1]])

		newpos=mtrans*mpos
		#print(newpos)

		goal=PoseStamped()
		goal.header.frame_id="base_laser_down"
		goal.header.stamp=rospy.Time.now()
		goal.pose.position.x=newpos.A[0][0]
		goal.pose.position.y=newpos.A[1][0]
		goal.pose.orientation.z=newquad[2] #-pose.pose.orientation.z
		goal.pose.orientation.w=newquad[3]#pose.pose.orientation.w


		print(goal)
		goal_pub.publish(goal)

	

rospy.init_node("fork_pallet")
relative_palltet_pose_sub=rospy.Subscriber("fine_pallet_pose",PoseStamped,pallet_pose_callback)

rospy.spin()

# pub=rospy.Publisher("move_base_simple/goal",PoseWithCovarianceStamped,queue_size=1)
# rospy.init_node("pose_trigger_pub",anonymous=True)n
# pose=PoseWithCovarianceStamped()
# pose.header.frame_id="base_laser_down"
# pose.pose.covariance[0]=0.06;
# pose.pose.covariance[7]=0.18;
# pose.pose.pose.position.x=1.1;
# pose.pose.pose.position.y=0.0;
# pose.pose.pose.orientation.z=0.0;
# pose.pose.pose.orientation.w=0.1;
# rate=rospy.Rate(0.1);

# while not rospy.is_shutdown():
# 	print("publishing")
# 	pub.publish(pose)
# 	rate.sleep()