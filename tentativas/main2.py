from datetime import date
from email import charset
import json
from unicodedata import name
from caworker import Worker
import time
import requests
from matplotlib.font_manager import json_dump, json_load

    # curso,
    # tipoSolicitacao:

    # transporte:  MotoristaHabilitadoCpf ou contratServLocalExecucao ou compraPassRg
    # diaria, adiantamento,

    # solProtocEmail,
    # solProtocNomeCompleto,
    # solProtocTelefone,
    # solProtocPrioridade,
    # solProtocDepartamento,
    # solProtocInstRefer,
    # solProtocProjeto,
    # solProtocJustificativaNec,
    # solProtocDataRealiz,
    # solProtocDataLocal,
    # solProtocTipoInsumo,

    # recebedorNome,
    # recebedorCpf,
    # recebedorTelefone,
    # recebedorLinkAnexos,
    # recebedorConfirmEnvio,

    # aluguelTranspJustificativa,

    # MotoristaHabilitadoNomeCompleto,
    # MotoristaHabilitadoCpf,
    # MotoristaHabilitadoCargo,
    # MotoristaHabilitadoNascimento,
    # MotoristaHabilitadoRg,
    # MotoristaHabilitadoOrgaoEm,
    # MotoristaHabilitadoEndereco,
    # MotoristaHabilitadoCep,
    # MotoristaHabilitadoEmail,
    # MotoristaHabilitadoTelefone,
    # MotoristaHabilitadoCronogViagem,
    # MotoristaHabilitadoInstRef,
    # MotoristaHabilitadoLinkCnh,
    # MotoristaHabilitadolocalHorVeiculo,
    # contratarMotoristaAdicional,
    # MotoristaHabilitadoDescVeiculo,

    # contratServInstituicaoRef,
    # contratServJustNecesside,
    # contratServLocalExecucao,

    # compraPassJustificativaNecess,
    # compraPassNomeCompleto,
    # compraPassNomeCargo,
    # compraPassNascimento,
    # compraPassRg,
    # compraPassOrgaoEmissor,
    # compraPassEndereco,
    # compraPassCep,
    # compraPassEmail,
    # compraPassTelefone,
    # compraPassBanco,
    # compraPassAgencia,
    # compraPassConta,
    # compraPassPix,
    # compraPassCronogSaidaData,
    # compraPassCronogSaidaHora,
    # compraPassCronogRetornoData,
    # compraPassCronogRetornoHora,
    # compraPassLinkRgCnh,
    # ConfirmacaoAluguelTransporte,

    # SolDiariasProfessorSelect,
    # solDiariasProfJustificativa,
    # solDiariasProfNomeCompleto,
    # solDiariasProfCpf,
    # solDiariasProfCargo,
    # solDiariasProfNascimento,
    # solDiariasProfRg,
    # solDiariasProfOrgaoEmissor,
    # solDiariasProfEndereco,
    # solDiariasProfCep,
    # solDiariasProfEmail,
    # solDiariasProfTelefone,
    # solDiariasProfBanco,
    # solDiariasProfAgencia,
    # solDiariasProfConta,
    # solDiariasProfPix,
    # solDiariasProfCronogramaViagem,
    # solDiariasProfInstReferencia,
    # confSolDiariasProf,

    # confSolDiariasAuxExt,

    # SolDiariasMotoristaessorSelect,
    # solDiariasMotoristaJustificativa,
    # solDiariasMotoristaNomeCompleto,
    # solDiariasMotoristaCpf,
    # solDiariasMotoristaCargo,
    # solDiariasMotoristaNascimento,
    # solDiariasMotoristaRg,
    # solDiariasMotoristaOrgaoEmissor,
    # solDiariasMotoristaEndereco,
    # solDiariasMotoristaCep,
    # solDiariasMotoristaEmail,
    # solDiariasMotoristaTelefone,
    # solDiariasMotoristaBanco,
    # solDiariasMotoristaAgencia,
    # solDiariasMotoristaConta,
    # solDiariasMotoristaPix,
    # solDiariasMotoristaCronogramaViagem,
    # solDiariasMotoristaInstReferencia,
    # confSolDiariasMotorista,

    # adiantEqExecJustificativaComb,
    # adiantEqExecCronogramaRealizComb,
    # adiantEqExecNomeCompletoComb,
    # adiantEqExecCpfComb,
    # adiantEqExecRgComb,
    # adiantEqExecCargoComb,
    # adiantEqExecNascimentoComb,
    # adiantEqExecOrgaoEmissorComb,
    # adiantEqExecEnderecoComb,
    # adiantEqExecCepComb,
    # adiantEqExecEmailComb,
    # adiantEqExecTelefoneComb,
    # adiantEqExecBancoComb,
    # adiantEqExecAgenciaComb,
    # adiantEqExecContaComb,
    # adiantEqExecPixComb,
    # adiantEqExecDataLimiteComb,
    # adiantEqExecInstReferenciaComb,
    # confAdiantEqExecComb

    # adiantEqExecJustificativaIns,
    # adiantEqExecCronogramaRealizIns,
    # adiantEqExecNomeCompletoIns,
    # adiantEqExecCpfIns,
    # adiantEqExecRgIns,
    # adiantEqExecCargoIns,
    # adiantEqExecNascimentoIns,
    # adiantEqExecOrgaoEmissorIns,
    # adiantEqExecEnderecoIns,
    # adiantEqExecCepIns,
    # adiantEqExecEmailIns,
    # adiantEqExecTelefoneIns,
    # adiantEqExecBancoIns,
    # adiantEqExecAgenciaIns,
    # adiantEqExecContaIns,
    # adiantEqExecPixIns,
    # adiantEqExecDataLimiteIns,
    # adiantEqExecInstReferenciaIns,
    # confAdiantEqExecIns

