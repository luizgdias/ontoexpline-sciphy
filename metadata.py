import datetime
import types

def create_metadata_type(ontoexpline, metadata_name, metadata_description):
    """função que cria um tipo de metadado (uma subclasse da classe Metadata)

    Arguments:
        ontoexpline {[ontology]} -- [ontologia utilizada pelo código, no caso: ontoexpline com provone, expline, metadata e edam]
        metadata_name {[string]} -- [nome da classe que será criada]
        metadata_description {[string]} -- [descrição da classe que será criada]
    """    
    with ontoexpline:
        NewClass = types.new_class(metadata_name, (ontoexpline.Metadata,))
        NewClass.seeAlso.append(metadata_description)
    return(NewClass)


def create_metadata(ontoexpline, artefact , metadata_type, metadata_name, metadata_description): 
    """[função que cria instancias de metadado do tipo criado por create_metadata_type]

    Arguments:
        ontoexpline {[ontology]} -- [ontologia utilizada pelo código, no caso: ontoexpline com provone, expline, metadata e edam]
        artefact {[ontology instance]} -- [individuo a ser agregado ao metadado]
        metadata_type {[ontology class]} -- [tipo de metadado criado anteriormente pela função create_metadata_type]
        metadata_name {[string]} -- [metadado a ser agregado pela relação hasMetadata: artefact hasMetadata metadata_name]
    """  
    metadata = ontoexpline.Metadata(metadata_name)
    metadata.seeAlso.append(metadata_description)
    metadata.is_a.append(metadata_type)
    metadata.is_a.append(metadata_type)
    print(metadata)
    print(artefact)
    # artefact.hasMetadata.append(metadata)