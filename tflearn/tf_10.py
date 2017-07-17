import tensorflow as tf
import numpy as np

# W = tf.Variable([[1, 2, 3], [3, 4, 5]], dtype=tf.float32, name='weright')
# b = tf.Variable([[1, 2, 3]], dtype=tf.float32, name='biases')
#
# init = tf.initialize_all_variables()
# saver = tf.train.Saver()
# with tf.Session() as sess:
#     sess.run(init)
#     save_path = saver.save(sess, "my_net/save_net.ckpt")
#     print("Save to path", save_path)

# 读取这个储存的文件以后，需要重新定义这个网络的文件 不需要init
W2 = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name='weright')
b2 = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name='biases')

saver2 = tf.train.Saver()
with tf.Session() as sess:
    saver2.restore(sess,"my_net/save_net.ckpt")
    print("weights:",sess.run(W2))
    print("weights:",sess.run(b2))