# def mountSolicitacaoAluguelVeiculo(task):
#     Txtdiaria = "Solicitamos diárias para o (a) professor (a) "+ solDiariasProfNomeCompleto + " que irá ministrar o curso de "+curso +", na cidade de "+ cidade +", entre os dias" + data_inicio +" e " + data_final + ", vinculado ao COTEC" + solProtocInstRefer + ", para o GPS.\n"

#     "CRONOGRAMA DE VIAGEM\n"
#     solDiariasProfCronogramaViagem
#     "Dados Pessoais da diária\n"
#     "Nome:"solDiariasProfNomeCompleto'\n'
#     "CPF:"solDiariasProfCpf'\n'
#     "Cargo:"solDiariasProfCargo'\n'
#     "Data de Nascimento:"solDiariasProfNascimento'\n'
#     "RG:"solDiariasProfRg, "Órgão Emissor"solDiariasProfOrgaoEmissor'\n'
#     "Endereço:"solDiariasProfEndereco'\n'
#     "CEP:"solDiariasProfCep'\n'
#     "E-mail:"solDiariasProfEmail'\n'
#     "Telefone:"solDiariasProfTelefone'\n'
#     "Banco:"solDiariasProfBanco'\n'
#     "Agencia:"solDiariasProfAgencia'\n'
#     "Conta:"solDiariasProfConta'\n'
#     "Pix:"solDiariasProfPix'\n'
#     return True
def mountParte(label, message="", column=False):
    line = "<div>"
    if(column):
        line += "<h4 style=\"display: block;\">"
    else:
        line += "<h4 style=\"display: inline;\">"
    line += label + ":"
    line += "</h4> <span>"
    line +=  message+"</span></div>"
    return line


def mountSolicitacaoAluguelVeiculo(task):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value
    solProtocInstRefer = task.variables['solProtocInstRefer'].value

    # curso = "teste"
    # data_inicio = "teste"
    # data_final = "teste"
    # cidade_realizacao = "teste"
    # endereco_realizacao = "teste"
    # solProtocInstRefer = "teste"

    aluguelTranspJustificativa = task.variables['aluguelTranspJustificativa'].value
    tipoSolTransporte = task.variables['tipoSolTransporte'].value
    MotoristaHabilitadoNomeCompleto = task.variables["MotoristaHabilitadoNomeCompleto"].value
    MotoristaHabilitadoCpf = task.variables["MotoristaHabilitadoCpf"].value
    MotoristaHabilitadoCargo = task.variables["MotoristaHabilitadoCargo"].value
    MotoristaHabilitadoNascimento = task.variables["MotoristaHabilitadoNascimento"].value
    MotoristaHabilitadoRg = task.variables["MotoristaHabilitadoRg"].value
    MotoristaHabilitadoOrgaoEm = task.variables["MotoristaHabilitadoOrgaoEm"].value
    MotoristaHabilitadoEndereco = task.variables["MotoristaHabilitadoEndereco"].value
    MotoristaHabilitadoCep = task.variables["MotoristaHabilitadoCep"].value
    MotoristaHabilitadoEmail = task.variables["MotoristaHabilitadoEmail"].value
    MotoristaHabilitadoTelefone = task.variables["MotoristaHabilitadoTelefone"].value
    MotoristaHabilitadoCronogViagem = task.variables["MotoristaHabilitadoCronogViagem"].value
    MotoristaHabilitadoInstRef = task.variables["MotoristaHabilitadoInstRef"].value
    MotoristaHabilitadoLinkCnh = task.variables["MotoristaHabilitadoLinkCnh"].value
    MotoristaHabilitadolocalHorVeiculo = task.variables["MotoristaHabilitadolocalHorVeiculo"].value
    MotoristaHabilitadoDescVeiculo = task.variables["MotoristaHabilitadoDescVeiculo"].value

    textoAluguelVeiculo = "<p>Solicitamos locação de veículo em nome de "
    textoAluguelVeiculo += MotoristaHabilitadoNomeCompleto
    textoAluguelVeiculo += " como condutor principal , para realização do transporte dos professores dos cursos de "
    textoAluguelVeiculo += curso
    textoAluguelVeiculo += ", na cidade de cidade (GO), entre os dias "
    textoAluguelVeiculo += data_inicio
    textoAluguelVeiculo +=  " e "
    textoAluguelVeiculo += data_final
    textoAluguelVeiculo += ", vinculado ao COTEC "
    textoAluguelVeiculo += solProtocInstRefer
    textoAluguelVeiculo += ", para o GPS.</p>"
    textoAluguelVeiculo += "<h5>VEÍCULO</h5>"
    textoAluguelVeiculo += mountParte("Modelo",MotoristaHabilitadoDescVeiculo)
    textoAluguelVeiculo += mountParte("Retirada", data_inicio)
    textoAluguelVeiculo += mountParte("Devolução",data_final )
    textoAluguelVeiculo +=  "<h5>Dados Pessoas do Motorista</h5>"
    textoAluguelVeiculo += mountParte("Nome",MotoristaHabilitadoNomeCompleto)
    textoAluguelVeiculo += mountParte("CPF", MotoristaHabilitadoCpf)
    textoAluguelVeiculo += mountParte("Cargo", MotoristaHabilitadoCargo)
    textoAluguelVeiculo += mountParte("Data de Nascimento", MotoristaHabilitadoNascimento)
    textoAluguelVeiculo += mountParte("RG", MotoristaHabilitadoRg)
    textoAluguelVeiculo += mountParte("Órgão Emissor", MotoristaHabilitadoOrgaoEm)
    textoAluguelVeiculo += mountParte("Endereço", MotoristaHabilitadoEndereco)
    textoAluguelVeiculo += mountParte("CEP", MotoristaHabilitadoCep)
    textoAluguelVeiculo += mountParte("E-mail",  MotoristaHabilitadoEmail)
    textoAluguelVeiculo += mountParte("Telefone", MotoristaHabilitadoTelefone)
    textoAluguelVeiculo += mountParte("Local do curso", MotoristaHabilitadolocalHorVeiculo)
    textoAluguelVeiculo += mountParte("CRONOGRAMA DE VIAGEM", MotoristaHabilitadoCronogViagem)
    return textoAluguelVeiculo

