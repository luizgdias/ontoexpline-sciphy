from owlready2 import *

def refactor_entity(ontoexpline, entity, refactor_name):
    search_entity = ontoexpline.search(iri = '*'+refactor_name)
    if((search_entity)):
        print('Entidade presente na ontologia, nao é possível refatorar')
    else:
        print('Entidade ', entity, ' refatorada para ', refactor_name)
        entity.name = refactor_name
    return(entity)

def delete_entity(ontoexpline, entity):
    verify = None
    if(entity):
        owlready2.destroy_entity(entity) == True
        verify = True
    else:
        verify = False
    return(verify)

def insert_annotation(ontoexpline, entity, new_annotation):
    verify = None
    if(entity):
        entity.seeAlso.append(new_annotation)
        verify = True
    else:
        print(entity, ' => entidade não existe existe')
        verify = False
    return(verify)
