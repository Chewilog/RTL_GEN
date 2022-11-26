# This is a sample Python script.
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

def generate(file2open, output_name):
    # Use a breakpoint in the code line below to debug your script.

    avaiable_components_list = []
    avaiable_components = {}
    flag=0
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
    for name in os.listdir('component_files'):
        if not(name[:-4] in avaiable_components_list):
            file = open('component_files/'+name, 'r')
            aux = ''
            component_aux = {}

            for line in file.readlines():
                if 'entity' in line:
                    flag = 1
                    aux = line
                    aux = aux.replace('entity', '')
                    aux = aux.replace('is', '')
                    aux = aux.replace(' ', '')
                    component_aux[aux] = Component(aux)
                    component_aux[aux].entity += line

                elif flag == 1 and 'end ' in line:

                    component_aux[aux].entity += line
                    flag = 0

                elif flag == 1:
                    component_aux[aux].entity += line



            print(component_aux[aux].entity)




    exit()
    # Read the xml file
    tree = ET.parse(file2open)
    root = tree.getroot()
    for child in root[0]:
        print(child)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate('teste.xml', 'teste')