def mountSolicitacaContratServico(task):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value


    aluguelTranspJustificativa = task.variables['aluguelTranspJustificativa'].value
    contratServDescricao = task.variables['contratServDescricao'].value
    contratServLocalExecucao = task.variables['contratServLocalExecucao'].value

    textoAluguelVeiculo = mountParte("Solicitação de contratação de serviço de transporte","")
    textoAluguelVeiculo += mountParte("Justificativa",contratServDescricao)
    textoAluguelVeiculo += contratServDescricao
    textoAluguelVeiculo += mountParte("local e data",contratServLocalExecucao)

    return textoAluguelVeiculo

def mountSolicitacaCompraPassagem(task):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value

    # curso = "teste"
    # data_inicio = "teste"
    # data_final = "teste"
    # cidade_realizacao = "teste"
    # endereco_realizacao = "teste"

    solProtocInstRefer = task.variables['solProtocInstRefer'].value
    aluguelTranspJustificativa = task.variables['aluguelTranspJustificativa'].value
    compraPassNomeCompleto = task.variables['compraPassNomeCompleto'].value
    compraPassCpf = task.variables['compraPassCpf'].value
    compraPassCargo = task.variables['compraPassCargo'].value
    compraPassNascimento = task.variables['compraPassNascimento'].value
    compraPassRg = task.variables['compraPassRg'].value
    compraPassOrgaoEmissor = task.variables['compraPassOrgaoEmissor'].value
    compraPassEndereco = task.variables['compraPassEndereco'].value
    compraPassCep = task.variables['compraPassCep'].value
    compraPassEmail = task.variables['compraPassEmail'].value
    compraPassTelefone = task.variables['compraPassTelefone'].value
    compraPassBanco = task.variables['compraPassBanco'].value
    compraPassAgencia = task.variables['compraPassAgencia'].value
    compraPassConta = task.variables['compraPassConta'].value
    compraPassPix = task.variables['compraPassPix'].value
    compraPassCronogSaidaData = task.variables['compraPassCronogSaidaData'].value
    compraPassCronogSaidaHora = task.variables['compraPassCronogSaidaHora'].value
    compraPassCronogRetornoData = task.variables['compraPassCronogRetornoData'].value
    compraPassCronogRetornoHora = task.variables['compraPassCronogRetornoHora'].value
    compraPassLinkRgCnh = task.variables['compraPassLinkRgCnh'].value
    # CNH ACHO QUE NÃO PRECISA

    textoCompraPassagem = mountParte("Solicitação de Compra de passagem")
    textoCompraPassagem += "Solicitamos a compra de passagem de ônibus para "
    textoCompraPassagem += compraPassNomeCompleto
    textoCompraPassagem += ", residente em "
    textoCompraPassagem += compraPassEndereco
    textoCompraPassagem += ", que necessita de transporte de "
    textoCompraPassagem += compraPassEndereco
    textoCompraPassagem += " para " + endereco_realizacao
    textoCompraPassagem += ", após a ministração do curso de "
    textoCompraPassagem += curso
    textoCompraPassagem += ", com aulas do dia: "
    textoCompraPassagem += data_inicio+ " a "+ data_final
    textoCompraPassagem += ", vinculado ao COTEC"
    textoCompraPassagem += solProtocInstRefer+"."

    textoCompraPassagem += mountParte("DADOS BANCÁRIOS","")
    textoCompraPassagem += mountParte("Banco", compraPassBanco)
    textoCompraPassagem += mountParte("Agência", compraPassAgencia)
    textoCompraPassagem += mountParte("Conta", compraPassConta)
    textoCompraPassagem += mountParte("PIX", compraPassPix)

    textoCompraPassagem += mountParte("SAIDA","")
    textoCompraPassagem += mountParte("Data", compraPassCronogSaidaData)
    textoCompraPassagem += mountParte("Hora", compraPassCronogSaidaHora)

    textoCompraPassagem += mountParte("RETORNO","")
    textoCompraPassagem += mountParte("Data", compraPassCronogRetornoData)
    textoCompraPassagem += mountParte("Hora", compraPassCronogRetornoHora)

    return textoCompraPassagem

