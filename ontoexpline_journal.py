from domain_operation import define_domain_operation, list_operations
from attribute import create_attribute, associate_att_to_port
from relation import create_relation
from metadata import create_metadata_type
from metadata import create_metadata, rename_entity
from program import create_program
from relation import create_relation, associate_attriute_to_relation
from abstract_activity import create_abstract_activity
from channel import create_channel
from basic_structural_operations import refactor_entity, delete_entity, insert_annotation
from port import create_port, associate_port_to_program

from owlready2 import *
import types
import datetime

# Carregando a ontologia
ontoexpline = get_ontology("ontologies/ontoexpline.owl").load()

# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                  Definindo Operações de domínio (edam:operation)
# -------------------------------------------------------------------------------------------------------------------------------------------

# definir uma listagem de todas as classes
sequencing_quality_control  = define_domain_operation(ontoexpline, ontoexpline.Bio, ontoexpline.Sequencing_quality_control)
sequence_alignment          = define_domain_operation(ontoexpline, ontoexpline.Bio, ontoexpline.Sequence_alignment_operation_0292)

# listar operations
# operations = list_operations(ontoexpline, ontoexpline.Bio)


# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Definindo tipos de Metadados
# -------------------------------------------------------------------------------------------------------------------------------------------

# criar tipos de metadado (classes)
# adicionar mais um parametro a respeito do dominio do metadado
uri                     =  create_metadata_type(ontoexpline, 'Uri', 'uniform resource identifier')
url                     =  create_metadata_type(ontoexpline, 'Url', 'uniform resource locator')
description             =  create_metadata_type(ontoexpline, 'Description', 'Description of artefact')
terms_of_use            =  create_metadata_type(ontoexpline, 'Terms_of_use', 'Terms of use of artefact')
configuration_parameter =  create_metadata_type(ontoexpline, 'Configuration_Parameter', 'Possiveis valores de atruibutos de configuração')

# ----------------------- Funções estruturais basicas: ----------------------
uri3 = ontoexpline.Teste
# uri = refactor_entity(ontoexpline, uri, 'Uri2')
# delete = delete_entity(ontoexpline, uri3)
# print(delete)
insert = insert_annotation(ontoexpline, configuration_parameter, 'new annotation for entity')
# ----------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Itens da Primeira Atividade Abstrata
# -------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Definindo atributos abstratos
abs_att_sequence_input      = create_attribute(ontoexpline, 'abs_att_sequence_input')
abs_att_validated_sequence  = create_attribute(ontoexpline, 'abs_att_validated_sequence')

# 2 - Definindo individuo do tipo Port | criando individuo do tipo metadata e atribuindo-o a um attribute
sequence_input  =   create_port(ontoexpline, 'Sequence_input')
metadata3       =   create_metadata(ontoexpline, sequence_input , description, 'Description_Sequence_Input') 

# Criando individuos do tipo Port | criando individuo do tipo metadata e atribuindo-o a um attribute
validated_sequence   =   create_port(ontoexpline, 'Validated_sequence')
metadata4            =   create_metadata(ontoexpline, validated_sequence , description, 'Description_Validated_Sequence')

# 3 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_sequence_input, sequence_input)
associate_att_to_port(ontoexpline, abs_att_validated_sequence, validated_sequence)

# 4 - Definindo programa
validator_program       =   create_program(ontoexpline, 'Remove_Pipe', sequencing_quality_control, [sequence_input], [validated_sequence])

# criando metadados e relacionando a individuos do tipo Program:
metadata    =   create_metadata(ontoexpline, validator_program , description, 'Description_Remove_Pipe') 
metadata2   =   create_metadata(ontoexpline, validator_program , terms_of_use, 'Termo_De_Uso') 

# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação
in_relation_aa_validation    =   create_relation(ontoexpline, 'In_relation_aa_validation')
out_relation_aa_validation   =   create_relation(ontoexpline, 'Out_relation_aa_validation')

# 6 - Associando atributos a relações
associate_attriute_to_relation(ontoexpline, in_relation_aa_validation, [sequence_input])
associate_attriute_to_relation(ontoexpline, out_relation_aa_validation, [validated_sequence])

# 7 - Definindo atividade abstrata : create_abstract_activity(ontologia, 'nome da atividade', relação de entrada, relação de saida, opcionalidade)
aa_1 = create_abstract_activity(ontoexpline, 'AA_Validation', sequencing_quality_control,  [in_relation_aa_validation], [out_relation_aa_validation], False)
# # -------------------------------------------------------------------------------------------------------------------------------------------


