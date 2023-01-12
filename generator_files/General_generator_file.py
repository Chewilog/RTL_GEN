
from generator_files.adder_gen import AdderGenClass
from generator_files.table_gen import TableGenClass
from generator_files.unite_in_array import UniteInArrayClass
from generator_files.splitter import SplitterClass
from generator_files.and2 import And2Class

#getattr(o, name)()
class GeneralGenerator:
    def __init__(self):
        self.adder_gen_class = AdderGenClass()
        self.table_gen_class = TableGenClass()
        self.unite_in_array_class = UniteInArrayClass()
        self.splitter_class = SplitterClass()
        self.and2_class = And2Class()

    def and2(self,parameters=[],inputs={'a':'signal1','b':'signal2'},outputs={'c':'signal3'}, showconfig=0):
        if showconfig:
            return (self.and2_class.input_ports, self.and2_class.output_ports)
        return self.and2_class.and2(parameters, inputs, outputs)

    def adder_gen(self, parameters=['8', '0'], inputs={'a':'signal1', 'b':'signal2'}, outputs={'c':'signal3'}, showconfig=0):
        if showconfig:
            return (self.adder_gen_class.input_ports, self.adder_gen_class.output_ports)
        return self.adder_gen_class.adder_gen(parameters, inputs, outputs)

    def table_gen(self, parameters=[], inputs={}, outputs={}, showconfig=0):
        if showconfig:
            return (self.table_gen_class.input_ports, self.table_gen_class.output_ports)
        return self.table_gen_class.table_gen(parameters, inputs, outputs)

    def unite_in_array(self, parameters=[], inputs={}, outputs={}, showconfig=0):
        if showconfig:
            return (self.unite_in_array_class.input_ports, self.unite_in_array_class.output_ports)
        return self.unite_in_array_class.unite_in_array(parameters, inputs, outputs)

    def splitter(self, parameters=[], inputs={'a': 'signal1'}, outputs={'b': 'signal2', 'c': 'signal3'}, showconfig=0):
        if showconfig:
            return (self.splitter_class.input_ports, self.splitter_class.output_ports)
        return self.splitter_class.splitter(parameters, inputs, outputs)