def mountSolicitacaDiariaProf(task):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value

    # curso = "teste"
    # data_inicio = "teste"
    # data_final = "teste"
    # cidade_realizacao = "teste"
    # endereco_realizacao = "teste"

    solProtocInstRefer = task.variables['solProtocInstRefer'].value
    SolDiariasProfessorSelect = task.variables['SolDiariasProfessorSelect'].value
    solDiariasProfJustificativa = task.variables['solDiariasProfJustificativa'].value
    solDiariasProfNomeCompleto = task.variables['solDiariasProfNomeCompleto'].value
    solDiariasProfCpf = task.variables['solDiariasProfCpf'].value
    solDiariasProfCargo = task.variables['solDiariasProfCargo'].value
    solDiariasProfNascimento = task.variables['solDiariasProfNascimento'].value
    solDiariasProfRg = task.variables['solDiariasProfRg'].value
    solDiariasProfOrgaoEmissor = task.variables['solDiariasProfOrgaoEmissor'].value
    solDiariasProfEndereco = task.variables['solDiariasProfEndereco'].value
    solDiariasProfCep = task.variables['solDiariasProfCep'].value
    solDiariasProfEmail = task.variables['solDiariasProfEmail'].value
    solDiariasProfTelefone = task.variables['solDiariasProfTelefone'].value
    solDiariasProfBanco = task.variables['solDiariasProfBanco'].value
    solDiariasProfAgencia = task.variables['solDiariasProfAgencia'].value
    solDiariasProfConta = task.variables['solDiariasProfConta'].value
    solDiariasProfPix = task.variables['solDiariasProfPix'].value
    solDiariasProfCronogramaViagem = task.variables['solDiariasProfCronogramaViagem'].value
    solDiariasProfInstReferencia = task.variables['solDiariasProfInstReferencia'].value

    textoDiariaProf = mountParte("Solicitação de Diaria Para Professor")
    textoDiariaProf += "Solicitamos o pagamento, por meio de RPA para "+solDiariasProfNomeCompleto+","
    textoDiariaProf += " pela ministração do curso de "+curso +" na cidade de " +cidade_realizacao+","
    textoDiariaProf += "com aulas do dia "+data_inicio+" a "+data_final+","
    textoDiariaProf += " vinculado ao COTEC "+solProtocInstRefer+"."

    textoDiariaProf += mountParte("DADOS PESSOAIS")
    textoDiariaProf += mountParte("Nome Completo", solDiariasProfNomeCompleto)
    textoDiariaProf += mountParte("CPF", solDiariasProfCpf)
    textoDiariaProf += mountParte("Cargo/Função", solDiariasProfCargo)
    textoDiariaProf += mountParte("Nascimento", solDiariasProfNascimento)
    textoDiariaProf += mountParte("RG", solDiariasProfRg)
    textoDiariaProf += mountParte("Orgão Emissor", solDiariasProfOrgaoEmissor)
    textoDiariaProf += mountParte("Endereço", solDiariasProfEndereco)
    textoDiariaProf += mountParte("CEP", solDiariasProfCep)
    textoDiariaProf += mountParte("Email", solDiariasProfEmail)
    textoDiariaProf += mountParte("Telefone", solDiariasProfTelefone)

    textoDiariaProf += mountParte("DADOS Bancários")
    textoDiariaProf += mountParte("Banco", solDiariasProfBanco)
    textoDiariaProf += mountParte("Agêmcia", solDiariasProfAgencia)
    textoDiariaProf += mountParte("Conta Com Digito", solDiariasProfConta)
    textoDiariaProf += mountParte("PIX", solDiariasProfPix)
    textoDiariaProf += mountParte("Cronograma de Viagem", solDiariasProfCronogramaViagem)
    textoDiariaProf += mountParte("Instituição de Referência", solDiariasProfInstReferencia)

    return textoDiariaProf

