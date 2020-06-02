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
in_port_remove_pipe_sequence_input  =   create_port(ontoexpline, 'in_port_remove_pipe_sequence_input')
out_port_remove_pipe_validated_sequence   =   create_port(ontoexpline, 'out_port_remove_pipe_validated_sequence')

# 3 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_sequence_input, in_port_remove_pipe_sequence_input)
associate_att_to_port(ontoexpline, abs_att_validated_sequence, out_port_remove_pipe_validated_sequence)

# 4 - Definindo programa
validator_program       =   create_program(ontoexpline, 'remove_Pipe', sequencing_quality_control, [in_port_remove_pipe_sequence_input], [out_port_remove_pipe_validated_sequence])

# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação
in_relation_aa_validation    =   create_relation(ontoexpline, 'in_relation_aa_validation')
out_relation_aa_validation   =   create_relation(ontoexpline, 'out_relation_aa_validation')

# 6 - Associando atributos a relações
associate_attriutes_to_relation(ontoexpline, in_relation_aa_validation, [abs_att_sequence_input])
associate_attriutes_to_relation(ontoexpline, out_relation_aa_validation, [abs_att_validated_sequence])

# 7 - Definindo atividade abstrata : create_abstract_activity(ontologia, 'nome da atividade', relação de entrada, relação de saida, opcionalidade)
aa_1 = create_abstract_activity(ontoexpline, 'aa_validation', sequencing_quality_control,  [in_relation_aa_validation], [out_relation_aa_validation], False)

# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Itens da Segunda Atividade Abstrata
# -------------------------------------------------------------------------------------------------------------------------------------------
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
in_port_mafft_validated_sequence = create_port(ontoexpline, 'in_port_mafft_validated_sequence')
in_port_6merpair       =   create_port(ontoexpline, 'in_port_6merpair')
in_port_global_pair     =   create_port(ontoexpline, 'in_port_global_pair')
in_port_op              =   create_port(ontoexpline, 'in_port_op')
# portas de saida
out_port_mafft_aligned_sequence =   create_port(ontoexpline, 'out_port_mafft_aligned_sequence')

# 3.1 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_validated_sequence, in_port_mafft_validated_sequence)
associate_att_to_port(ontoexpline, abs_att_6merpair, in_port_6merpair)
associate_att_to_port(ontoexpline, abs_att_global_pair, in_port_global_pair)
associate_att_to_port(ontoexpline, abs_att_op, in_port_op)
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, out_port_mafft_aligned_sequence)

# 4.1 - Definindo programa
mafft       =   create_program(ontoexpline, 'mafft', sequence_alignment,    [  in_port_mafft_validated_sequence, 
                                                                                in_port_6merpair, 
                                                                                in_port_global_pair, 
                                                                                in_port_op],
                                                                            [   out_port_mafft_aligned_sequence])

# ---------------------------------------------------------------------------------------------------------------------------------
# 2.2 - Definindo portas do programa 2
in_port_muscle_validated_sequence         =   create_port(ontoexpline, 'in_port_muscle_validated_sequence')
in_port_muscle_maxhours                   =   create_port(ontoexpline, 'in_port_muscle_maxhours' ) 
in_port_muscle_maxiter                    =   create_port(ontoexpline, 'in_port_muscle_maxiter' ) 
out_port_muscle_aligned_sequence          =   create_port(ontoexpline, 'out_port_muscle_aligned_sequence') 

# 3.2 - Associando portas aos atributos

associate_att_to_port(ontoexpline, abs_att_validated_sequence, in_port_muscle_validated_sequence)
associate_att_to_port(ontoexpline, abs_att_maxiter, in_port_muscle_maxiter)
associate_att_to_port(ontoexpline, abs_att_maxhours, in_port_muscle_maxhours)
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, out_port_muscle_aligned_sequence)

# 4.3 - Definindo programa 2
muscle       =   create_program(ontoexpline, 'muscle', sequence_alignment,  [   in_port_muscle_validated_sequence, 
                                                                                in_port_muscle_maxhours, 
                                                                                in_port_muscle_maxiter
                                                                            ], 
                                                                            [   
                                                                                out_port_muscle_aligned_sequence
                                                                            ])

