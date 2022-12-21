
from generator_files.adder_gen import AdderGenClass

#getattr(o, name)()
class GeneralGenerator:
    def __init__(self):
        self.adder_gen_class = AdderGenClass()

    def adder_gen(self, parameters=['8', '0'], inputs={'a':'signal1', 'b':'signal2'}, outputs={'c':'signal3'}, showconfig=0):
        if showconfig:
            return (self.adder_gen_class.input_ports, self.adder_gen_class.output_ports)
        return self.adder_gen_class.adder_gen(parameters, inputs, outputs)


