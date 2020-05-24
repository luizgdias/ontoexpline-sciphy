def create_relation(ontoexpline, relation_name):
    relation = ontoexpline.Relation(relation_name) 
    return(relation)
    

def associate_relation_to_attributes(ontoexpline, relation, relation_type, attributes):
    print(relation)
    if(relation_type == 'input'):
        for att in attributes:
            relation.composedBy.append(att)
    
    if(relation_type == 'output'):
        for att in attributes:
            relation.composedBy.append(att)