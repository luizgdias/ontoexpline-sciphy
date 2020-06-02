def create_attribute(ontoexpline, att_name):
    """[função que cria instancias de atributo]

    Arguments:
        ontoexpline {[ontology]} -- [ontologia utilizada pelo código, no caso: ontoexpline com provone, expline, metadata e edam]
        artefact {[ontology instance]} -- [nome do atributo]
    """   
    att = ontoexpline.Attribute(att_name)
    return(att)

def associate_att_to_port(ontoexpline, att, port):
    print("***att: ", att)
    print("***port: ", port)
    att.wasAssociatedWith.append(port)