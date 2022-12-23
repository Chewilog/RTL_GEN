from math import sin,pi
import struct
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
class TableGenClass():
    def __init__(self):
        self.input_ports={'t':'std_logic_vector(7 downto 0)'}
        self.output_ports={'b':'std_logic_vector(31 downto 0)'}

    def table_gen(self, parameters, inputs, outputs):
        t = inputs['t']
        b = outputs['b']

        entity=f'with {t} select {b}\n'
        for i in range(int(parameters[0])):
            aux = sin(2*pi*i/int(parameters[0]))
            aux = binary(aux)
            aux2 = '{0:08b}'.format(i)
            entity += f'  "{aux}" when "{aux2}",\n'
        entity += f'  "{binary(0)}" when others;'

        print(entity)


a=TableGenClass()
print(a.table_gen(['8'],{'t':'signal1'},{'b':'signal2'}))