def mountSolicitacaDiariaAuxExt(task, numero):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value

    # curso = "teste"
    # data_inicio = "teste"
    # data_final = "teste"
    # cidade_realizacao = "teste"
    # endereco_realizacao = "teste"

    solProtocInstRefer = task.variables['solProtocInstRefer'].value
    # formAuxExtJustificativa = task.variables['formAuxExtJustificativa'+numero].value
    formAuxExtNome = task.variables['formAuxExtNome'+numero].value
    formAuxExtCpf = task.variables['formAuxExtCpf'+numero].value
    formAuxExtCargo = task.variables['formAuxExtCargo'+numero].value
    formAuxExtNascimento = task.variables['formAuxExtNascimento'+numero].value
    formAuxExtRg = task.variables['formAuxExtRg'+numero].value
    formAuxExtOrgaoEmissor = task.variables['formAuxExtOrgaoEmissor'+numero].value
    formAuxExtEndereco = task.variables['formAuxExtEndereco'+numero].value
    formAuxExtCep = task.variables['formAuxExtCep'+numero].value
    formAuxExtEmail = task.variables['formAuxExtEmail'+numero].value
    formAuxExtTelefone = task.variables['formAuxExtTelefone'+numero].value
    formAuxExtBanco = task.variables['formAuxExtBanco'+numero].value
    formAuxExtAgencia = task.variables['formAuxExtAgencia'+numero].value
    formAuxExtConta = task.variables['formAuxExtConta'+numero].value
    formAuxExtPix = task.variables['formAuxExtPix'+numero].value
    formAuxExtCronogramaViagem = task.variables['formAuxExtCronogramaViagem'+numero].value
    formAuxExtInstituicao = task.variables['formAuxExtInstituicao'+numero].value

    textoDiariaAuxExt = mountParte("Solicitação de Diaria Para Auxiliar de Extensão ("+numero+")")
    textoDiariaAuxExt += "Solicitamos o pagamento, por meio de RPA para "+formAuxExtNome+","
    textoDiariaAuxExt += " pela ministração do curso de "+curso +" na cidade de " +cidade_realizacao+","
    textoDiariaAuxExt += "com aulas do dia "+data_inicio+" a "+data_final+","
    textoDiariaAuxExt += " vinculado ao COTEC "+solProtocInstRefer+"."

    textoDiariaAuxExt += mountParte("DADOS PESSOAIS")
    textoDiariaAuxExt += mountParte("Nome Completo", formAuxExtNome)
    textoDiariaAuxExt += mountParte("CPF", formAuxExtCpf)
    textoDiariaAuxExt += mountParte("Cargo/Função", formAuxExtCargo)
    textoDiariaAuxExt += mountParte("Nascimento", formAuxExtNascimento)
    textoDiariaAuxExt += mountParte("RG", formAuxExtRg)
    textoDiariaAuxExt += mountParte("Orgão Emissor", formAuxExtOrgaoEmissor)
    textoDiariaAuxExt += mountParte("Endereço", formAuxExtEndereco)
    textoDiariaAuxExt += mountParte("CEP", formAuxExtCep)
    textoDiariaAuxExt += mountParte("Email", formAuxExtEmail)
    textoDiariaAuxExt += mountParte("Telefone", formAuxExtTelefone)

    textoDiariaAuxExt += mountParte("DADOS Bancários")
    textoDiariaAuxExt += mountParte("Banco", formAuxExtBanco)
    textoDiariaAuxExt += mountParte("Agêmcia", formAuxExtAgencia)
    textoDiariaAuxExt += mountParte("Conta Com Digito", formAuxExtConta)
    textoDiariaAuxExt += mountParte("PIX", formAuxExtPix)
    textoDiariaAuxExt += mountParte("Cronograma de Viagem", formAuxExtCronogramaViagem)
    textoDiariaAuxExt += mountParte("Instituição de Referência", formAuxExtInstituicao)

    return textoDiariaAuxExt


def mountSolicitacaDiariaMotorista(task):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value

    # curso = "teste"
    # data_inicio = "teste"
    # data_final = "teste"
    # cidade_realizacao = "teste"
    # endereco_realizacao = "teste"

    solProtocInstRefer = task.variables['solProtocInstRefer'].value
    solDiariasMotoristaJustificativa = task.variables['solDiariasMotoristaJustificativa'].value
    solDiariasMotoristaNomeCompleto = task.variables['solDiariasMotoristaNomeCompleto'].value
    solDiariasMotoristaCpf = task.variables['solDiariasMotoristaCpf'].value
    solDiariasMotoristaCargo = task.variables['solDiariasMotoristaCargo'].value
    solDiariasMotoristaNascimento = task.variables['solDiariasMotoristaNascimento'].value
    solDiariasMotoristaRg = task.variables['solDiariasMotoristaRg'].value
    solDiariasMotoristaOrgaoEmissor = task.variables['solDiariasMotoristaOrgaoEmissor'].value
    solDiariasMotoristaEndereco = task.variables['solDiariasMotoristaEndereco'].value
    solDiariasMotoristaCep = task.variables['solDiariasMotoristaCep'].value
    solDiariasMotoristaEmail = task.variables['solDiariasMotoristaEmail'].value
    solDiariasMotoristaTelefone = task.variables['solDiariasMotoristaTelefone'].value
    solDiariasMotoristaBanco = task.variables['solDiariasMotoristaBanco'].value
    solDiariasMotoristaAgencia = task.variables['solDiariasMotoristaAgencia'].value
    solDiariasMotoristaConta = task.variables['solDiariasMotoristaConta'].value
    solDiariasMotoristaPix = task.variables['solDiariasMotoristaPix'].value
    solDiariasMotoristaCronogramaViagem = task.variables['solDiariasMotoristaCronogramaViagem'].value
    solDiariasMotoristaInstReferencia = task.variables['solDiariasMotoristaInstReferencia'].value

    textoDiariaAuxExt = mountParte("Solicitação de Diaria Para Motorista")
    textoDiariaAuxExt += "Solicitamos o pagamento, por meio de RPA para "+solDiariasMotoristaNomeCompleto+","
    textoDiariaAuxExt += " pela ministração do curso de "+curso +" na cidade de " +cidade_realizacao+","
    textoDiariaAuxExt += "com aulas do dia "+data_inicio+" a "+data_final+","
    textoDiariaAuxExt += " vinculado ao COTEC "+solProtocInstRefer+"."

    textoDiariaAuxExt += mountParte("DADOS PESSOAIS")
    textoDiariaAuxExt += mountParte("Nome Completo", solDiariasMotoristaNomeCompleto)
    textoDiariaAuxExt += mountParte("CPF", solDiariasMotoristaCpf)
    textoDiariaAuxExt += mountParte("Cargo/Função", solDiariasMotoristaCargo)
    textoDiariaAuxExt += mountParte("Nascimento", solDiariasMotoristaNascimento)
    textoDiariaAuxExt += mountParte("RG", solDiariasMotoristaRg)
    textoDiariaAuxExt += mountParte("Orgão Emissor", solDiariasMotoristaOrgaoEmissor)
    textoDiariaAuxExt += mountParte("Endereço", solDiariasMotoristaEndereco)
    textoDiariaAuxExt += mountParte("CEP", solDiariasMotoristaCep)
    textoDiariaAuxExt += mountParte("Email", solDiariasMotoristaEmail)
    textoDiariaAuxExt += mountParte("Telefone", solDiariasMotoristaTelefone)

    textoDiariaAuxExt += mountParte("DADOS Bancários")
    textoDiariaAuxExt += mountParte("Banco", solDiariasMotoristaBanco)
    textoDiariaAuxExt += mountParte("Agêmcia", solDiariasMotoristaAgencia)
    textoDiariaAuxExt += mountParte("Conta Com Digito", solDiariasMotoristaConta)
    textoDiariaAuxExt += mountParte("PIX", solDiariasMotoristaPix)
    textoDiariaAuxExt += mountParte("Cronograma de Viagem", solDiariasMotoristaCronogramaViagem)
    textoDiariaAuxExt += mountParte("Instituição de Referência", solDiariasMotoristaInstReferencia)

    return textoDiariaAuxExt

