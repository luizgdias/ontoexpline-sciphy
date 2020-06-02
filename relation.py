def create_relation(ontoexpline, relation_name):
    relation = ontoexpline.Relation(relation_name) 
    return(relation)
    

def associate_attriutes_to_relation(ontoexpline, relation, attributes):
    # print(relation)
    if(relation):
        relation.composedBy = attributes
    else:
        print("Relation.py -> Relação não existe")
    