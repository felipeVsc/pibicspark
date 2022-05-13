
def getHeader2008():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','CD_TIPO_ELEICAO','NM_TIPO_ELEICAO','NR_TURNO',
    'CD_ELEICAO','DS_ELEICAO','DT_ELEICAO','TP_ABRANGENCIA','SG_UF','SG_UE','NM_MUNICIPIO','CD_CARGO','DS_CARGO',
    'SQ_CANDIDATO','NR_CANDIDATO','NM_CANDIDATO','NM_URNA_CANDIDATO','NM_SOCIAL_CANDIDATO','NR_CPF_CANDIDATO',
    'NM_EMAIL','CD_SITUACAO_CANDIDATURA','DS_SITUACAO_CANDIDATURA','CD_DETALHE_SITUACAO_CAND',
    'DS_DETALHE_SITUACAO_CAND','TP_AGREMIACAO','NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','SQ_COLIGACAO',
    'NM_COLIGACAO','DS_COMPOSICAO_COLIGACAO','CD_NACIONALIDADE','DS_NACIONALIDADE','SG_UF_NASCIMENTO',
    'CD_MUNICIPIO_NASCIMENTO','NM_MUNICIPIO_NASCIMENTO','DT_NASCIMENTO','NR_IDADE_DATA_POSSE','NR_TITULO_ELEITORAL_CANDIDATO',
    'CD_GENERO','DS_GENERO','CD_GRAU_INSTRUCAO','DS_GRAU_INSTRUCAO','CD_ESTADO_CIVIL','DS_ESTADO_CIVIL','CD_COR_RACA','DS_COR_RACA',
    'CD_OCUPACAO','DS_OCUPACAO','VR_DESPESA_MAX_CAMPANHA','CD_SIT_TOT_TURNO','DS_SIT_TOT_TURNO','ST_REELEICAO','ST_DECLARAR_BENS',
    'NR_PROTOCOLO_CANDIDATURA','NR_PROCESSO','CD_SITUACAO_CANDIDATO_PLEITO','DS_SITUACAO_CANDIDATO_PLEITO','CD_SITUACAO_CANDIDATO_URNA',
    'DS_SITUACAO_CANDIDATO_URNA','ST_CANDIDATO_INSERIDO_URNA','CD_MUN_IBGE']


def getHeader2020():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','NR_TURNO','DS_ELEICAO','SG_UF','SG_UE','NM_UE','CD_CARGO','DS_CARGO',
'NM_CANDIDATO','SQ_CANDIDATO','NR_CANDIDATO','NR_CPF_CANDIDATO','NM_URNA_CANDIDATO','CD_SITUACAO_CANDIDATURA',
'DS_SITUACAO_CANDIDATURA','NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','CD_LEGENDA','SG_LEGENDA','DS_COMPOSICAO_LEGENDA',
'NM_LEGENDA','CD_OCUPACAO','DS_OCUPACAO','DT_NASCIMENTO','NR_TITULO_ELEITORAL_CANDIDATO','IDADE_DATA_ELEICAO',
'CD_SEXO','DS_SEXO','CD_GRAU_INSTRUCAO','DS_GRAU_INSTRUCAO','CD_ESTADO_CIVIL','DS_ESTADO_CIVIL',
'CD_NACIONALIDADE','DS_NACIONALIDADE','SG_UF_NASCIMENTO','CD_MUNICIPIO_NASCIMENTO','NM_MUNICIPIO_NASCIMENTO',
'DESPESA_MAX_CAMPANHA','CD_SIT_TOT_TURNO','DS_SIT_TOT_TURNO']

# consulta candidatos

