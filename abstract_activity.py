################################################################################################ 
# Autor: Luiz Gustavo Dias 11/05/2020
# email: lgdias@id.uff.br
# Desc: função para criar atividades abstratas no ramo ExpLine da ontoexpline. As atividades 
# abstratas devem possuir um nome, um tipo de domínio previamente cadastrado e uma lista de 
# programas previamente cadastrados. Nessa função, após a validação dos tipos de programas, 
# e tipo de atividade, também é criado o relacionamento implements(program, activity) entre os
# ramos ProvONE e ExpLine na ontoexpline.
################################################################################################ 


def create_abstract_activity(ontoexpline, aa_name, aa_domain_type, input_relation, output_relation, optional):
    """[função que cria atividades abstratas]

    Arguments:
        ontoexpline {[ontology]} -- [ontologia utilizada pelo código, no caso: ontoexpline com provone, expline, metadata e edam]
        aa_name {[string]} -- [nome da atividade abstrata]
        aa_domain {[ontology class]} -- [classe relacionada a operação de dominio]
        input_relation {[list]} -- [relações de atributos consumidas pela atividade]
        output_relation{[list]} -- [relações de atributos produzidos pela atividade]
    """   
    # print(ontoexpline.search(subclass_of = ontoexpline.Activity_Domain_Type))
    # print(aa_domain_type)
    aa = ontoexpline.Abstract_activity(aa_name)
    aa.is_a.append(aa_domain_type)
    aa.hasInputRelation    = input_relation
    aa.hasOutputRelation   = output_relation
    if optional == True:
        aa.is_a.append(ontoexpline.Optional)
        
    return(True)


# codigo antigo:
# def  create_aa(ontoexpline, aa_name, aa_domain_type, implementers):
#     search_type = ontoexpline.search(iri = "*"+aa_domain_type)
#     search_activity = ontoexpline.search(iri = "*"+aa_name)
#     for type_on_domain in search_type:
#         if ((ontoexpline.Activity_Domain_Type in type_on_domain.is_a) and not(search_activity)):
#             aa = ontoexpline.Abstract_activity(aa_name) 
#             aa.is_a.append(type_on_domain)
#             for implementer in implementers:
#                 search_program = ontoexpline.search(iri = "*"+implementer)
#                 for program in search_program:
#                     if((program) and (type_on_domain in program.is_a) and (ontoexpline.Program in program.is_a)):
#                         print("|** O programa ", program, " existe para a atividade ", type_on_domain)
#                         program.implements.append(aa)
#                     else:
#                         print("|** O programa ", program, " nao existe para a atividade " , type_on_domain)         
#             ontoexpline.save(file = "ontologies/ontoexpline.owl", format = "rdfxml")

#             search_programs = ontoexpline.search(is_a = type_on_domain, implements = ontoexpline.search(is_a = ontoexpline.Abstract_activity))
#             if(len(search_programs) >= 2):
#                 aa.is_a.append(ontoexpline.Variant)
#                 print("|** A atividade ", aa_name, " possui perfil ontoexpline.Variant ")
#                 print('|**********')
#             if(len(search_programs) == 1):
#                 aa.is_a.append(ontoexpline.Mandatory)
#                 print("|** A atividade ", aa_name, " possui perfil ontoexpline.Mandatory ")
#                 print('|**********')
#         else:
#             print('|** A atividade ', aa_name,' ja existe')
#             print('|**********')
#         ontoexpline.save(file = "ontologies/ontoexpline.owl", format = "rdfxml")
#         # create_relations(ontoexpline, aa_name)


# def create_relations(ontoexpline, aa_name):
#     search_aa = ontoexpline.search(iri = "*"+aa_name)
#     for aa in search_aa:
#         if(ontoexpline.Abstract_activity in aa.is_a):
#             in_relation     = ontoexpline.Relation("in_relation_"+aa_name)
#             out_relation    = ontoexpline.Relation("out_relation_"+aa_name)
#             aa.hasInputRelation.append(in_relation)
#             aa.hasOutputRelation.append(out_relation)
#             ontoexpline.save(file = "ontologies/ontoexpline.owl", format = "rdfxml")