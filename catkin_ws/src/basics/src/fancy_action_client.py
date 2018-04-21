#!/usr/bin/env python
import rospy
import time
import actionlib
from basics.msg import TimerAction, TimerGoal, TimerResult,TimerFeedback

def feedback_cb(feedback):
    print('[Feedback] Time elapsed: %f'%(feedback.time_elapsed.to_sec()))
    print('[Feedback] Time remaining: %f'%(feedback.time_remaining.to_sec()))

rospy.init_node('timer_acttion_client')
client=actionlib.SimpleActionClient('timer',TimerAction)
client.wait_for_server()
goal=TimerGoal()
goal.time_to_wait=rospy.Duration.from_sec(500.0)

client.send_goal(goal,feedback_cb=feedback_cb)
#time.sleep(1.0)
#client.send_goal(goal,feedback_cb=feedback_cb)

client.wait_for_result()

print('[Result] State: %d'%(client.get_state()))
print('[Result] Status: %s'%(client.get_goal_status_text()))
print('[Result] Time elapsed: %f'%(client.get_result().time_elapsed.to_sec()))
print('[Result] updates_sent: %d'%(client.get_result().updates_sent))
