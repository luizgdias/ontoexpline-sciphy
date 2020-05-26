def create_relation(ontoexpline, relation_name):
    relation = ontoexpline.Relation(relation_name) 
    return(relation)
    

def associate_relation_to_attributes(ontoexpline, relation, attributes):
    # print(relation)
    if(relation):
        for att in attributes:
            relation.composedBy.append(att)
    else:
        print("Relation.py -> Relação não existe")
    