def getHeaderCandidatos2010():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','NR_TURNO','NM_TIPO_ELEICAO','SG_UF','SG_UE','NM_MUNICIPIO','CD_CARGO',
'DS_CARGO','NM_CANDIDATO','SQ_CANDIDATO','NR_CANDIDATO','NR_CPF_CANDIDATO','NM_URNA_CANDIDATO','CD_SITUACAO_CANDIDATURA',
'DS_SITUACAO_CANDIDATURA','NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','SQ_COLIGACAO','SG_LEGENDA','DS_COMPOSICAO_COLIGACAO',
'NM_COLIGACAO','CD_OCUPACAO','DS_OCUPACAO','DT_NASCIMENTO','NR_TITULO_ELEITORAL_CANDIDATO','NR_IDADE_DATA_POSSE','CD_GENERO','DS_GENERO',
'CD_GRAU_INSTRUCAO','DS_GRAU_INSTRUCAO','CD_ESTADO_CIVIL','DS_ESTADO_CIVIL','CD_NACIONALIDADE','DS_NACIONALIDADE',
'SG_UF_NASCIMENTO','CD_MUNICIPIO_NASCIMENTO','NM_MUNICIPIO_NASCIMENTO','DESPESA_MAX_CAMPANHA','CD_SIT_TOT_TURNO','DS_SIT_TOT_TURNO']
# email add aqui
def getHeaderCandidatos2012():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','NR_TURNO','NM_TIPO_ELEICAO','SG_UF','SG_UE','NM_UE','CD_CARGO',
'DS_CARGO','NM_CANDIDATO','SQ_CANDIDATO','NR_CANDIDATO','NR_CPF_CANDIDATO','NM_URNA_CANDIDATO','CD_SITUACAO_CANDIDATURA',
'DS_SITUACAO_CANDIDATURA','NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','CD_LEGENDA','SG_LEGENDA','DS_COMPOSICAO_LEGENDA',
'NM_LEGENDA','CD_OCUPACAO','DS_OCUPACAO','DT_NASCIMENTO','NR_TITULO_ELEITORAL_CANDIDATO','NR_IDADE_DATA_POSSE','CD_GENERO','DS_GENERO',
'CD_GRAU_INSTRUCAO','DS_GRAU_INSTRUCAO','CD_ESTADO_CIVIL','DS_ESTADO_CIVIL','CD_NACIONALIDADE','DS_NACIONALIDADE',
'SG_UF_NASCIMENTO','CD_MUNICIPIO_NASCIMENTO','NM_MUNICIPIO_NASCIMENTO','DESPESA_MAX_CAMPANHA','CD_SIT_TOT_TURNO','NM_EMAIL']

# raca add aq
def getHeaderCandidatos2014():
    return ["DT_GERACAO","HH_GERACAO","ANO_ELEICAO","CD_TIPO_ELEICAO","NM_TIPO_ELEICAO",
    "NR_TURNO","CD_ELEICAO","DS_ELEICAO","DT_ELEICAO","TP_ABRANGENCIA","SG_UF","SG_UE","NM_MUNICIPIO","CD_CARGO","DS_CARGO","SQ_CANDIDATO","NR_CANDIDATO","NM_CANDIDATO",
    "NM_URNA_CANDIDATO","NM_SOCIAL_CANDIDATO","NR_CPF_CANDIDATO","NM_EMAIL","CD_SITUACAO_CANDIDATURA",
    "DS_SITUACAO_CANDIDATURA","CD_DETALHE_SITUACAO_CAND","DS_DETALHE_SITUACAO_CAND","TP_AGREMIACAO",
    "NR_PARTIDO","SG_PARTIDO","NM_PARTIDO","SQ_COLIGACAO","NM_COLIGACAO","DS_COMPOSICAO_COLIGACAO",
    "CD_NACIONALIDADE","DS_NACIONALIDADE","SG_UF_NASCIMENTO","CD_MUNICIPIO_NASCIMENTO","NM_MUNICIPIO_NASCIMENTO",
    "DT_NASCIMENTO","NR_IDADE_DATA_POSSE","NR_TITULO_ELEITORAL_CANDIDATO","CD_GENERO","DS_GENERO","CD_GRAU_INSTRUCAO",
    "DS_GRAU_INSTRUCAO","CD_ESTADO_CIVIL","DS_ESTADO_CIVIL","CD_COR_RACA","DS_COR_RACA","CD_OCUPACAO","DS_OCUPACAO",
    "VR_DESPESA_MAX_CAMPANHA","CD_SIT_TOT_TURNO","DS_SIT_TOT_TURNO","ST_REELEICAO","ST_DECLARAR_BENS","NR_PROTOCOLO_CANDIDATURA",
    "NR_PROCESSO","CD_SITUACAO_CANDIDATO_PLEITO","DS_SITUACAO_CANDIDATO_PLEITO","CD_SITUACAO_CANDIDATO_URNA","DS_SITUACAO_CANDIDATO_URNA","ST_CANDIDATO_INSERIDO_URNA"
]




