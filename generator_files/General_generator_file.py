
from generator_files.adder_gen import AdderGenClass
from generator_files.table_gen import TableGenClass

#getattr(o, name)()
class GeneralGenerator:
    def __init__(self):
        self.adder_gen_class = AdderGenClass()
        self.table_gen_class = TableGenClass()


    def adder_gen(self, parameters=['8', '0'], inputs={'a':'signal1', 'b':'signal2'}, outputs={'c':'signal3'}, showconfig=0):
        if showconfig:
            return (self.adder_gen_class.input_ports, self.adder_gen_class.output_ports)
        return self.adder_gen_class.adder_gen(parameters, inputs, outputs)

    def table_gen(self,parameters, inputs, outputs, showconfig):
        if showconfig:
            return (self.table_gen_class.input_ports, self.table_gen_class.output_ports)
        return self.table_gen_class.table_gen(parameters, inputs, outputs)