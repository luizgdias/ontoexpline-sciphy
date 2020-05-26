################################################################################################ 
# Autor: Luiz Gustavo Dias 11/05/2020
# email: lgdias@id.uff.br
# Desc: função para criar portas no ramo ProvONE da ontoexpline. As portas são criadas automaticamente
# após a criação e validação dos programas. Nessa função também é feito o relacionamento entre
# hasInPort(program, port) e hasOutPort(program, port)
################################################################################################ 

def create_port(ontoexpline, port_name):
    new_port = ontoexpline.Port(port_name)
    
    return(new_port)

def associate_port_to_program(ontoexpline, program, input_ports, output_ports):
    """[associa duas listas de portas a um programa]

    Arguments:
        ontoexpline {[ontoexpline]} -- [ontologia carregada]
        program {[ontoexpline.Program]} -- [individuo do tipo programa]
        input_ports {[list]} -- [lista de portas de entrada]
        output_ports {[list]} -- [lista de portas de saida]
    """
    print(input_ports)
    program.hasInPort   = input_ports
    program.hasOutPort  = output_ports

    for in_port in input_ports:
        print(in_port)
        # in_port.isUsedBy(program)
    
    # for out_port in output_ports:
    #     out_port.wasGeneratedBy(program)
