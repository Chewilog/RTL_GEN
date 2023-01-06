# This is a sample Python script.
import xml.etree.ElementTree as ET
import os
import pickle
import random
from generator_files.General_generator_file import *



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# problemas com as constantes


class InOut:
    def __init__(self, name, port, is_signal):
        self.name = name
        self.port = port
        self.type = ''  # talvez nao seja necessario
        self.is_signal = is_signal


class Component:
    def __init__(self, name):
        self.name = name
        self.entity = ''
        self.in_ports = {}
        self.out_ports = {}
        self.generic_ports = []
        self.input_signals = []
        self.output_signals = []

class ForGens:
    def __init__(self,id):
        self.id = ''
        self.iter = ''
        self.variables_list = {}
        self.component = {}
        self.input_signals = {}
        self.output_signals = {}
        self.input_ports = {}
        self.output_ports = {}



def convert_signal(type0, type1, val):
    type0=type0.upper().split('(')[0]
    type1=type1.upper().split('(')[0]




    vals = (type0,type1)

    if type0.upper() == type1.upper():
        return val
    else:
        print('Signal type does not match in', val)
    match vals:
        case ('STD_LOGIC_VECTOR', 'UNSIGNED'):
            print(val, '-> has been transformed from ',type0,'to', type1 )
            return f'unsigned({val})'

        case ('STD_LOGIC_VECTOR', 'SIGNED'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'signed({val})'

        case ('STD_LOGIC_VECTOR', 'INTEGER'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'to_integer(unsigned({val}))'

        case ('UNSIGNED', 'STD_LOGIC_VECTOR'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'std_logic_vector({val})'

        case ('UNSIGNED', 'SIGNED'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'signed({val})'

        case ('UNSIGNED', 'INTEGER'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'to_integer({val})'

        case ('SIGNED', 'STD_LOGIC_VECTOR'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'std_logic_vector({val})'

        case ('SIGNED', 'INTEGER'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'to_integer({val})'

        case ('SIGNED', 'UNSIGNED'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'unsigned({val})'

        case ('INTEGER', 'UNSIGNED'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'to_unsigned({val},1)'

        case ('INTEGER', 'SIGNED'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'to_signed({val},1)'

        case ('INTEGER', 'STD_LOGIC_VECTOR'):
            print(val, '-> has been transformed from ', type0, 'to', type1)
            return f'std_logic_vector(to_unsigned({val},1))'

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

def generate(file2open, output_name, add_component='n'):
    # Use a breakpoint in the code line below to debug your script.

    avaiable_components = {}
    generators = {}
    used_components = {}
    used_transitions = {}
    for_gens = {}
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

            #load the components from library
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
                                    component_aux[aux].in_ports[port[0]]= port[2]
                                else:
                                    component_aux[aux].in_ports[port[0]] = port[2]+'( '+port[3]+' '+port[4]+' '+port[5]+' )'

                            elif 'OUT' in port:
                                if len(port) == 3:
                                    component_aux[aux].out_ports[port[0]] = port[2]
                                else:
                                    component_aux[aux].out_ports[port[0]] = port[2]+'( '+port[3]+' '+port[4]+' '+port[5]+' )'
                    if ')' in line and flag2 == 1:
                        flag2 = 0

                    component_aux[aux].entity += line

    # a = General_generator()
    #
    # print(getattr(a,'adder_gen')())
    #
    # exit()

    for i in component_aux.keys():
        if '' in component_aux[i].generic_ports:
            component_aux[i].generic_ports = component_aux[i].generic_ports[:-1]

    components = {}
    signals={}
    inputs = []
    outputs = []
    generic = []
    aux_generic = {}
    terminals ={}
    constants = {}
    for_gens = {}
    types_and_constants= {}
    lists={}

    generators_in_diagram = {}
    general_generator_class = GeneralGenerator()


    entity = '''library IEEE;\nuse IEEE.STD_LOGIC_1164.ALL;\nuse IEEE.NUMERIC_STD.ALL;\n\n'''


    # Read the xml file
    tree = ET.parse(file2open)
    root = tree.getroot()
    cnt=0
    for child in root[0]:
        dict_child = child.attrib
        if len(dict_child['id']) > 5:

            if 'containerType=tree' in dict_child['style'] or dict_child['parent'] != "1":


                if    'text' in dict_child['style'] and dict_child['parent'] in lists.keys():
                    lists[dict_child['parent']].append(dict_child['value'])

                elif 'containerType=tree' in dict_child['style']:
                    if dict_child['id'] not in for_gens.keys():
                        for_gens[dict_child['id']] = ForGens(dict_child['id'])

                    iter_comp_aux = dict_child['value'].split('/')
                    for_gens[dict_child['id']].iter = (iter_comp_aux[1], iter_comp_aux[2])
                    continue

                else:

                    if '=' in dict_child['value']:
                        types_and_constants[dict_child['id']] = (dict_child['parent'], dict_child['value'])

                        pass
                        continue
                    if dict_child['parent'] not in for_gens.keys():
                        for_gens[dict_child['parent']] = ForGens(dict_child['parent'])

                    if 'shape=mxgraph.electrical.logic_gates.dual_inline_ic' in dict_child['style']:
                        aux = dict_child['value'].replace('<br>', '')
                        aux = aux.split('/')
                        components[dict_child['id']] = (aux[0], aux[1])
                        for_gens[dict_child['parent']].component[dict_child['id']] = (aux[0], aux[1])
                        continue

                    elif 'endArrow' in dict_child['style'] or 'orthogonalEdgeStyle' in dict_child['style']:
                        if not dict_child.get('value'):
                            a = dict_child['id']
                            print(f'The signal {a} does not have a "from/to" value.')
                            exit()

                        aux = dict_child['value']
                        aux = aux.split('/')
                        is_signal = 1
                        if 'in' in aux or 'out' in aux:
                            is_signal = 0

                        signals[dict_child['id']] = InOut(
                            's' + aux[0].replace('$', 'const') + '_to_' + aux[1] + str(random.randint(100, 1000)) + str(
                                cnt), (aux, dict_child['source'], dict_child['target']), is_signal)

                        if dict_child['source'] == dict_child['parent']:
                            for_gens[dict_child['parent']].input_signals[dict_child['id']] = signals[dict_child['id']]
                            for_gens[dict_child['parent']].input_ports[aux[0]] = aux[1]
                        else:
                            for_gens[dict_child['parent']].output_signals[dict_child['id']] = signals[dict_child['id']]
                            for_gens[dict_child['parent']].output_ports[aux[0]] = aux[1]

                        continue



            if 'shape=mxgraph.electrical.logic_gates.dual_inline_ic' in dict_child['style']:
                aux = dict_child['value'].replace('<br>', '')
                aux = aux.split('/')
                components[dict_child['id']] = (aux[0], aux[1])



            #signals detection
            elif 'endArrow' in dict_child['style'] or 'orthogonalEdgeStyle' in dict_child['style']:
                if not dict_child.get('value'):
                    a = dict_child['id']
                    print(f'The signal {a} does not have a "from/to" value.')
                    exit()
                aux = dict_child['value']


                aux = aux.split('/')
                is_signal=1
                if 'in' in aux or 'out' in aux:
                    is_signal = 0

                signals[dict_child['id']] = InOut('s'+aux[0].replace('$', 'const')+'_to_'+aux[1]+str(random.randint(100,1000))+str(cnt), (aux, dict_child['source'],dict_child['target']), is_signal)

            elif 'shape=mxgraph.electrical.abstract.dac' in dict_child['style'] or 'shape=mxgraph.electrical.abstract.delta' in dict_child['style']:
                if 'shape=mxgraph.electrical.abstract.dac' in dict_child['style']:

                    aux = dict_child['value'].split('/')
                    #aux = aux.replace('&nbsp;',' ')
                    terminals[dict_child['id']] = (aux[0], aux[1])
                    inputs.append((aux[0], aux[1]))
                else:
                    aux = dict_child['value'].split('/')
                    #aux = aux.replace('&nbsp;', ' ')
                    terminals[dict_child['id']] = (aux[0], aux[1])
                    outputs.append((aux[0], aux[1]))
            # constants
            elif 'shape=mxgraph.electrical.miscellaneous.generic_component' in dict_child['style']:
                aux = dict_child['value'].split('/')
                constants[dict_child['id']] = [aux[0], aux[1], '']

            elif 'shape=mxgraph.electrical.rot_mech.winding_connection' in dict_child['style']:
                aux = dict_child['value'].split('/')
                terminals[dict_child['id']] = (aux[0], aux[1], aux[2])
                generic.append((aux[0], aux[1], aux[2]))

            elif 'whiteSpace=wrap' in dict_child['style']:
                if len(dict_child['value'].split('/'))>1:
                    generators_in_diagram[dict_child['id']] = (dict_child['value'].split('/')[0], dict_child['value'].split('/')[1:],{},{})
                else:
                    generators_in_diagram[dict_child['id']] = (dict_child['value'].split('/')[0], [], {}, {})

            elif 'childLayout=stackLayout' in dict_child['style']:
                lists[dict_child['id']] = []



            cnt+=1


    entity += 'entity '+output_name+' is\n'

    # Generic

    if len(generic)>0:
        entity+='   generic(\n'
        for i in generic:
            entity+='   '+i[2]+' : ' + i[1] + ' := ' + i[0] + ';\n'
        entity = entity[:-2]
        entity += '   );\n'


    entity += '\n   port(\n'
    # Inputs
    for i in inputs:
        entity += '     ' + i[0]+': in '+i[1]+';\n'

    # Outputs
    for i in outputs:
        entity += '     ' + i[0]+': out '+i[1]+';\n'
    entity=entity[:-2]
    entity+='   );\n'

    entity+='end '+output_name+';\n\n'

    entity+= 'architecture Behavioral of '+output_name+' is\n\n'

    #TYPES
    for i in lists.keys():
        for j in lists[i]:
            aux = j.split("=")
            if ' of ' in j:
                entity += "type "+aux[0] + " is " + aux[1]+';\n'
            else:
                entity += 'constant ' + aux[0]+ " : " + aux[1]+':='+aux[2] +';\n'



    #components
    already_created = []
    for i in components.keys():

        if components[i][0] not in already_created:
            entity_cp = component_aux[components[i][0]].entity
            start_aux = entity_cp.find('entity')
            end_aux = entity_cp.find('end')
            aux_str = entity_cp[start_aux + len('entity'):end_aux]
            entity += 'component'

            entity += aux_str.replace(components[i][0], components[i][0])
            entity += 'end component;\n\n'
            already_created.append(components[i][0])

    #  signals
    aux_signals = {}
    cnt = 0
    # primeiro conseguir declarar sinais e depois ligar com os sinais auxiliares
    for key in signals:

        if signals[key].port[1] not in aux_signals.keys() :
            aux_signals[signals[key].port[1]] = []
            aux_signals[signals[key].port[1]].append((key, signals[key].port[2]))
        else:
            aux_signals[signals[key].port[1]].append((key, signals[key].port[2]))

    for i in aux_signals.keys():
        if len(aux_signals[i]) != 1 and i not in for_gens.keys():

            for j in aux_signals[i]:
                if i in generators_in_diagram and signals[j[0]].port[0][0] !=  signals[aux_signals[i][0][0]].port[0][0]:
                    continue
                signals[j[0]].name = signals[aux_signals[i][0][0]].name # talvez funcione mas ficar de olho

        if not(signals[aux_signals[i][0][0]].port[0][0] == 'in' or signals[aux_signals[i][0][0]].port[0][0] == '$' or signals[aux_signals[i][0][0]].port[0][0] == 'generic'):
            #  components[signals[aux_signals[i][0][0]].port[1]][0] -> name of component


            if i in generators_in_diagram.keys():
                # getattr(general_generator_class,)
                #getattr(o, "adder_gen")(showconfig=1)
                inout_of_generator = getattr(general_generator_class, generators_in_diagram[i][0])(showconfig=1)
                #botar um for aqui
                for j in aux_signals[i]:
                signals[j[0]].type = inout_of_generator[1][signals[aux_signals[i][0][0]].port[0][0]]
                aux_type = signals[aux_signals[i][0][0]].type
                entity += 'signal ' + signals[aux_signals[i][0][0]].name + ' :' + aux_type + ';\n'
                generators_in_diagram[i][3][signals[aux_signals[i][0][0]].port[0][0]]=signals[aux_signals[i][0][0]].name
                continue

            if i in for_gens.keys():
                # aux_type = signals[aux_signals[i][0][0]].type
                 for j in aux_signals[i]:
                     # definir tipo


                     if len(signals[j[0]].port[0]) >2: #Ocorre quando está entrando em um componente dentro do forgen e quando sai para outro forgen
                         signals[j[0]].type = signals[j[0]].port[0][3]
                         aux_type = signals[j[0]].type
                         entity += 'signal ' + signals[j[0]].name + ' :' + aux_type + ';\n'

                     else: #Ocorre quando vai para um terminal de saída, um componente ou gerador de codigo
                        if signals[j[0]].port[0][1]=='out':#terminal de saida
                            # terminals
                            aux_type = terminals[signals[j[0]].port[2]][1]
                            entity += 'signal ' + signals[j[0]].name + ' :' + aux_type + ';\n'
                            pass

                        elif signals[j[0]].port[2] in components.keys():# outro componente
                            aux_type = component_aux[components[signals[j[0]].port[2]][0]].in_ports[signals[j[0]].port[0][1]]
                            entity += 'signal ' + signals[j[0]].name + ' :' + aux_type + ';\n'

                        elif signals[j[0]].port[2] in for_gens.keys(): # Gerador de código
                            aux_type = for_gens[signals[j[0]].port[2]].input_ports[signals[j[0]].port[0][1]]
                            entity += 'signal ' + signals[j[0]].name + ' :' + aux_type + ';\n'

                        elif signals[j[0]].port[0][0] == 'in':
                            signals[aux_signals[i][0][0]].type = terminals[signals[aux_signals[i][0][0]].port[1]][1]
                            aux = terminals[signals[aux_signals[i][0][0]].port[1]]
                            terminals[signals[aux_signals[i][0][0]].port[1]]=(aux[0],aux[1],i)

                 continue

            cont=0
            for forgenkey in for_gens.keys():
                if i in for_gens[forgenkey].component.keys():
                    for j in aux_signals[i]:
                        if len(signals[j[0]].port[
                                   0]) > 2:  # Ocorre quando está entrando em um componente dentro do forgen e quando sai para outro forgen
                            signals[j[0]].type = signals[j[0]].port[0][3]
                            aux_type = signals[j[0]].type
                            entity += 'signal ' + signals[j[0]].name + ' :' + aux_type + ';\n'

                        pass
                    cont=1
            if cont:
                cont=0
                continue


            aux_outputports = component_aux[components[signals[aux_signals[i][0][0]].port[1]][0]].out_ports #  output ports dict
            aux_port = signals[aux_signals[i][0][0]].port[0][0]
            aux_type = aux_outputports[aux_port.upper()]
            signals[aux_signals[i][0][0]].type = aux_type
            entity += 'signal ' + signals[aux_signals[i][0][0]].name + ' :' + aux_type + ';\n'

        elif signals[aux_signals[i][0][0]].port[0][0] == '$':

            #  nome da constante sera                                        essa string
            constants[signals[aux_signals[i][0][0]].port[1]][2]= signals[aux_signals[i][0][0]].name
            signals[aux_signals[i][0][0]].type = constants[signals[aux_signals[i][0][0]].port[1]][1]
            entity += 'constant '+constants[signals[aux_signals[i][0][0]].port[1]][2]+' : ' + constants[signals[aux_signals[i][0][0]].port[1]][1] + ':=' +constants[signals[aux_signals[i][0][0]].port[1]][0] +';\n'

        elif signals[aux_signals[i][0][0]].port[0][0] == 'generic':
            generic_port_name = terminals[signals[aux_signals[i][0][0]].port[1]]
            signals[aux_signals[i][0][0]].name = generic_port_name[2]

        elif signals[aux_signals[i][0][0]].port[0][0] == 'in':
            signals[aux_signals[i][0][0]].type = terminals[signals[aux_signals[i][0][0]].port[1]][1]
            print('port2 é ',signals[aux_signals[i][0][0]].port[2])

            if signals[aux_signals[i][0][0]].port[2] in list(for_gens.keys()):
                aux = terminals[signals[aux_signals[i][0][0]].port[1]]
                terminals[signals[aux_signals[i][0][0]].port[1]] = (aux[0], aux[1], signals[aux_signals[i][0][0]].port[2],signals[aux_signals[i][0][0]].port[0][1])

        for k in aux_signals.keys():
            if len(aux_signals[k]) != 1:
                for j in aux_signals[k]:
                    if len(signals[j[0]].type) > len(signals[aux_signals[k][0][0]].type):
                        signals[aux_signals[k][0][0]].type = signals[j[0]].type
                    else:
                        signals[j[0]].type = signals[aux_signals[k][0][0]].type  # talvez funcione mas ficar de olho



        cnt+=1
    #  begin architecture
    entity+='\nbegin\n\n'

    #instanciation

    #  organize circuit's generic input
    # aux_generic = {}
    # if len(generic)>0:
    #     for i in generic:
    #         aux_generic[i[2]] = (i[1],i[0])


    for key in components.keys():

        cont=0
        for forgenkey in for_gens:
            if key in for_gens[forgenkey].component.keys():
                cont=1
        if cont:
            cont=0
            continue
        #  organize input/output/generic
        component_outputs = {}
        component_inputs = {}
        generic_inputs = {}
        for i in signals.keys():
            if signals[i].port[1] == key:

                component_outputs[signals[i].port[0][0].upper()]=(signals[i].name,signals[i].type)
            elif signals[i].port[2] == key:

                    # generators_in_diagram[i][2][signals[aux_signals[i][0][0]].port[0][0]]
                if signals[i].is_signal: # precisa testar mais casos genericos
                    if signals[i].port[0][0]=='generic':
                        generic_inputs[signals[i].port[0][1]] = signals[i].name
                    else:
                        component_inputs[signals[i].port[0][1].upper()] = (signals[i].name, signals[i].type)
                else:
                    component_inputs[signals[i].port[0][1].upper()] = (terminals[signals[i].port[1]][0], terminals[signals[i].port[1]][1])

        entity += components[key][1] + ': ' + components[key][0]
        if len(generic_inputs.keys()) > 0:
            entity += '\n  generic map(\n'


            aux = {}
            for i in generic:
                aux[i[2]] = (i[0],i[1])

            aux2 = {}
            for i in component_aux[components[key][0]].generic_ports:
                aux2[i[0]]=i[1]


            for item in generic_inputs.keys():
                if generic_inputs[item] in aux.keys():
                                                # converte do type0 para type1
                    entity+= '    '+item+' => '+convert_signal(aux[generic_inputs[item]][1], aux2[item], generic_inputs[item])+',\n'

            entity=entity[:-2]+');\n'

        entity+= '\n  port map(\n'



        for i in component_aux[components[key][0]].in_ports.keys():

                entity += '     '+i+'=>' + convert_signal(component_inputs[i][1], component_aux[components[key][0]].in_ports[i], component_inputs[i][0]) + ',\n'

        for i in component_aux[components[key][0]].out_ports.keys():

                entity += '     '+i+'=>' + convert_signal(component_outputs[i][1], component_aux[components[key][0]].out_ports[i], component_outputs[i][0]) + ',\n'

        entity = entity[:-2] + ');\n\n'

    for key in generators_in_diagram.keys():
        for i in signals.keys():
            if signals[i].port[1] == key:
                if signals[i].is_signal:
                    continue
                else:
                    continue
                    #generators_in_diagram[key][2][signals[i].port[0][0]] = terminals[ signals[i].port[2]][0]
            elif signals[i].port[2] == key:
                if signals[i].is_signal:
                    generators_in_diagram[key][2][signals[i].port[0][1]]=signals[i].name
                else:
                    generators_in_diagram[key][2][signals[i].port[0][1]] = terminals[ signals[i].port[1]][0]
                    pass

    entity+='\n\n'

    #code generators
    for i in generators_in_diagram.keys(): # É preciso arrumar quando for um input
         entity+=(getattr(general_generator_class,generators_in_diagram[i][0])(generators_in_diagram[i][1],generators_in_diagram[i][2],generators_in_diagram[i][3]))

    # FOR GENERATOR
    entity+='\n'
    for forgen in for_gens.keys():
        entity+= 'gen_'+list(for_gens[forgen].component.values())[0][1]+': '+ 'FOR' + ' I ' +'IN ' +for_gens[forgen].iter[0]  +' TO '+ for_gens[forgen].iter[1] + ' GENERATE\n'
        entity+= '  '+list(for_gens[forgen].component.values())[0][1]+': '+list(for_gens[forgen].component.values())[0][0]+'\n'
        entity+= '      port map(\n'

        # INPUTS
        for i in for_gens[forgen].input_signals.keys():
            if len(for_gens[forgen].input_signals[i].port[0])==2:
                entity+= '          '+ for_gens[forgen].input_signals[i].port[0][1] + ' => ' + for_gens[forgen].input_signals[i].name+',\n'
            else:
                entity+= '          '+ for_gens[forgen].input_signals[i].port[0][1] + ' => ' + for_gens[forgen].input_signals[i].name
                if for_gens[forgen].input_signals[i].port[0][2]!='0':
                    entity+='('+ for_gens[forgen].input_signals[i].port[0][2] +')'
            entity+=',\n'

        # OUTPUTS
        for i in for_gens[forgen].output_signals.keys():
            if len(for_gens[forgen].output_signals[i].port[0]) == 2:
                entity+= '          '+ for_gens[forgen].output_signals[i].port[0][0] + ' => ' + for_gens[forgen].output_signals[i].name+',\n'
            else:
                entity+= '          '+ for_gens[forgen].output_signals[i].port[0][0] + ' => ' + for_gens[forgen].output_signals[i].name
                if for_gens[forgen].output_signals[i].port[0][2]!='0':
                    entity+='('+ for_gens[forgen].output_signals[i].port[0][2]+')'
            entity += ',\n'
        entity=entity[0:-2]+');\n'
        entity+='END GENERATE;\n\n'
        # entity += component_aux[list(for_gens[forgen].component.values())[0][0]]

    #s-2 /j-9
    #connect buff signals/falta implementar para constantes e Generic
    for forgen in for_gens.keys():
        for input_forgen in for_gens[forgen].input_signals.keys() :
            for j in signals.keys():
                if for_gens[forgen].input_signals[input_forgen].port[1]==signals[j].port[2] and for_gens[forgen].input_signals[input_forgen].port[0][0]==signals[j].port[0][1] and 'in' not in signals[j].port[0]:
                    entity += for_gens[forgen].input_signals[input_forgen].name +"<="+ signals[j].name+";\n"

            for j in terminals.keys():
                if len(terminals[j])>2:
                    if terminals[j][2]==forgen and terminals[j][3].upper()==for_gens[forgen].input_signals[input_forgen].port[0][0].upper():
                        entity+=for_gens[forgen].input_signals[input_forgen].name +"<="+terminals[j][0]+';\n'
            #Falta constantes e generic


        for input_forgen in for_gens[forgen].output_signals.keys():
            for j in signals.keys():
                if for_gens[forgen].output_signals[input_forgen].port[2]==signals[j].port[1] and for_gens[forgen].output_signals[input_forgen].port[0][1]==signals[j].port[0][0] and 'in' not in signals[j].port[0]:
                    entity += signals[j].name+"<="+  for_gens[forgen].output_signals[input_forgen].name +";\n"


    #  connect outputs
    entity+='\n'
    for i in signals.keys():
        if signals[i].port[0][1]=='out':
            entity += terminals[signals[i].port[2]][0] + '<=' +signals[i].name+';\n'


    entity += ' \n'

    entity += '\nend behavioral;'
    if not os.path.isdir(output_name):
        os.mkdir(output_name)

    used_components = []
    for i in components.keys():
        if components[i][0] not in used_components:
            used_components.append(components[i][0])

    for comp in used_components:

        file = open('component_files/'+comp+'.vhd', 'r')
        file2 = open(output_name+'/'+comp+'.vhd', 'w')
        file2.write(file.read())
        file.close()
        file2.close()


    file = open(output_name+'/'+output_name+'.vhd', 'w')
    file.write(entity)
    file.close()

    # add to library
    if add_component.upper() == 'Y':
        file = open('component_files/'+output_name+'.vhd', 'w')
        file.write(entity)
        file.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate('teste.xml', 'teste2', 'N')


