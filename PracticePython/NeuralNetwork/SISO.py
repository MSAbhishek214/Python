class SISO:
    """
    Single input Single output Neural Network
    """
    #class variables
    weight = 0.0
    input_x = 0.0
    ALPHA = 0.1
    output_y = 0.0
    

    def __init__(self, weight, output_y):
        self.weight = float(weight)
        self.output_y = float(output_y)


    def input_node(self, input_x):
        return float(input_x)


    def predict(self, input_x):
        return input_x * self.weight


    def compare(self, y, y1):
        return y - y1


    def learn(self, weight, alpha, delta):
        return weight + alpha * delta


def train():
    weight = 0.85
    y = 12
    siso = SISO(weight, y)
    x = siso.input_node(10)
    y1 = siso.predict(x)