# # -------------------------------------------------------------------------------------------------------------------------------------------
# #                                                   Itens da Segunda Atividade Abstrata
# # -------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Definindo atributos abstratos
abs_att_6merpair            =   create_attribute(ontoexpline, 'abs_att__6merpair')
abs_att_global_pair         =   create_attribute(ontoexpline, 'abs_att_global_pair')
abs_att_op                  =   create_attribute(ontoexpline, 'abs_att_op')
abs_att_aligned_sequence    =   create_attribute(ontoexpline, 'abs_att_aligned_sequence')

# 2 - Definindo individuo do tipo Port | criando individuo do tipo metadata e atribuindo-o a um attribute
# portas de entrada
_6merpair       =   create_port(ontoexpline, '_6merpair')
global_pair     =   create_port(ontoexpline, 'global_pair')
op              =   create_port(ontoexpline, 'op')
# portas de saida
aligned_sequence =   create_port(ontoexpline, 'aligned_sequence')

# 3 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_6merpair, _6merpair)
associate_att_to_port(ontoexpline, abs_att_global_pair, global_pair)
associate_att_to_port(ontoexpline, abs_att_op, op)
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, aligned_sequence)

# 4 - Definindo programa
mafft       =   create_program(ontoexpline, 'Mafft', sequence_alignment, [_6merpair, global_pair, op],[aligned_sequence])

# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação
in_relation_aa_alignment    =   create_relation(ontoexpline, 'In_relation_aa_alignment')
out_relation_aa_alignment   =   create_relation(ontoexpline, 'Out_relation_aa_alignment')

# 6 - Associando atributos a relações
associate_attriute_to_relation(ontoexpline, in_relation_aa_alignment, [abs_att_6merpair, abs_att_global_pair, abs_att_op])
associate_attriute_to_relation(ontoexpline, out_relation_aa_alignment, [abs_att_aligned_sequence])

# 7 - Definindo atividade abstrata
aa_2    = create_abstract_activity(ontoexpline, 'AA_Alignment', sequence_alignment,  [in_relation_aa_alignment], [out_relation_aa_alignment], False)


# # -------------------------------------------------------------------------------------------------
# # criando programa
# muscle       =   create_program(ontoexpline, 'Muscle', sequence_alignment)

# # criando metadados e relacionando a individuos do tipo Program:
# metadata    =   create_metadata(ontoexpline, muscle , description, 'Description_Muscle', 'Muscle: programa que alinha sequencias') 
# metadata2   =   create_metadata(ontoexpline, muscle , terms_of_use, 'Termo_de_Uso_Muscle', 'Muscle: termo de uso') 

# # criando individuos do tipo Attribute | criando individuo do tipo metadata e atribuindo-o ao atributo criado
# maxhours                   =   create_attribute(ontoexpline, 'Maxhours' ) 
# maxhours_description       =   create_metadata(ontoexpline, maxhours , description, 'MaxHour_Description', 'Maximim time. If h hours have elpased, then complete the current iteration and stop. Default no time limit.') 
# maxiter                    =   create_attribute(ontoexpline, 'Maxiter' ) 
# maxiter_description        =   create_metadata(ontoexpline, maxiter , description, 'Maxiter_Description', 'Maximum number of iterations to run. Default 16. Set to 2 for large datasets where refinement (iterations 3+) is too slow.')
# out_filename               =   create_attribute(ontoexpline, 'OutFileName' ) 
# out_filename_description   =   create_metadata(ontoexpline, out_filename , description, 'OutFileName_Description', 'Output file, default format is aligned FASTA. ')

# # criando individuo do tipo relação de entrada | associando atributos a relação
# in_relation_muscle    =   create_relation(ontoexpline, 'Relation_in_Muscle')
# associate_relation_to_attributes(ontoexpline, in_relation_muscle, 'input', [validated_sequence, maxhours, maxiter, out_filename])

# #  criando atributo gerado
# aligned_sequence    = create_attribute(ontoexpline, 'aligned_sequence')

# # criando individuo do tipo relação de entrada | associando atributos a relação
# out_relation_muscle   =   create_relation(ontoexpline, 'Relation_out_Muscle')
# associate_relation_to_attributes(ontoexpline, out_relation_muscle, 'output', [aligned_sequence])


# # -------------------------------------------------------------------------------------------------
# #  criando programa
# clustalw       =   create_program(ontoexpline, 'ClustalW', sequence_alignment)

