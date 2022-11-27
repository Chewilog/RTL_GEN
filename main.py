# This is a sample Python script.
import copy
import xml.etree.ElementTree as ET
import sys
import os
import pickle
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class InOut:
    def __init__(self, name, port, is_signal):
        self.name = name
        self.port = port
        #self.type = var_type  # talvez nao seja necessario
        self.is_signal = is_signal


class Component:
    def __init__(self, name):
        self.name = name
        self.entity = ''
        self.in_ports = {}
        self.out_ports = {}
        self.generic_ports = []


def get_genport(line):

    line2 = line
    line2 = line2.replace(':', ' ')
    line2 = line2.replace('=', ' = ')
    line2 = line2.replace('(', ' ')
    line2 = line2.split(' ')
    aux = []
    for i in range(len(line2)):
        line2[i] = line2[i].replace('(', '')
        line2[i] = line2[i].replace(')', '')
        line2[i] = line2[i].replace(';', '')
        line2[i] = line2[i].replace('\n', '')
        if not (line2[i] == ''):
            aux.append(line2[i])

    line2 = aux

    for i in range(len(line2)):
        if line2[i] == '=':

            return (line2[i-2], line2[i-1])
    return ''

def get_port(line):
    line2 = line.upper()
    line2 = line2.replace(':', ' ')
    line2 = line2.replace('=', ' = ')
    line2 = line2.replace('(', ' ')
    line2 = line2.split(' ')
    aux = []
    for i in range(len(line2)):
        line2[i] = line2[i].replace('(', '')
        line2[i] = line2[i].replace(')', '')
        line2[i] = line2[i].replace(';', '')
        line2[i] = line2[i].replace('\n', '')
        if not (line2[i] == ''):
            aux.append(line2[i])


    line2 = aux

    return line2

    # for i in range(len(line2)):
    #     if line2[i] == '=':
    #         return line2[i - 1]
    # return ''

