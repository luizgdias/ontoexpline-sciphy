################################################################################################ 
# Autor: Luiz Gustavo Dias 12/05/2020
# email: lgdias@id.uff.br
# Desc: função para criar canais entre programas no ramo ProvONE da ontoexpline. As atividades 
# abstratas devem possuir um nome, um tipo de domínio previamente cadastrado e uma lista de 
# programas previamente cadastrados. Nessa função, após a validação dos tipos de programas, 
# e tipo de atividade, também é criado o relacionamento implements(program, activity) entre os
# ramos ProvONE e ExpLine na ontoexpline.
################################################################################################ 

def create_channel(ontoexpline, ch_name, relation_list):
    """[função que cria canais entre portas]

    Arguments:
        ontoexpline {[ontology]} -- [ontologia utilizada pelo código, no caso: ontoexpline com provone, expline, metadata e edam]
        ch_name {[string]} -- [string que identifica o canal]
        relation_list {[list]} -- [lista de relações que compõem o canal a ser criado]
    """   
    ch = ontoexpline.Channel(ch_name)
    for relation in relation_list:
        relation.belongsTo.append(ch)








# def create_channel(ontoexpline, prev_aa, next_aa):
#     search_prev_aa = ontoexpline.search_one(iri = "*"+prev_aa, type= ontoexpline.Abstract_activity)
#     implementers_prev_aa = ontoexpline.search(is_a = ontoexpline.Program, implements = search_prev_aa)
    
#     search_next_aa = ontoexpline.search_one(iri = "*"+next_aa, type= ontoexpline.Abstract_activity)
#     implementers_next_aa = ontoexpline.search(is_a = ontoexpline.Program, implements = search_next_aa)
    
#     print(search_prev_aa)
#     print(search_next_aa)

#     print(implementers_prev_aa)
#     print(implementers_next_aa)

#     # Selecionando as out ports dos programas implementadores da atividade prev
#     ports_prev = []
#     ports_prev_list = []
#     for program_prev in implementers_prev_aa:
#         ports_prev = (program_prev.hasOutPort)
#         ports_prev = list(dict.fromkeys(ports_prev))
#         ports_prev_list.append(ports_prev)
#     print(ports_prev_list)

#     # selecionando os parametros gerados pelas out ports da atividade prev
#     out_params_prev = []
#     out_params_prev_list = []
#     for port_prev in ports_prev_list:
#         for port_out in port_prev:
#             default_params_prev = port_out.hasDefaultParam
#             default_params_prev = list(dict.fromkeys(default_params_prev))
#             out_params_prev_list.append(default_params_prev)
#     print(out_params_prev_list)

#     # selecionando as in ports dos programas implementadores da atividade next
#     ports_next = []
#     ports_next_list = []
#     for program_next in implementers_next_aa:
#         ports_next = program_next.hasInPort
#         ports_next = list(dict.fromkeys(ports_next))
#         ports_next_list.append(ports_next)        
#     print(ports_next_list)

#     # selecionando os parametros consumidos pelas in ports das atividades next
#     in_params_next = []
#     in_params_next_list = []
#     for port_next in ports_next_list:
#         for port_in in port_next:
#             print(port_in)
#             default_params_next = port_in.hasDefaultParam
#             default_params_next = list(dict.fromkeys(default_params_next))
#             in_params_next_list.append(default_params_next)
#     # print(in_params_next_list)

#     verify = params_verify_match(ontoexpline, in_params_next_list, out_params_prev_list)
#     if(verify == True):
#         ch1 = ontoexpline.Channel("ch_"+prev_aa+"_"+next_aa)
#         print(ch1)
#     else:
#         print('Atividades Abstradas Incompatíveis para Conectar')



# def params_verify_match(ontoexpline, in_params_next_list, out_params_prev_list):
#     for in_list in in_params_next_list:
#         for out_list in out_params_prev_list:
#             for i in in_list:    
#                 if not(i in out_list):
#                     print('nao esta na saida ', i)
#                     return(False)
    
#     return(True)
                    
        



        

