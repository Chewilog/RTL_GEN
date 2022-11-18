# This is a sample Python script.
import xml.etree.ElementTree as ET
import sys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def generate(file2open, output_name):
    # Use a breakpoint in the code line below to debug your script.

    tree = ET.parse(file2open)
    root = tree.getroot()
    for child in root[0]:
        print(child)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate('teste.xml', 'teste')