# ---------------------------------------------------------------------------------------------------------------------------------
# 2.3 - Definindo portas do programa 3
in_port_clustalw_validated_sequence                      =   create_port(ontoexpline, 'in_port_clustalw_validated_sequence')
in_port_clustalw_interactive                             =   create_port(ontoexpline, 'in_port_lustalw_interactive' ) 
in_port_clustalw_quickTree                               =   create_port(ontoexpline, 'in_port_clustalw_quickTree')
in_port_clustalw_negative                                =   create_port(ontoexpline, 'in_port_clustalw_negative')
in_port_clustalw_seqnos                                  =   create_port(ontoexpline, 'on_port_clustalw_seqnosNos')
out_port_clustaw_aligned_sequence                        =   create_port(ontoexpline, 'out_port_clustaw_aligned_sequence')

# 3.3 - Associando portas aos atributos
associate_att_to_port(ontoexpline, abs_att_validated_sequence, in_port_clustalw_validated_sequence)
associate_att_to_port(ontoexpline, abs_att_interactive, in_port_clustalw_interactive)
associate_att_to_port(ontoexpline, abs_att_quickTree, in_port_clustalw_quickTree)
associate_att_to_port(ontoexpline, abs_att_negative, in_port_clustalw_negative)
associate_att_to_port(ontoexpline, abs_att_seqnos, in_port_clustalw_seqnos)
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, out_port_clustaw_aligned_sequence)

# 4.3 - Definindo programa 3 
clustalw     =      create_program(ontoexpline, 'clustalw', sequence_alignment, [   in_port_clustalw_validated_sequence, 
                                                                                    in_port_clustalw_interactive, 
                                                                                    in_port_clustalw_quickTree, 
                                                                                    in_port_clustalw_negative, 
                                                                                    in_port_clustalw_seqnos
                                                                                ], 
                                                                                [   
                                                                                    out_port_clustaw_aligned_sequence
                                                                                ])
# ---------------------------------------------------------------------------------------------------------------------------------
# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação

in_relation_aa_alignment    =   create_relation(ontoexpline, 'in_relation_aa_alignment')
out_relation_aa_alignment   =   create_relation(ontoexpline, 'out_relation_aa_alignment')

# 6 - Associando atributos a relações
associate_attriutes_to_relation(ontoexpline, in_relation_aa_alignment,   [  abs_att_validated_sequence,
                                                                            abs_att_6merpair, 
                                                                            abs_att_global_pair, 
                                                                            abs_att_op, 
                                                                            abs_att_maxhours, 
                                                                            abs_att_maxiter, 
                                                                            abs_att_negative,
                                                                            abs_att_quickTree, 
                                                                            abs_att_seqnos
                                                                        ])
associate_attriutes_to_relation(ontoexpline, out_relation_aa_alignment, [
                                                                            abs_att_aligned_sequence
                                                                        ])

# 7 - Definindo atividade abstrata
aa_2    = create_abstract_activity(ontoexpline, 'aa_alignment', sequence_alignment, [in_relation_aa_alignment], 
                                                                                    [out_relation_aa_alignment], False)
# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Fim da Segunda Atividade Abstrata
# -------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                     Criando canal entre aa1 e aa2
# -------------------------------------------------------------------------------------------------------------------------------------------

ch1 = create_channel(ontoexpline, aa_1, aa_2)

# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Itens da Terceira Atividade Abstrata
# -------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Definindo atributos abstratos (de saida)
abs_att_embl_format      = create_attribute(ontoexpline, 'abs_att_embl_format')
abs_att_genbank_format   = create_attribute(ontoexpline, 'abs_att_genbank_format')
abs_att_fasta_format     = create_attribute(ontoexpline, 'abs_att_fasta_format')
abs_att_phylip_format    = create_attribute(ontoexpline, 'abs_att_phylip_format')

# 2 - Definindo individuo do tipo Port | criando individuo do tipo metadata e atribuindo-o a um attribute
in_port_readseq_aligned_sequence     =   create_port(ontoexpline, 'in_port_readseq_aligned_sequence') #essa porta será associada a um atributo definido na atividade anterior
out_port_readseq_embl_format         =   create_port(ontoexpline, 'out_port_readseq_embl_format')
out_port_readseq_genbank_format      =   create_port(ontoexpline, 'out_port_readseq_genbank_format')
out_port_readseq_fasta_format        =   create_port(ontoexpline, 'out_port_readseq_fasta_format')
out_port_readseq_phylip_format       =   create_port(ontoexpline, 'out_port_readseq_phylip_format')

