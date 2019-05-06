import pandas as pd
import numpy as np

class SimpleNeuralNetwork(object):
  def __init__(self):
    np.random.seed(1)
    self.synaptic_weights = []

  def __sigmoid(self, x, deriv=False):
    if deriv == True:
      return x * (1-x)
    return 1 / (1 + np.exp(-x))
  
  def predict(self, x):
    predicted = np.dot(x, self.synaptic_weights)
    return self.__sigmoid(predicted)

  def train(self, file, X, y, iterations):
    dim = file.shape #Return dimensions of the file, say (m,n)
    self.synaptic_weight = 2 * np.random.random((dim[1] - 1, 1)) - 1 #shape of weight matrix is (n,1)
        
    for i in range(iterations):
      output = self.predict(X) #Product of training_inputs and weight matrix
      error = y - output       
            
      adjustment = np.dot(X.T, error * self.__sigmoid(output, deriv=True))
      self.synaptic_weight += adjustment

if __name__ == "__main__":
  # Loading Data
  data = pd.read_csv("file.csv")
  display(len(data))
  
  X = data.iloc[:, 0:4].values #features
  y = data.iloc[:, [4]].values #labels
  number_of_iterations = 6000
  clf = SimpleNeuralNetwork()
  
  #Training
  clf.train(data, X, y, number_of_iterations)
  
  #Testing
  prediction = np.array([0,1,1,0])
  res = clf.predict(prediction)[0]

  #Threshold value check
  if res >= 0.5:
    print("Prediction:", 1)
  else:
    print("Prediction:", 0)