def mountSolicitacaoAdiantamentoCom(task):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value

    # curso = "teste"
    # data_inicio = "teste"
    # data_final = "teste"
    # cidade_realizacao = "teste"
    # endereco_realizacao = "teste"

    solProtocInstRefer = task.variables['solProtocInstRefer'].value
    adiantEqExecValorComb = task.variables['adiantEqExecValorComb'].value
    adiantEqExecCronogramaRealizComb = task.variables['adiantEqExecCronogramaRealizComb'].value
    adiantEqExecNomeCompletoComb = task.variables['adiantEqExecNomeCompletoComb'].value
    adiantEqExecCpfComb = task.variables['adiantEqExecCpfComb'].value
    adiantEqExecRgComb = task.variables['adiantEqExecRgComb'].value
    adiantEqExecCargoComb = task.variables['adiantEqExecCargoComb'].value
    adiantEqExecNascimentoComb = task.variables['adiantEqExecNascimentoComb'].value
    adiantEqExecOrgaoEmissorComb = task.variables['adiantEqExecOrgaoEmissorComb'].value
    adiantEqExecEnderecoComb = task.variables['adiantEqExecEnderecoComb'].value
    adiantEqExecCepComb = task.variables['adiantEqExecCepComb'].value
    adiantEqExecEmailComb = task.variables['adiantEqExecEmailComb'].value
    adiantEqExecTelefoneComb = task.variables['adiantEqExecTelefoneComb'].value
    adiantEqExecBancoComb = task.variables['adiantEqExecBancoComb'].value
    adiantEqExecAgenciaComb = task.variables['adiantEqExecAgenciaComb'].value
    adiantEqExecContaComb = task.variables['adiantEqExecContaComb'].value
    adiantEqExecPixComb = task.variables['adiantEqExecPixComb'].value
    adiantEqExecDataLimiteComb = task.variables['adiantEqExecDataLimiteComb'].value
    adiantEqExecInstReferenciaComb = task.variables['adiantEqExecInstReferenciaComb'].value

    textoAdiantamentoCombustivel = mountParte("Solicitação de Adiantamento de Combustível")
    textoAdiantamentoCombustivel += "Solicitamos adiantamento do valor de R$"+adiantEqExecValorComb+",00,"
    textoAdiantamentoCombustivel += "para "+ adiantEqExecNomeCompletoComb+", para combustível, para realização do transporte dos materiais do curso de "
    textoAdiantamentoCombustivel += curso+", para a cidade de " + cidade_realizacao + " (GO), cujas aulas serão de "  +data_inicio + " a " + data_final
    textoAdiantamentoCombustivel += ", vinculado ao COTEC"+ solProtocInstRefer+", para o GPS."

    textoAdiantamentoCombustivel += mountParte("VALOR <br> R$ "+adiantEqExecValorComb+",00",)
    textoAdiantamentoCombustivel += mountParte("DADOS PESSOAIS")
    textoAdiantamentoCombustivel += mountParte("Nome", adiantEqExecNomeCompletoComb)
    textoAdiantamentoCombustivel += mountParte("CPF", adiantEqExecCpfComb)
    textoAdiantamentoCombustivel += mountParte("Cargo", adiantEqExecCargoComb)
    textoAdiantamentoCombustivel += mountParte("Data de Nascimento", adiantEqExecNascimentoComb)
    textoAdiantamentoCombustivel += mountParte("RG", adiantEqExecRgComb)
    textoAdiantamentoCombustivel += mountParte("Órgão Emissor", adiantEqExecOrgaoEmissorComb)
    textoAdiantamentoCombustivel += mountParte("Endereço", adiantEqExecEnderecoComb)
    textoAdiantamentoCombustivel += mountParte("CEP", adiantEqExecCepComb)
    textoAdiantamentoCombustivel += mountParte("E-mail", adiantEqExecEmailComb)
    textoAdiantamentoCombustivel += mountParte("Telefone", adiantEqExecTelefoneComb)
    textoAdiantamentoCombustivel += mountParte("Banco", adiantEqExecBancoComb)
    textoAdiantamentoCombustivel += mountParte("Agencia", adiantEqExecAgenciaComb)
    textoAdiantamentoCombustivel += mountParte("Conta", adiantEqExecContaComb)

    return textoAdiantamentoCombustivel


