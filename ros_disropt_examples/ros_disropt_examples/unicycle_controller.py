import rclpy
from rclpy.node import Node
from ros_disropt.controller import UnicycleVelocityController



def main():
    rclpy.init(args=None)

    pos_handler = 'pubsub'
    pos_topic = 'odom'


    controller = UnicycleVelocityController(pos_handler, pos_topic)
    rclpy.spin(controller)