# # criando metadados e relacionando a individuos do tipo Program:
# metadata    =   create_metadata(ontoexpline, clustalw , description, 'Description_Clustalw', 'Clustalw: programa que alinha sequencias') 
# metadata2   =   create_metadata(ontoexpline, clustalw , terms_of_use, 'Termo_de_Uso_Clustalw', 'Clustalw: termo de uso') 

# # criando individuos do tipo Attribute | criando individuo do tipo metadata e atribuindo-o ao atributo criado
# interactive                             =   create_attribute(ontoexpline, 'Interactive' ) 
# interactive_description                 =   create_metadata(ontoexpline, interactive , description, 'Interactive_Description', 'ead command line, then enter normal interactive menus') 
# quickTree                               =   create_attribute(ontoexpline, 'QuickTree')
# quickTree_description                   =   create_metadata(ontoexpline, quickTree , description, 'QuickTree_Description', 'use FAST algorithm for the alignment guide tree') 
# negative                                =   create_attribute(ontoexpline, 'Negative')
# negative_description                    =   create_metadata(ontoexpline, negative , description, 'Negative_Description', 'protein alignment with negative values in matrix') 
# seqnos                                  =   create_attribute(ontoexpline, 'SeqNos')
# seqnos_description                      =   create_metadata(ontoexpline, seqnos , description, 'Seqnos_Description', 'OFF or ON (for Clustal output only)') 

# # criando individuo do tipo relação de entrada | associando atributos a relação
# in_relation_clustalw    =   create_relation(ontoexpline, 'Relation_in_ClustalW')
# associate_relation_to_attributes(ontoexpline, in_relation_clustalw, 'input', [validated_sequence])

# #  criando atributo gerado
# aligned_sequence    = create_attribute(ontoexpline, 'aligned_sequence')

# # criando individuo do tipo relação de entrada | associando atributos a relação
# out_relation_clustalw   =   create_relation(ontoexpline, 'Relation_out_Clustalw')
# associate_relation_to_attributes(ontoexpline, out_relation_clustalw, 'output', [aligned_sequence])

# # criando atividade abstrata 2
# # aa_2    = create_abstract_activity(ontoexpline, 'AA_Alignment', sequence_alignment,  [in_relation_mafft, in_relation_muscle, in_relation_clustalw], [out_relation_clustalw, out_relation_mafft, out_relation_muscle], False)

# # criando canal
# # ch1     = create_channel(ontoexpline, 'ch_validation_alignment', [out_relation_remove_pipe, in_relation_clustalw, in_relation_mafft, in_relation_muscle])

# # salvando na ontologia
ontoexpline.save(file = "ontologies/ontoexpline.owl", format = "rdfxml")

# # outputDataset   =   create_relation(ontoexpline, 'out','Out_Remove_Pipe', [validated_sequence])

# # p2          =   program.create_program(ontoexpline, 'Mafft', 'Sequence_alignment_operation_0292')
# # metadata    =   create_metadata(ontoexpline, prog1 , 'ubuntu', 'program', 'ubuntu.com')


# # collection.create_collection(ontoexpline, p2, 'in', 'In_Coll_Mafft', ['validatedSequence', 'at1'])
# # collection.create_collection(ontoexpline, p2, 'out', 'Out_Coll_Mafft', ['alignedSequence'])

# # p3 = program.create_program(ontoexpline, 'Clustalw', 'Sequence_alignment_operation_0292')
# # collection.create_collection(ontoexpline, p3, 'in', 'In_Coll_Clustalw', ['validatedSequence', 'at1'])
# # collection.create_collection(ontoexpline, p3, 'out', 'Out_Coll_Clustalw', ['alignedSequence', 'at1', 'at3'])

# # abstract_activity.create_aa(ontoexpline, 'AA_Validation', 'Sequencing_quality_control', ['Remove_Pipe'])
# # abstract_activity.create_aa(ontoexpline, 'AA_Alignment', 'Sequence_alignment_operation_0292', ['Mafft', 'Clustalw'])

# # channel.create_channel(ontoexpline, 'AA_Validation', 'AA_Alignment')



# # deve-se passar uma string para as funções e fazer o search por iri, e verificar se existe na ontologia, 
# # do jeito que esta da erro e nao salva as instancias: https://owlready2.readthedocs.io/en/latest/onto.html#saving-an-ontology-to-an-owl-file
# # x = '*Sequence_alignment_operation_0292'
# # print(ontoexpline.search(iri = x))