# 3 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_aligned_sequence, in_port_readseq_aligned_sequence)
associate_att_to_port(ontoexpline, abs_att_embl_format, out_port_readseq_embl_format)
associate_att_to_port(ontoexpline, abs_att_genbank_format, out_port_readseq_genbank_format)
associate_att_to_port(ontoexpline, abs_att_fasta_format, out_port_readseq_fasta_format)
associate_att_to_port(ontoexpline, abs_att_phylip_format, out_port_readseq_phylip_format)

# 4 - Definindo programa
readseq       =   create_program(ontoexpline, 'readseq', sequencing_quality_control,    [   in_port_readseq_aligned_sequence ], 
                                                                                        [   out_port_readseq_embl_format, 
                                                                                            out_port_readseq_genbank_format, 
                                                                                            out_port_readseq_fasta_format])

# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação
in_relation_aa_readseq    =   create_relation(ontoexpline, 'in_relation_aa_readseq')
out_relation_aa_readseq   =   create_relation(ontoexpline, 'out_relation_aa_readseq')

# 6 - Associando atributos a relações
associate_attriutes_to_relation(ontoexpline, in_relation_aa_readseq,     [   abs_att_aligned_sequence    ])
associate_attriutes_to_relation(ontoexpline, out_relation_aa_readseq,    [   
                                                                                abs_att_embl_format, 
                                                                                abs_att_fasta_format, 
                                                                                abs_att_genbank_format     
                                                                            ])

# 7 - Definindo atividade abstrata : create_abstract_activity(ontologia, 'nome da atividade', relação de entrada, relação de saida, opcionalidade)
aa_3 = create_abstract_activity(ontoexpline, 'aa_converter', conversion,  [in_relation_aa_readseq], [out_relation_aa_readseq], False)

# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                     Criando canal entre aa2 e aa3
# -------------------------------------------------------------------------------------------------------------------------------------------

ch2 = create_channel(ontoexpline, aa_2, aa_3)

# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                   Itens da Quarta Atividade Abstrata
# -------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Definindo atributos abstratos (de saida)
abs_att_evolutive_model     = create_attribute(ontoexpline, 'abs_att_evolutive_model')

# 2 - Definindo individuo do tipo Port | criando individuo do tipo metadata e atribuindo-o a um attribute
in_port_model_gen_phylip_format         =   create_port(ontoexpline, 'in_port_model_gen_phylip_format')
in_port_model_gen_fasta_format          =   create_port(ontoexpline, 'in_port_model_gen_fasta_format')
out_port_model_gen_evolutive_model      =   create_port(ontoexpline, 'out_port_model_gen_evolutive_model')

# 3 - Associando atributos (abstratos) a portas (concretas)
associate_att_to_port(ontoexpline, abs_att_fasta_format, in_port_model_gen_fasta_format)
associate_att_to_port(ontoexpline, abs_att_phylip_format, in_port_model_gen_phylip_format)
associate_att_to_port(ontoexpline, abs_att_evolutive_model, out_port_model_gen_evolutive_model)

# 4 - Definindo programa
modelGen       =   create_program(ontoexpline, 'model_generator', model_generator,  [   
                                                                                        in_port_model_gen_phylip_format, 
                                                                                        in_port_model_gen_fasta_format       
                                                                                    ], 
                                                                                    [   out_port_model_gen_evolutive_model   ])

# 5 - Definindo individuo do tipo relação de entrada | associando atributos a relação
in_relation_aa_model_gen    =   create_relation(ontoexpline, 'in_relation_model_Gen')
out_relation_aa_model_gen   =   create_relation(ontoexpline, 'out_relation_model_Gen')

# 6 - Associando atributos a relações
associate_attriutes_to_relation(ontoexpline, in_relation_aa_model_gen,     [   abs_att_aligned_sequence])
associate_attriutes_to_relation(ontoexpline, out_relation_aa_model_gen,    [   
                                                                                abs_att_evolutive_model 
                                                                            ])

# 7 - Definindo atividade abstrata : create_abstract_activity(ontologia, 'nome da atividade', 'tipo operação de domínio', relação de entrada, relação de saida, opcionalidade)
aa_4 = create_abstract_activity(ontoexpline, 'aa_model_gen', model_generator,  [in_relation_aa_model_gen], [out_relation_aa_model_gen], False)

# -------------------------------------------------------------------------------------------------------------------------------------------
#                                                     Criando canal entre aa3 e aa4
# -------------------------------------------------------------------------------------------------------------------------------------------

ch3 = create_channel(ontoexpline, aa_3, aa_4)


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