# votacao nominal #

def getVotacaoHeader2012():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','NR_TURNO','DS_ELEICAO','SG_UF','SG_UE','CD_MUNICIPIO','NM_MUNICIPIO','NR_ZONA','CD_CARGO',
'NR_CANDIDATO','SQ_CANDIDATO','NM_CANDIDATO','NM_URNA_CANDIDATO','DS_CARGO','CD_SIT_CAND_SUPERIOR','DS_SIT_CAND_SUPERIOR','CD_SIT_CANDIDATO','DS_SIT_CANDIDATO',
'CD_SIT_CAND_TOT','DS_SIT_CAND_TOT','NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','SQ_COLIGACAO','NM_COLIGACAO','DS_COMPOSICAO_COLIGACAO','QT_VOTOS_NOMINAIS']

def getVotacaoHeaderAntigo():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','NR_TURNO','DS_ELEICAO','SG_UF','SG_UE','CD_CARGO','NUM_CANDIDATO','SQ_CANDIDATO','NM_CANDIDATO','NM_URNA_CANDIDATO','DS_CARGO',
    'CD_SIT_CAND_SUPERIOR','DS_SIT_CAND_SUPERIOR','CD_SIT_CANDIDATO','DS_SIT_CANDIDATO',
'CD_SIT_CAND_TOT','DS_SIT_CAND_TOT','NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','SQ_LEGENDA','NM_COLIGACAO','DS_COMPOSICAO_LEGENDA','TOTAL_VOTOS']


def getVotacaoHeader2014():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','NR_TURNO','DS_ELEICAO','SG_UF','SG_UE','CD_MUNICIPIO','NM_MUNICIPIO','NR_ZONA','CD_CARGO',
'NR_CAND','SQ_CANDIDATO','NM_CANDIDATO','NM_URNA_CANDIDATO','DS_CARGO','CD_SIT_CAND_SUPERIOR','DS_SIT_CAND_SUPERIOR','CD_SIT_CANDIDATO','DS_SIT_CANDIDATO',
'CD_SIT_CAND_TOT','DS_SIT_CAND_TOT','NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','SQ_LEGENDA','NM_COLIGACAO','DS_COMPOSICAO_LEGENDA','QT_VOTOS_NOMINAIS','ST_VOTO_EM_TRANSITO']


# quando que muda pra

def getVotacaoHeader2020():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','CD_TIPO_ELEICAO','NM_TIPO_ELEICAO','NR_TURNO','CD_ELEICAO',
    'DS_ELEICAO','DT_ELEICAO','TP_ABRANGENCIA','SG_UF','SG_UE','NM_UE','CD_MUNICIPIO','NM_MUNICIPIO','NR_ZONA','CD_CARGO','DS_CARGO',
'SQ_CANDIDATO','NR_CANDIDATO','NM_CANDIDATO','NM_URNA_CANDIDATO','NM_SOCIAL_CANDIDATO','CD_SITUACAO_CANDIDATURA','DS_SITUACAO_CANDIDATURA','CD_SIT_CAND_SUPERIOR','CD_DETALHE_SITUACAO_CAND',
'DS_DETALHE_SITUACAO_CAND','TP_AGREMIACAO','NR_PARTIDO','SG_PARTIDO','NM_PARTIDO','SQ_COLIGACAO','NM_COLIGACAO','DS_COMPOSICAO_COLIGACAO','CD_SIT_TOT_TURNO','DS_SIT_TOT_TURNO',
'ST_VOTO_EM_TRANSITO','QT_VOTOS_NOMINAIS']