def generate(file2open, output_name):
    # Use a breakpoint in the code line below to debug your script.

    avaiable_components = {}
    used_components = {}
    used_transitions = {}
    flag = 0
    flag2 = 0
    component_name=''


    #Initializing components
    if not os.path.isdir('component_files'):
        os.mkdir('component_files')
    if not os.path.isfile('components.pckl'):
        file = open('components.pckl', 'wb')
        pickle.dump(avaiable_components, file)
        file.close()

    # file = open('components.pckl', 'wb')
    # avaiable_components = pickle.load(file)
    # file.close()

    #  I still need to end pickle
    file = open('components_list.pckl', 'rb')
    avaiable_components_list = pickle.load(file)
    component_aux = {}
    for name in os.listdir('component_files'):
        if not(name[:-4] in list(avaiable_components.keys())):
            file = open('component_files/'+name, 'r')
            aux = ''


            for line in file.readlines():
                if 'entity' in line:
                    flag = 1
                    flag2 = 0
                    aux = line
                    aux = aux.replace('entity', '')
                    aux = aux.replace('is', '')
                    aux = aux.replace(' ', '')
                    aux = aux.replace('\n', '')
                    component_aux[aux] = Component(aux)
                    component_aux[aux].entity += line

                elif flag == 1 and ('end ' in line or 'END' in line or 'End' in line):

                    component_aux[aux].entity += line
                    flag = 0

                elif flag == 1:
                    if ('generic' in line) or ('Generic' in line) or ('GENERIC' in line):
                        flag2 = 1
                        if ':' in line:
                            component_aux[aux].generic_ports.append(get_genport(line))

                    elif flag2 == 1:

                        component_aux[aux].generic_ports.append(get_genport(line))
                    elif flag2 == 0:
                        if ':' in line:
                            port = get_port(line)

                            if port[0] == 'PORT':
                                port = port[1::]

                            # if aux =='FFT':
                            #     print(port)


                            if 'IN' in port:
                                if len(port) == 3:
                                    component_aux[aux].in_ports((port[0], port[2]))
                                else:
                                    component_aux[aux].in_ports.append((port[0], port[2]+'( '+port[3]+' '+port[4]+' '+port[5]+' )'))

                            elif 'OUT' in port:
                                if len(port) == 3:
                                    component_aux[aux].out_ports.append((port[0], port[2]))
                                else:
                                    component_aux[aux].out_ports.append((port[0], port[2]+'( '+port[3]+' '+port[4]+' '+port[5]+' )'))
                    if ')' in line and flag2 == 1:
                        flag2 = 0

                    component_aux[aux].entity += line


    for i in component_aux.keys():
        if '' in component_aux[i].generic_ports:
            component_aux[i].generic_ports = component_aux[i].generic_ports[:-1]

    components = {}
    signals={}
    inputs = []
    outputs = []
    generic = []
    terminals ={}
    constants = {}

    entity = '''library IEEE;\nuse IEEE.STD_LOGIC_1164.ALL;\nuse IEEE.NUMERIC_STD.ALL;\n\n'''


    # Read the xml file
    tree = ET.parse(file2open)
    root = tree.getroot()
    for child in root[0]:
        dict_child = child.attrib
        if len(dict_child['id']) > 5:
            if 'shape=mxgraph.electrical.logic_gates.dual_inline_ic' in dict_child['style']:
                aux = dict_child['value'].replace('<br>', '')

                aux = aux.split('/')
                components[dict_child['id']] = (aux[0], aux[1])
            elif 'endArrow' in dict_child['style'] or 'orthogonalEdgeStyle' in dict_child['style']:
                aux = dict_child['value']
                aux = aux.split('/')
                is_signal=1
                if 'in' in aux or 'out' in aux:
                    is_signal = 0

                signals[dict_child['id']] = InOut('s'+aux[0].replace('$', 'const')+'_to_'+aux[1]+str(random.randint(1,1000)), (aux, dict_child['source'],dict_child['target']), is_signal)

            elif 'shape=mxgraph.electrical.abstract.dac' in dict_child['style'] or 'shape=mxgraph.electrical.abstract.delta' in dict_child['style']:
                if 'shape=mxgraph.electrical.abstract.dac' in dict_child['style']:

                    aux = dict_child['value'].split('/')
                    terminals[dict_child['id']] = (aux[0], aux[1])
                    inputs.append((aux[0], aux[1]))
                else:
                    aux = dict_child['value'].split('/')
                    terminals[dict_child['id']] = (aux[0], aux[1])
                    outputs.append((aux[0], aux[1]))

            elif 'shape=mxgraph.electrical.miscellaneous.generic_component' in dict_child['style']:
                aux = dict_child['value'].split('/')
                constants[dict_child['id']] = (aux[0], aux[1])

            elif 'shape=mxgraph.electrical.rot_mech.winding_connection' in dict_child['style']:
                aux = dict_child['value'].split('/')
                terminals[dict_child['id']] = (aux[0], aux[1], aux[2])
                generic.append((aux[0], aux[1], aux[2]))


    entity += 'entity '+output_name+' is\n'

    # Generic

    if len(generic)>0:
        entity+='   generic(\n'
        for i in generic:
            entity+='   '+i[2]+' : ' + i[1] +' := '+i[0]+';\n'
    entity = entity[:-2]
    entity += '   );\n'


    entity += '\n   port(\n'
    # Inputs
    for i in inputs:
        entity += '     '+ i[0]+': in '+i[1]+';\n'

    # Outputs
    for i in outputs:
        entity += '     '+ i[0]+': out '+i[1]+';\n'
    entity=entity[:-2]
    entity+='   );\n'

    entity+='end '+output_name+';\n\n'

    entity+= 'architecture Behavioral of '+output_name+' is\n\n'

    #components

    for i in components.keys():
        entity_cp = component_aux[components[i][0]].entity
        start_aux = entity_cp.find('entity')
        end_aux = entity_cp.find('end')
        aux_str = entity_cp[start_aux + len('entity'):end_aux]
        entity += 'component'

        entity += aux_str.replace(components[i][0], components[i][0])
        entity += 'end component;\n\n'

    #  signals
    aux_signals={}
    for key in signals:


        if signals[key].port[1] not in aux_signals.keys() :
            aux_signals[signals[key].port[1]] = []
            aux_signals[signals[key].port[1]].append((key,signals[key].port[2]))
        else:
            aux_signals[signals[key].port[1]].append((key,signals[key].port[2]))

    for i in aux_signals.keys():
        if len(aux_signals[i]) == 1:


            if not(signals[aux_signals[i][0][0]].port[0][0] == 'in' or signals[aux_signals[i][0][0]].port[0][0] == '$' or signals[aux_signals[i][0][0]].port[0][0] == 'generic'):
                print('port is ', signals[aux_signals[i][0][0]].port)
                print('-----',components[signals[aux_signals[i][0][0]].port[1]][0])
                print('++++',component_aux[components[signals[aux_signals[i][0][0]].port[1]][0]].out_ports)
                #entity += 'signal '+signals[aux_signals[i][0][0]].name+' :'+ components[signals[aux_signals[i][0][0]].port[1]]
    #  begin architecture
    entity+='begin\n\n'

    entity+= 'end behavioral;'
    #print(entity)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate('teste.xml', 'teste')


