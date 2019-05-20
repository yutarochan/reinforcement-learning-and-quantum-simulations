import numpy as np
#  np.random.seed(42)
import tensorflow as tf
#  tf.set_random_seed(30)
#  from tf import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
#  from tensorflow.keras.utils import plot_model
import tensorflow.keras.backend as K
import matplotlib as m
m.use('TkAgg')
#  import matplotlib.pyplot as plt

print(tf.__version__)

train = np.array([np.random.rand(2) for _ in range(10)])
labels = np.array([np.random.randint(2) for _ in range(10)])

np.random.seed(100)
tf.set_random_seed(42)
model = Sequential([
    Dense(3, input_shape=(4,), activation='tanh'),
    Dense(2, activation='relu'),
    Dense(1)
])


#  print(model.get_weights())
#  weights1 = np.array([np.array([[0, 0, 0], [0, 0, 0]]),
#                       np.array([1, 0, 0]),
#                       np.array([[0, 1], [0, 0], [0, 0]])
#  model = keras.models.Sequential([
#      #  keras.layers.Flatten(input_shape=(5,)),
#      keras.layers.Dense(7, activation=tf.nn.relu),
#      keras.layers.Dense(2, activation=tf.nn.softmax)
#  ])


#  def mean_pred(y_true, y_pred):
#      return K.mean(y_pred)


#  model.compile(optimizer='adam', loss='mean_squared_error')
#  metrics=['accuracy'])

output = model.outputs
input = model.inputs
weights = model.trainable_weights
gradient = K.gradients(output, weights)
input_gradient = K.gradients(output, input)[0][0, 1:4]
hess = [K.gradients(input_gradient[i], input)[0][0, 1:4] for i in range(3)]


sess = K.get_session()
weights1 = np.array([np.array([[1, 2, 1], [2, 4, 0], [1, 6, -9], [0.5, 4, 0]]),
                     np.array([0, 0, 0]),
                     np.array([[1, 1], [2, 3], [1.3, -9.5]]),
                     np.array([0, 0]),
                     np.array([[1.5], [1]]),
                     np.array([0.5])]) * 0.5

model.set_weights(weights1)

#  sess = K.get_session()


def evaluate(f, input_):
    return sess.run(f, feed_dict={model.input: np.array([input_])})


#  ev = evaluate(gradient, [2, 3])

#  ev2 = sess.run(gradient, feed_dict={model.input: np.array([[2, 3]])})


#  print(sess.run(gradient, feed_dict={model.input: np.array([[2, 3]])}))

#  gradient_ev = np.array(
#      sess.run(gradient, feed_dict={model.input: np.array([[2, 3]])})
#  )

#  #  weights2 = [np.array([[0, 2, 0], [0, 4, 0]]),
#  #              np.array([1, 0, 0]),
#  #              np.array([[0, 1], [3, 0], [0, 0]]),
#  #              np.array([0, 0])]

#  model.set_weights(weights1 + 0.2 * gradient_ev)

#  print(sess.run(gradient, feed_dict={model.input: np.array([[2, 3]])}))
#  #  model.fit(train, labels, epochs=5)
