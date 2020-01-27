# -*- coding: utf-8 -*-
"""play_with_tf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDa33WTvXtIIVcKLJHWSrCTT8goRGDjI
"""

import tensorflow as tf
import numpy as np 
import pandas as pd 
import seaborn as sns 
import logging
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

"""# Function to convert"""

def cels_to_fahr(cels):
    return 1.8*cels + 32

# change 10000 to something smaller (e.g. 500) if not running on Cloud Notebook
celsius_train = 100*np.random.rand(10000, 1)
fahrenheit_train = np.apply_along_axis(cels_to_fahr, 0, celsius_train)

"""# Setup neural network layer"""

layer_0 = tf.keras.layers.Dense(units=1, input_shape=[1])

"""# Initialize the model & setup layer"""

model = tf.keras.Sequential([layer_0])
learn_rate = 0.1
epoch=500
model.compile(loss='mean_squared_error',
             optimizer=tf.keras.optimizers.Adam(learn_rate))

"""# Train the model"""

trained_model = model.fit(celsius_train, fahrenheit_train, epochs=epoch, verbose=False)

"""# Plot using seaborn
Seaborn expects a dataframe
"""

loss = trained_model.history['loss']
epoch_label = [x for x in range(epoch)]
loss_df = pd.DataFrame(list(zip(loss, epoch_label)), columns=['Loss', 'Epoch'])

loss_df

sns.set(style="darkgrid")
sns.lineplot(x="Epoch", y="Loss", data=loss_df)

