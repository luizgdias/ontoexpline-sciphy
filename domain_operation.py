################################################################################################ 
# Autor: Luiz Gustavo Dias 11/05/2020
# email: lgdias@id.uff.br
# Desc: função para criar atividades de tipos de domínio na ontoexpline, esses tipos são advindos
# de um ramo de domínio e são importantes para cadastrar programas implementadores e atividades.
# Dessa forma atividades só sao implementadas por programas que correspondam ao seu tipo
################################################################################################ 

def define_domain_operation(ontoexpline, domain, operation):
    """[função utilizada para explicitar as operações de domínio permitidas]

    Arguments:
        ontoexpline {[ontology]} -- [ontologia utilizada pelo código, no caso: ontoexpline com provone, expline, metadata e edam]
        domain {[ontology class]} -- [superclasse de dominio que contém as operações que podem ser utilizadas]
        operation {[ontology class]} -- [classe relacionada a operação de dominio]
    """   

    print("|** Verificando se operação ", operation ," é valida no contexto do SciPhy.")
    busca = ontoexpline.search(subclass_of = domain)
    for item in busca:
        if item == operation:
            operation.is_a.append(ontoexpline.Activity_Domain_Type)
            return(operation)

def list_operations(ontoexpline, domain):
    print('**Lista de Operações do domínio: ', domain, ' **')
    print(ontoexpline.search(subclass_of = domain))