["DT_GERACAO","HH_GERACAO","ANO_ELEICAO","CD_TIPO_ELEICAO","NM_TIPO_ELEICAO",
"NR_TURNO","CD_ELEICAO","DS_ELEICAO","DT_ELEICAO","TP_ABRANGENCIA","SG_UF","SG_UE",
"NM_UE","CD_MUNICIPIO","NM_MUNICIPIO","NR_ZONA","CD_CARGO","DS_CARGO","SQ_CANDIDATO",
"NR_CANDIDATO","NM_CANDIDATO","NM_URNA_CANDIDATO","NM_SOCIAL_CANDIDATO","CD_SITUACAO_CANDIDATURA",
"DS_SITUACAO_CANDIDATURA","CD_DETALHE_SITUACAO_CAND","DS_DETALHE_SITUACAO_CAND","TP_AGREMIACAO","NR_PARTIDO",
"SG_PARTIDO","NM_PARTIDO","SQ_COLIGACAO","NM_COLIGACAO","DS_COMPOSICAO_COLIGACAO","CD_SIT_TOT_TURNO","DS_SIT_TOT_TURNO","ST_VOTO_EM_TRANSITO","QT_VOTOS_NOMINAIS"]

def dicionarioDados():
    return ['DT_GERACAO','HH_GERACAO','ANO_ELEICAO','NR_TURNO',
    'NM_TIPO_ELEICAO','SG_UF','SG_UE','NM_UE','CD_CARGO','DS_CARGO',
    'NM_CANDIDATO','SQ_CANDIDATO','NR_CANDIDATO','NM_URNA_CANDIDATO',
    'CD_SITUACAO_CANDIDATURA','DS_SITUACAO_CANDIDATURA','NR_PARTIDO',
    'SG_PARTIDO','NM_PARTIDO','SQ_COLIGACAO','NM_COLIGACAO','DS_COMPOSICAO_COLIGACAO',
    'CD_OCUPACAO','DS_OCUPACAO','DT_NASCIMENTO','NR_TITULO_ELEITORAL_CANDIDATO',
    'NR_IDADE_DATA_POSSE','CD_GENERO','DS_GENERO','SG_UF_NASCIMENTO','CD_MUNICIPIO_NASCIMENTO',
    'NM_MUNICIPIO_NASCIMENTO','CD_SIT_TOT_TURNO','DS_SIT_TOT_TURNO','CD_IBGE_MUN_NASC','NR_ZONA',
    'CD_SIT_CAND_SUPERIOR','DS_SIT_CAND_SUPERIOR','QT_VOTOS_NOMINAIS','CD_TIPO_ELEICAO','TP_ABRANGENCIA','CD_MUNICIPIO',
    'NM_SOCIAL_CANDIDATO','CD_DETALHE_SITUACAO_CAND','DS_DETALHE_SITUACAO_CAND','CD_CBO','CD_MUN_IBGE']

############## 


def getHeaderBensCandidatos():
    return ["DT_GERACAO","HH_GERACAO","ANO_ELEICAO","CD_TIPO_ELEICAO","NM_TIPO_ELEICAO","CD_ELEICAO",
    "DS_ELEICAO","DT_ELEICAO","SG_UF","SG_UE","NM_UE","SQ_CANDIDATO","NR_ORDEM_CANDIDATO","CD_TIPO_BEM_CANDIDATO",
    "DS_TIPO_BEM_CANDIDATO","DS_BEM_CANDIDATO","VR_BEM_CANDIDATO","DT_ULTIMA_ATUALIZACAO","HH_ULTIMA_ATUALIZACAO"]


def getSiglas():
    return [
                            'AC',
                            'AL',
                            'AP',
                            'AM',
                            'BA',
                            'CE',
                            'DF',
                            'ES',
                            'GO',
                            'MA',
                            'MS',
                            'MT',
                            'MG',
                            'PA',
                            'PB',
                            'PR',
                            'PE',
                            'PI',
                            'RJ',
                            'RN',
                            'RS',
                            'RO',
                            'RR',
                            'SC',
                            'SP',
                            'SE',
                            'TO',
                        ]