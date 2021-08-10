class SISO:
    """
    Single input Single output Neural Network
    """
    #class variables
    weight = 0.0
    ALPHA = 0.1
    TARGET = 12
    input_x = 0.0
    

    def __init__(self, weight, input_x):
        self.weight = float(weight)
        self.input_x = float(input_x)


    def input_node(self, input_x):
        return float(input_x)


    def predict(self, input_x):
        return input_x * self.weight


    def compare(self, predicted_y1):
        return self.TARGET - predicted_y1


    def gd_learn(self, weight, delta):
        w_new = weight + self.ALPHA
        new_y = w_new * input_x
        error_up = self.compare(new_y)

        w_new = weight - self.ALPHA
        new_y = w_new * input_x
        error_down = self.compare(new_y)

        if error_down < error:
            de
            

    def __repr__(self):
        return f'''
        A SISO object with following variables
        weight: {self.weight}
        Alpha value: {self.ALPHA}
        '''


def train_NN(weight, y, epochs):
    # initially adjusted weight will be weight itself, then after an epoch we get the new weight and feed the same to the network
    adjusted_weight = weight

    # Loop through given number of epochs until we find no difference in the delta value (indicating learning complete)
    for i in range(epochs):
        siso = SISO(adjusted_weight, input_x)
        print(siso)
        input_x = siso.input_node(input_x)
        y1 = siso.predict(input_x)
        delta = siso.compare(y1)
        if delta == 0.00:
            break
        adjusted_weight = siso.learn(adjusted_weight, delta)
        print(f'{i+1} --> x: {input_x}, y1: {y1}, delta: {delta:.2f}, weight: {weight}, adjusted weight: {adjusted_weight}')


weight = 20
input_x = 10
epochs = 100
train_NN(weight, input_x, epochs)
