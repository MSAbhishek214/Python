class SISO:
    """
    Single input Single output Neural Network
    """
    #class variables
    weight = 0.0
    ALPHA = 0.1
    actual_y = 12
    

    def __init__(self, weight):
        self.weight = float(weight)


    def input_node(self, input_y):
        return float(input_y)


    def predict(self, input_y):
        return input_y * self.weight


    def compare(self, given_y, predicted_y1):
        return given_y - predicted_y1


    def learn(self, weight, delta):
        return weight + self.ALPHA * delta


    def __repr__(self):
        return f'''
        A SISO object with following variables
        weight: {self.weight}
        Alpha value: {self.ALPHA}
        actual value of y: {self.actual_y}
        '''


def train_NN(weight, y, epochs):
    # initially adjusted weight will be weight itself, then after an epoch we get the new weight and feed the same to the network
    adjusted_weight = weight

    # Loop through given number of epochs until we find no difference in the delta value (indicating learning complete)
    for i in range(epochs):
        siso = SISO(adjusted_weight)
        print(siso)
        input_y = siso.input_node(y)
        y1 = siso.predict(input_y)
        delta = siso.compare(y, y1)
        if delta == 0.00:
            break
        adjusted_weight = siso.learn(adjusted_weight, delta)
        print(f'{i+1} --> y: {input_y}, y1: {y1}, delta: {delta:.2f}, weight: {weight}, adjusted weight: {adjusted_weight}')


weight = 21
given_y = 21
epochs = 1000000
train_NN(weight, given_y, epochs)
