
class AdderGenClass():
    def __init__(self):
        self.input_ports={'a':'std_logic_vector(7 downto 0)', 'b':'std_logic_vector(7 downto 0)'}
        self.output_ports={'c':'std_logic_vector(7 downto 0)'}
    def adder_gen(self,parameters=['8', '0'], inputs={'a':'signal_name', 'b':'signal_name2'},outputs={'c':'signal_name3'}):#N_of_bits-> adder number of bits; carry-> 0=not carry, 1=carry; register-> 0=do not register, 1=register output
        entity = ''
        entity+='process('
        for i in inputs.values():
            entity+=i+','



        for i in outputs.values():
            entity += i +','
        entity = entity[:-1] + ')\n'
        entity+='begin\n'
        entity += '   ' + outputs['c'] + '<= '
        for i in inputs.values():
            entity+= 'unsigned('+i+')'+'+'

        entity = entity[:-1] +';'

        entity+='\nend process;\n'
        return entity

