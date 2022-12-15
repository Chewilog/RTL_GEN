def adder_gen(N_of_bits='8', carry='0', inputs=['a','b','c','d'],outputs=['c']):#N_of_bits-> adder number of bits; carry-> 0=not carry, 1=carry; register-> 0=do not register, 1=register output
    entity = ''
    entity+='process('
    for i in inputs:
        entity+=i+','



    for i in outputs:
        entity += i +','
    entity = entity[:-1] + ')\n'
    entity+='begin\n'
    entity += '   ' + outputs[0] + '<= '
    for i in inputs:
        entity+= 'unsigned('+i+')'+'+'

    entity = entity[:-1] +';'

    entity+='\nend process;\n'
    return entity

