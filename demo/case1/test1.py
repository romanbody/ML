import numpy as np
import matplotlib.pyplot as plt

def thang(x):
    return x*x 

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class test:

    def aa(self):
        self.output = 1


class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4) 
        self.weights2   = np.random.rand(4,1)                 
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


if __name__ == "__main__":
    steps = []
    X = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
    y = np.array([[0],[1],[1],[0]])
    nn = NeuralNetwork(X,y)
    
    for i in range(400):
        nn.feedforward()
        nn.backprop()
        if (i % 10) == 0:
            #print(nn.output) 
            steps.append(nn.output)

    #print(nn.output)

    fig = plt.figure()

    ax = fig.add_subplot(2, 1, 1,title='Sample ANN')

    #ax.plot(steps)
    mat = np.array(steps)
    ax.plot(mat[:,0],'b--')
    ax.plot(mat[:,1],'g')
    ax.plot(mat[:,2],'r--')
    ax.plot(mat[:,3],'y')
    plt.show()