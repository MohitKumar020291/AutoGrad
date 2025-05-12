import warnings
import numpy as np
from typing import Optional, Union
from neuron_backprop import Neuron, Value

class Linear:
    def __init__(
        self,
        fan_in,
        fan_out
        ):
        self.fan_in = fan_in
        self.fan_out = fan_out
        self.layers = []
    
    def forward(
        self,
        prev_data: Union[list[Neuron], list[Value]],
        weights: Optional[list] = None
        ):
        self.data = prev_data
        if weights:
            if len(weights) != self.fan_in:
                raise Exception(f'''
                    the length of previous data = {self.fan_in} and the #weights of a neuron = {len(weights)}, it 
                    is a mismatch - the error could be easily solved by providing the correct shaped weights! 
                    ''')
            else:
                #to numpy
                if not isinstance(weights, np.ndarray):
                    self.weights = np.array(weights)
        else:
            #generate weights
            self.weights = np.random.randn(self.fan_in, self.fan_out)

        if not isinstance(prev_data[0], list):
            pass
        else:
            for chunk in self.data:
                chunk = np.array(chunk)
                # for neuron_idx in range(self.fan_out):
                #     neuron_weights = self.weights[:, neuron_idx]
                #     neuron


datas = [[1,2], [3,4], [5,6], [7,8]]
for i, data in enumerate(datas):
    for j, dp in enumerate(data):
        value = Value(dp)
        datas[i][j] = value

# previous_neurons = [] #let's make some neurons
weights = [[1,2,3], [4,5,6]]
l = Linear(2, 3)
l.forward(prev_data=datas)