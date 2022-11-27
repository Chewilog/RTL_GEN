# This is a sample Python script.
import copy
import xml.etree.ElementTree as ET
import sys
import os
import pickle

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class InOut:
    def __init__(self, name, port, var_type, is_signal):
        self.name = name
        self.port = port
        self.type = var_type  # talvez nao seja necessario
        self.is_signal = is_signal


class Component:
    def __init__(self, name):
        self.name = name
        self.entity = ''
        self.in_ports = []
        self.out_ports = []
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
    print(line2)
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

    avaiable_components_list = []
    avaiable_components = {}
    flag = 0
    flag2 = 0
    component_name=''


    #Initializing components
    if not os.path.isdir('component_files'):
        os.mkdir('component_files')
    if not os.path.isfile('components_list.pckl'):
        file = open('components_list.pckl', 'wb')
        pickle.dump(avaiable_components_list, file)
        file.close()
    if not os.path.isfile('components.pckl'):
        file = open('components.pckl', 'wb')
        pickle.dump(avaiable_components, file)
        file.close()


    file = open('components_list.pckl', 'rb')
    avaiable_components_list = pickle.load(file)
    component_aux = {}
    for name in os.listdir('component_files'):
        if not(name[:-4] in avaiable_components_list):
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
                                    component_aux[aux].in_ports.append((port[0], port[2]))
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
        print(i,'-->',component_aux[i].generic_ports)
        print(i,'-->',component_aux[i].in_ports)
        print(i,'-->',component_aux[i].out_ports)





    exit()
    # Read the xml file
    tree = ET.parse(file2open)
    root = tree.getroot()
    for child in root[0]:
        print(child)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate('teste.xml', 'teste')


