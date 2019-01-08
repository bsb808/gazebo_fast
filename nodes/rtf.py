import rospy
from rosgraph_msgs.msg import Clock
import time

t0 = time.time()
s0 = 0.0
cnt = 1
def callback(msg):
    global t0
    global s0
    global cnt
    if bool(cnt%10000):
        cnt += 1
        return
    cnt = 1
    # Wall clock
    now = time.time()
    dwall = now-t0
    t0 = now
    # Sim clock
    now = msg.clock.secs+float(msg.clock.nsecs)/1.0e9
    dsim = now-s0
    s0 = now
    print("%.1f"%(dsim/dwall))
    
def listener():
    rospy.init_node('node_name')
    rospy.Subscriber("clock", Clock, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
