import rclpy
from rclpy.node import Node
from person_msgs.msg import Person   #変更: 作ったPerson型を使う

rclpy.init()
node = Node("listener")


def cb(msg):
    node.get_logger().info("Listen: %s" % msg)   #変更: メッセージ全体を文字列で表示


def main():
    sub = node.create_subscription(Person, "person", cb, 10)   #変更: 型とトピック名
    rclpy.spin(node)
