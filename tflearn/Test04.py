import tensorflow as tf
# give it's value when sess.run()
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.matmul(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))