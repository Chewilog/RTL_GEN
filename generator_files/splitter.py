class SplitterClass():
    def __init__(self):
        self.input_ports = {'a':'std_logic_vector(31 downto 0)'}
        self.output_ports = {'b':'std_logic_vector(15 downto 0)','c':'std_logic_vector(15 downto 0)'}

    def splitter(self,parameters=[],inputs={'a':'signal1'},outputs={'b':'signal2','c':'signal3'}):
        entity='\n\n'
        entity+=outputs['b'] + '<=' + inputs['a']+'(31 downto 16);\n'
        entity+=outputs['c'] + '<=' + inputs['a']+'(15 downto 0);\n'
        return entity

# a = SplitterClass()
# print(a.splitter() )