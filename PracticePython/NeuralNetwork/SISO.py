class SISO:
    """
    Single input Single output Neural Network
    """
    #class variables
    weight = 0.0
    ALPHA = 0.1
    output_y = 0.0
    

    def __init__(self, weight, output_y):
        self.weight = float(weight)
        self.output_y = float(output_y)


    def input_node(self, input_x):
        return float(input_x)


    def predict(self, input_x):
        return input_x * self.weight


    def compare(self, output_y, predicted_y1):
        return output_y - predicted_y1


    def learn(self, weight, delta):
        return weight + self.ALPHA * delta


def train_NN(weight, y, epochs):
    adjusted_weight = weight
    for i in range(epochs):
        siso = SISO(adjusted_weight, y)
        input_y = siso.input_node(y)
        y1 = siso.predict(input_y)
        delta = siso.compare(y, y1)
        if delta == 0.00:
            break
        adjusted_weight = siso.learn(adjusted_weight, delta)
        print(f'{i} --> y: {input_y}, y1: {y1}, delta: {delta:.2f}, weight: {weight}, adjusted weight: {adjusted_weight}')


weight = 0.1
y = 12
epochs = 10000000000000000000000
train_NN(weight, y, epochs)
