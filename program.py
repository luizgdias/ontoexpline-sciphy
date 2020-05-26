################################################################################################ 
# Autor: Luiz Gustavo Dias 11/05/2020
# email: lgdias@id.uff.br
# Desc: função para criar programas no ramo ProvONE da ontoexpline. Os programas devem possuir um
# tipo de domínio previamente cadastrado. O tipo de domínio é cadastrado pela function 
# domain_activity.create_domain_activity. Se o tipo não for cadastrado previamente o programa também
# não é cadastrado
################################################################################################ 

def create_program(ontoexpline, program, domain_type):
    new_program = ontoexpline.Program(program)
    # new_program.is_a.append(domain_type)
    # print('****', domain_type)
    # create_ports(ontoexpline, new_program)
    ontoexpline.save(file = "ontologies/ontoexpline.owl", format = "rdfxml")
    return new_program

################################################################################################ 
# Autor: Luiz Gustavo Dias 11/05/2020
# email: lgdias@id.uff.br
# Desc: função para criar portas no ramo ProvONE da ontoexpline. As portas são criadas automaticamente
# após a criação e validação dos programas. Nessa função também é feito o relacionamento entre
# hasInPort(program, port) e hasOutPort(program, port)
################################################################################################ 

def create_ports(ontoexpline, program):
    in_port = ontoexpline.Port("in_port_"+program.name)
    in_port.isUsedBy.append(program)

    out_port = ontoexpline.Port("out_port_"+program.name)
    out_port.isUsedBy.append(program)

    program.hasInPort.append(in_port)
    program.hasOutPort.append(out_port)
            


