from domain_operation import define_domain_operation, list_operations
from attribute import create_attribute, associate_att_to_port
from relation import create_relation
from metadata import create_metadata_type
from metadata import create_metadata, rename_entity
from program import create_program
from relation import create_relation, associate_attriutes_to_relation
from abstract_activity import create_abstract_activity
from channel import create_channel
from basic_structural_operations import refactor_entity, delete_entity, insert_annotation
from port import create_port, associate_port_to_program
from channel import create_channel

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
conversion                  = define_domain_operation(ontoexpline, ontoexpline.Bio, ontoexpline.Sequence_alignment_conversion_operation_0260)
model_generator             = define_domain_operation(ontoexpline, ontoexpline.Bio, ontoexpline.Sequence_alignment_refinament_operation_2089)
tree_generator              = define_domain_operation(ontoexpline, ontoexpline.Bio, ontoexpline.Phylogenetic_tree_generation_operation_0547)

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
# 1 - Definindo atributos abstratos atividade 1
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
associate_attriutes_to_relation(ontoexpline, in_relation_aa_validation, [sequence_input])
associate_attriutes_to_relation(ontoexpline, out_relation_aa_validation, [validated_sequence])

# 7 - Definindo atividade abstrata : create_abstract_activity(ontologia, 'nome da atividade', relação de entrada, relação de saida, opcionalidade)
aa_1 = create_abstract_activity(ontoexpline, 'AA_Validation', sequencing_quality_control,  [in_relation_aa_validation], [out_relation_aa_validation], False)
# # -------------------------------------------------------------------------------------------------------------------------------------------


# # -------------------------------------------------------------------------------------------------------------------------------------------
# #                                                   Itens da Segunda Atividade Abstrata
# # -------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Definindo atributos abstratos
abs_att_6merpair            =   create_attribute(ontoexpline, 'abs_att__6merpair') # mafft
abs_att_global_pair         =   create_attribute(ontoexpline, 'abs_att_global_pair') # mafft
abs_att_op                  =   create_attribute(ontoexpline, 'abs_att_op') # mafft
abs_att_aligned_sequence    =   create_attribute(ontoexpline, 'abs_att_aligned_sequence') # mafft clustalw muscle
abs_att_maxhours            =   create_attribute(ontoexpline, 'abs_att_maxhours' ) # muscle
abs_att_maxiter             =   create_attribute(ontoexpline, 'abs_att_maxiter' ) # muscle
abs_att_interactive         =   create_attribute(ontoexpline, 'abs_att_interactive' ) # clustalw
abs_att_quickTree           =   create_attribute(ontoexpline, 'abs_att_quickTree' ) # clustalw
abs_att_negative            =   create_attribute(ontoexpline, 'abs_att_negative' ) # clustalw
abs_att_seqnos              =   create_attribute(ontoexpline, 'abs_att_seqnos') # clustalw

# 2.1 - Definindo individuo do tipo Port | criando individuo do tipo metadata e atribuindo-o a um attribute
# portas de entrada
_6merpair       =   create_port(ontoexpline, '_6merpair')
global_pair     =   create_port(ontoexpline, 'global_pair')
op              =   create_port(ontoexpline, 'op')
# portas de saida
aligned_sequence =   create_port(ontoexpline, 'aligned_sequence')

# 3.1 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_6merpair, _6merpair)
associate_att_to_port(ontoexpline, abs_att_global_pair, global_pair)
associate_att_to_port(ontoexpline, abs_att_op, op)
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, aligned_sequence)

# 4.1 - Definindo programa
mafft       =   create_program(ontoexpline, 'Mafft', sequence_alignment, [_6merpair, global_pair, op],[aligned_sequence])

# ---------------------------------------------------------------------------------------------------------------------------------
# 2.2 - Definindo portas do programa 2
maxhours                   =   create_port(ontoexpline, 'Maxhours' ) 
maxiter                    =   create_port(ontoexpline, 'Maxiter' ) 
out_filename               =   create_port(ontoexpline, 'OutFileName') 