def mountSolicitacaoAdiantamentoInsumos(task):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value
    # curso = "teste"
    # data_inicio = "teste"
    # data_final = "teste"
    # cidade_realizacao = "teste"
    # endereco_realizacao = "teste"

    solProtocInstRefer = task.variables['solProtocInstRefer'].value
    adiantEqExecValorIns = task.variables['adiantEqExecValorIns'].value
    adiantEqExecCronogramaRealizIns = task.variables['adiantEqExecCronogramaRealizIns'].value
    adiantEqExecNomeCompletoIns = task.variables['adiantEqExecNomeCompletoIns'].value
    adiantEqExecCpfIns = task.variables['adiantEqExecCpfIns'].value
    adiantEqExecRgIns = task.variables['adiantEqExecRgIns'].value
    adiantEqExecCargoIns = task.variables['adiantEqExecCargoIns'].value
    adiantEqExecNascimentoIns = task.variables['adiantEqExecNascimentoIns'].value
    adiantEqExecOrgaoEmissorIns = task.variables['adiantEqExecOrgaoEmissorIns'].value
    adiantEqExecEnderecoIns = task.variables['adiantEqExecEnderecoIns'].value
    adiantEqExecCepIns = task.variables['adiantEqExecCepIns'].value
    adiantEqExecEmailIns = task.variables['adiantEqExecEmailIns'].value
    adiantEqExecTelefoneIns = task.variables['adiantEqExecTelefoneIns'].value
    adiantEqExecBancoIns = task.variables['adiantEqExecBancoIns'].value
    adiantEqExecAgenciaIns = task.variables['adiantEqExecAgenciaIns'].value
    adiantEqExecContaIns = task.variables['adiantEqExecContaIns'].value
    adiantEqExecPixIns = task.variables['adiantEqExecPixIns'].value
    adiantEqExecDataLimiteIns = task.variables['adiantEqExecDataLimiteIns'].value
    adiantEqExecInstReferenciaIns = task.variables['adiantEqExecInstReferenciaIns'].value

    textoAdiantamentoCombustivel = mountParte("Solicitação de Adiantamento Para Insumos")
    textoAdiantamentoCombustivel += "Solicitamos adiantamento do valor de R$"+adiantEqExecValorIns+",00,"
    textoAdiantamentoCombustivel += "para "+ adiantEqExecNomeCompletoIns+", para compra de insumos prerecíveis do curso de "
    textoAdiantamentoCombustivel += curso+", para a cidade de " + cidade_realizacao + " (GO), cujas aulas serão de "  +data_inicio + " a " + data_final
    textoAdiantamentoCombustivel += ", vinculado ao COTEC"+ solProtocInstRefer+", para o GPS."

    textoAdiantamentoCombustivel += mountParte("VALOR <br> R$ "+adiantEqExecValorIns+",00",)
    textoAdiantamentoCombustivel += mountParte("DADOS PESSOAIS")
    textoAdiantamentoCombustivel += mountParte("Nome", adiantEqExecNomeCompletoIns)
    textoAdiantamentoCombustivel += mountParte("CPF", adiantEqExecCpfIns)
    textoAdiantamentoCombustivel += mountParte("Cargo", adiantEqExecCargoIns)
    textoAdiantamentoCombustivel += mountParte("Data de Nascimento", adiantEqExecNascimentoIns)
    textoAdiantamentoCombustivel += mountParte("RG", adiantEqExecRgIns)
    textoAdiantamentoCombustivel += mountParte("Órgão Emissor", adiantEqExecOrgaoEmissorIns)
    textoAdiantamentoCombustivel += mountParte("Endereço", adiantEqExecEnderecoIns)
    textoAdiantamentoCombustivel += mountParte("CEP", adiantEqExecCepIns)
    textoAdiantamentoCombustivel += mountParte("E-mail", adiantEqExecEmailIns)
    textoAdiantamentoCombustivel += mountParte("Telefone", adiantEqExecTelefoneIns)
    textoAdiantamentoCombustivel += mountParte("Banco", adiantEqExecBancoIns)
    textoAdiantamentoCombustivel += mountParte("Agencia", adiantEqExecAgenciaIns)
    textoAdiantamentoCombustivel += mountParte("Conta", adiantEqExecContaIns)

    return textoAdiantamentoCombustivel


def mountDadosSolicitante(task):
    curso = task.variables['cursos'].value
    data_inicio = task.variables['data_inicio'].value
    data_final = task.variables['data_fim'].value
    cidade_realizacao = task.variables['cidade_realizacao'].value
    endereco_realizacao = task.variables['endereco_realizacao'].value
    
    # curso = "tste"
    # data_inicio = "tste"
    # data_final = "tste"
    # cidade_realizacao = "tste"
    # endereco_realizacao = "tste"

    solProtocEmail = task.variables['solProtocEmail'].value
    solProtocNomeCompleto = task.variables['solProtocNomeCompleto'].value
    solProtocTelefone = task.variables['solProtocTelefone'].value
    solProtocInstRefer = task.variables['solProtocInstRefer'].value
    solProtocProjeto = task.variables['solProtocProjeto'].value

    dadosSolicitante = {
        "email": solProtocEmail,
        "name": solProtocNomeCompleto,
        "phone": solProtocTelefone,
        "instituicao": solProtocInstRefer,
        "projeto": solProtocProjeto,
        "subject":curso+"-"+cidade_realizacao+"-"+solProtocNomeCompleto,
    }

    return dadosSolicitante

