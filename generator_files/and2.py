class And2Class:
    def __init__(self):
        self.input_ports = {'a':'std_logic', 'b':'std_logic'}
        self.output_ports = {'c':'std_logic'}

    def and2(self,parameters=[],inputs={'a':'signal1','b':'signal2'},outputs={'c':'signal3'}):
        entity = '\n\n'
        entity += outputs['c']+'<='+inputs['a']+" and "+inputs['b']+';\n\n'
        return entity

# a = And2Class()
# print(a.and2())