# 3.2 - Associando portas aos atributos
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, out_filename)
associate_att_to_port(ontoexpline, abs_att_maxiter, maxiter)
associate_att_to_port(ontoexpline, abs_att_maxhours, maxhours)

# 4.3 - Definindo programa 2
muscle       =   create_program(ontoexpline, 'Muscle', sequence_alignment, [maxhours, maxiter], [out_filename])

# ---------------------------------------------------------------------------------------------------------------------------------
# 2.3 - Definindo portas do programa 3
interactive                             =   create_port(ontoexpline, 'Interactive' ) 
quickTree                               =   create_port(ontoexpline, 'QuickTree')
negative                                =   create_port(ontoexpline, 'Negative')
seqnos                                  =   create_port(ontoexpline, 'SeqNos')
clustaw_aligned_sequence                =   create_port(ontoexpline, 'Clustalw_output_file')

# 3.3 - Associando portas aos atributos
associate_att_to_port(ontoexpline, abs_att_interactive, interactive)
associate_att_to_port(ontoexpline, abs_att_quickTree, quickTree)
associate_att_to_port(ontoexpline, abs_att_negative, negative)
associate_att_to_port(ontoexpline, abs_att_seqnos, seqnos)
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, clustaw_aligned_sequence)

# 4.3 - Definindo programa 3 
clustalw     =      create_program(ontoexpline, 'ClustalW', sequence_alignment, [interactive, quickTree, negative, seqnos], [])
# ---------------------------------------------------------------------------------------------------------------------------------
# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação

in_relation_aa_alignment    =   create_relation(ontoexpline, 'In_relation_aa_alignment')
out_relation_aa_alignment   =   create_relation(ontoexpline, 'Out_relation_aa_alignment')

# 6 - Associando atributos a relações
associate_attriutes_to_relation(ontoexpline, in_relation_aa_alignment,   [  abs_att_6merpair, abs_att_global_pair, 
                                                                            abs_att_op, abs_att_maxhours, 
                                                                            abs_att_maxiter, 
                                                                            abs_att_negative,
                                                                            abs_att_quickTree, 
                                                                            abs_att_seqnos
                                                                        ])
associate_attriutes_to_relation(ontoexpline, out_relation_aa_alignment, [abs_att_aligned_sequence])

# 7 - Definindo atividade abstrata
aa_2    = create_abstract_activity(ontoexpline, 'AA_Alignment', sequence_alignment,  [in_relation_aa_alignment], [out_relation_aa_alignment], False)
# # -------------------------------------------------------------------------------------------------------------------------------------------
# #                                                   Fim da Segunda Atividade Abstrata
# # -------------------------------------------------------------------------------------------------------------------------------------------

ch1 = create_channel(ontoexpline, aa_1, aa_2)

# # -------------------------------------------------------------------------------------------------------------------------------------------
# #                                                   Itens da Terceira Atividade Abstrata
# # -------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Definindo atributos abstratos (de saida)
abs_att_EMBL_format      = create_attribute(ontoexpline, 'abs_att_EMBL_format')
abs_att_GenBank_format   = create_attribute(ontoexpline, 'abs_att_GenBank_format')
abs_att_Fasta_format     = create_attribute(ontoexpline, 'abs_att_Fasta_format')
abs_att_Phylip_format    = create_attribute(ontoexpline, 'abs_att_Phylip_format')

# 2 - Definindo individuo do tipo Port | criando individuo do tipo metadata e atribuindo-o a um attribute
in_ReadSeq_aligned_sequence     =   create_port(ontoexpline, 'in_Readseq_aligned_sequence') #essa porta será associada a um atributo definido na atividade anterior
out_Readseq_EMBL_format         =   create_port(ontoexpline, 'out_Readseq_EMBL_Format')
out_Readseq_GenBank_format      =   create_port(ontoexpline, 'out_Readseq_GenBank_Format')
out_Readseq_Fasta_format        =   create_port(ontoexpline, 'out_Readseq_Fasta_Format')
out_Readseq_Phylip_format       =   create_port(ontoexpline, 'out_Readseq_Phylip_Format')