def saveOnJumla(dadosSolicitante, message, tipo):
    # subject: tipo de requisição:

    obj = {
        "authentication": {
            "api_key": "4157603089f949dcb76aea92088823e0",
            "api_secret": "20d4a4959a421a4615d8f7aca545a0457800354268559e3ed3fc724ef1dc8c29"
        },
        "data": {
            "email": dadosSolicitante["email"],
            "priorityid": "3",
            "name": dadosSolicitante["name"],
            "phone": dadosSolicitante["phone"],
            "departmentid": "27",
            "projeto": dadosSolicitante["projeto"],
            "instituicao": dadosSolicitante["instituicao"],
            "subject": tipo + "-"+dadosSolicitante["subject"],
            "message": message,
            "etapa": "Cadastrado",
            "limite_execucao": "data do cronograma: novo campo",
        }
    }
    json_dump = json.dumps(obj)
    URL = "https://protocolo2.cett.dev.br/plugins/jssupportticket/js_support_ticket_API/js_support_ticket_API.php"
    return requests.post(
        URL,
        json_dump
    )

worker=Worker()

if __name__ == '__main__':
    print('Worker started')
    while True:

        tasks = worker.fetch_tasks()

        for task in tasks:
            # print(task.variables)
            try:

                mensagemSolTransporte = ""
                if task.variables['tipoSolTransporte'].value == "veiculo":
                    mensagemSolTransporte = mountSolicitacaoAluguelVeiculo(task)
                if task.variables['tipoSolTransporte'].value == "servico":
                    mensagemSolTransporte = mountSolicitacaContratServico(task)
                if task.variables['tipoSolTransporte'].value == "passagem":
                    mensagemSolTransporte = mountSolicitacaCompraPassagem(task)

                dadosSolicitante = mountDadosSolicitante(task)

                cpfDiariaProf = task.variables['solDiariasProfCpf'].value
                mensagemSolDiariaProf = ""
                if cpfDiariaProf:
                    mensagemSolDiariaProf = mountSolicitacaDiariaProf(task)

                cpfAdiantComb = task.variables['adiantEqExecCpfComb'].value
                mensagemSolAdiantComb = ""
                if cpfAdiantComb:
                    mensagemSolAdiantComb = mountSolicitacaoAdiantamentoCom(task)

                cpfAdiantInsumo = task.variables['adiantEqExecCpfIns'].value
                mensagemSolAdiantInsumo = ""
                if cpfAdiantInsumo:
                    mensagemSolAdiantInsumo = mountSolicitacaoAdiantamentoInsumos(task)

                cpfDiariaMotorista = task.variables['solDiariasMotoristaCpf'].value
                mensagemSolDiariaMotorista = ""
                if cpfDiariaMotorista and cpfDiariaProf != cpfDiariaMotorista:
                    mensagemSolDiariaMotorista = mountSolicitacaDiariaMotorista(task)

                mensagemDiariaAuxExt = ""
                for i in range(int(task.variables['qtdAuxExt'].value)):
                    mensagemDiariaAuxExt += "<br>"
                    mensagemDiariaAuxExt += mountSolicitacaDiariaAuxExt(task, str(i+1))

                # print(mensagemSolTransporte)
                # print(mensagemDiariaAuxExt)
                # print(mensagemSolDiariaProf)
                # print(mensagemSolDiariaMotorista)
                # print(mensagemSolAdiantComb)
                # print(mensagemSolAdiantInsumo)
                # print(dadosSolicitante)

                mensagem = mensagemSolTransporte
                response = ""
                ticketIdSolicitacaoTransporte = ""
                if mensagem != "":
                    response = saveOnJumla(dadosSolicitante, mensagem, "solicitação de transporte")
                    print(response.content)
                    response = json.loads(response.content)
                    ticketIdSolicitacaoTransporte = response["ticketid"]

                mensagem = mensagemDiariaAuxExt
                mensagem += mensagemSolDiariaProf
                mensagem += mensagemSolDiariaMotorista
                response = ""
                ticketIdSolicitacaoDiaria = ""
                if mensagem != "":
                    response = saveOnJumla(dadosSolicitante, mensagem, "solicitação de diária")
                    response = json.loads(response.content)
                    ticketIdSolicitacaoDiaria = response["ticketid"]

                mensagem = mensagemSolAdiantComb
                mensagem += mensagemSolAdiantInsumo
                response = ""
                ticketIdSolicitacaoAdiantamento = ""
                if mensagem != "":
                    response = saveOnJumla(dadosSolicitante, mensagem, "solicitação de adiantamento")
                    response = json.loads(response.content)
                    ticketIdSolicitacaoAdiantamento = response["ticketid"]

                variables={
                    "ticketIdSolicitacaoTransporte": {"value": ticketIdSolicitacaoTransporte, "name": "ticketIdSolicitacaoTransporte"},
                    "ticketIdSolicitacaoDiaria": {"value": ticketIdSolicitacaoDiaria, "name": "ticketIdSolicitacaoDiaria"},
                    "ticketIdSolicitacaoAdiantamento": {"value": ticketIdSolicitacaoAdiantamento, "name": "ticketIdSolicitacaoAdiantamento"},
                }

                print("depois do upload", variables)
                worker.complete_task(
                    task_id=task.id_,
                    variables={
                        "ticketIdSolicitacaoTransporte": {"value": ticketIdSolicitacaoTransporte, "name": "ticketIdSolicitacaoTransporte"},
                        "ticketIdSolicitacaoDiaria": {"value": ticketIdSolicitacaoDiaria, "name": "ticketIdSolicitacaoDiaria"},
                        "ticketIdSolicitacaoAdiantamento": {"value": ticketIdSolicitacaoAdiantamento, "name": "ticketIdSolicitacaoAdiantamento"},
                    }
                )
            except:
                pass

        print('Inserção realizada com sucesso!')
        time.sleep(5)


