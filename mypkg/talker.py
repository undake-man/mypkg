import rclpy
from rclpy.node import Node
from person_msgs.msg import Person   #変更: 作ったPerson型を使う

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)   #変更: 型とトピック名
n = 0


def cb():
    global n
    msg = Person()          #変更: Person型のメッセージを作る
    msg.name = "後藤行稀"    #変更: msgファイルに書いた「name」
    msg.age = n % 256       #変更: msgファイルに書いた「age」（0〜255まで）
    pub.publish(msg)
    n += 1

def main():
    node.create_timer(0.5, cb)  #0.5秒ごとにcbを呼ぶタイマー
    rclpy.spin(node)            #実行（無限ループ。タイマーや送受信を処理し続ける）