# 3 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, in_ReadSeq_aligned_sequence)
associate_att_to_port(ontoexpline, abs_att_EMBL_format, out_Readseq_EMBL_format)
associate_att_to_port(ontoexpline, abs_att_GenBank_format, out_Readseq_GenBank_format)
associate_att_to_port(ontoexpline, abs_att_Fasta_format, out_Readseq_Fasta_format)

# 4 - Definindo programa
readseq       =   create_program(ontoexpline, 'ReadSeq', sequencing_quality_control, [in_ReadSeq_aligned_sequence], [out_Readseq_EMBL_format, out_Readseq_GenBank_format, out_Readseq_Fasta_format])


# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação
in_relation_aa_readseq    =   create_relation(ontoexpline, 'In_relation_aa_readseq')
out_relation_aa_readseq   =   create_relation(ontoexpline, 'Out_relation_aa_readseq')

# 6 - Associando atributos a relações
associate_attriutes_to_relation(ontoexpline, in_relation_aa_validation, [abs_att_aligned_sequence])
associate_attriutes_to_relation(ontoexpline, out_relation_aa_validation, [abs_att_EMBL_format, abs_att_Fasta_format, abs_att_GenBank_format])

# 7 - Definindo atividade abstrata : create_abstract_activity(ontologia, 'nome da atividade', relação de entrada, relação de saida, opcionalidade)
aa_3 = create_abstract_activity(ontoexpline, 'AA_Converter', conversion,  [in_relation_aa_readseq], [out_relation_aa_readseq], False)

# # -------------------------------------------------------------------------------------------------------------------------------------------
# #                                                   Itens da Quarta Atividade Abstrata
# # -------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Definindo atributos abstratos (de saida)
abs_att_Phylip_format      = create_attribute(ontoexpline, 'abs_att_Phylip_format')
abs_att_EvolutiveModel     = create_attribute(ontoexpline, 'abs_att_EvolutiveModel')

# 2 - Definindo individuo do tipo Port | criando individuo do tipo metadata e atribuindo-o a um attribute
in_ModelGen_Phylip_Format         =   create_port(ontoexpline, 'ModelGen_Phylip_Format')
in_ModelGen_Fasta_Format          =   create_port(ontoexpline, 'ModelGen_Fasta_Format')
out_ModelGen_EvolutiveModel       =   create_port(ontoexpline, 'ModelGen_EvolutiveModel')


# 3 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_Fasta_format, in_ModelGen_Fasta_Format)
associate_att_to_port(ontoexpline, abs_att_Phylip_format, in_ModelGen_Phylip_Format)

# 4 - Definindo programa
modelGen       =   create_program(ontoexpline, 'ReadSeq', sequencing_quality_control, [in_ModelGen_Fasta_Format, in_ModelGen_Phylip_Format], [out_ModelGen_EvolutiveModel])


# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação
in_relation_aa_modelGen    =   create_relation(ontoexpline, 'In_Relation_ModelGen')
out_relation_aa_modelGen   =   create_relation(ontoexpline, 'Out_Relation_aa_ModelGen')

# 6 - Associando atributos a relações
associate_attriutes_to_relation(ontoexpline, in_relation_aa_validation, [abs_att_aligned_sequence])
associate_attriutes_to_relation(ontoexpline, out_relation_aa_validation, [abs_att_EMBL_format, abs_att_Fasta_format, abs_att_GenBank_format])

# 7 - Definindo atividade abstrata : create_abstract_activity(ontologia, 'nome da atividade', 'tipo operação de domínio', relação de entrada, relação de saida, opcionalidade)
aa_4 = create_abstract_activity(ontoexpline, 'AA_ModelGen', model_generator,  [in_relation_aa_modelGen], [out_relation_aa_modelGen], False)

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
