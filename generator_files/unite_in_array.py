
class UniteInArrayClass():
    def __init__(self):
        self.input_ports={'a': 'std_logic_vector(7 downto 0)', 'b':'std_logic_vector(7 downto 0)','c':'std_logic_vector(7 downto 0)'}
        self.output_ports={'d':'array_24b'}

    def unite_in_array(self, parameters=['8', '0'], inputs={'a':'signal_name1', 'b':'signal_name2','c':'signal_name3'}, outputs={'d':'signal_name4'}):
            entity = ''
            entity += 'process('

            for i in inputs.values():
                entity += i + ','

            entity = entity[:-1] + ')\n'
            entity += 'begin\n'
            entity+='   '+outputs['d']+"<="
            for i in inputs.values():
                entity +=   i   + ' & '

            entity = entity[:-2] + ';'

            entity += '\nend process;\n'
            return entity
#
# a = UniteInArrayClass()
# print(a.unite_in_array())