def setVariables():
    ticketIdSolicitacaoTransporte = "teste"
    ticketIdSolicitacaoDiaria = ""
    ticketIdSolicitacaoAdiantamento = ""
    ticketIdSolicitacaoInsumosKits = "insumosKits"
    variables = {}

    if ticketIdSolicitacaoTransporte:
        variables["ticketIdSolicitacaoTransporte"] = {"value": ticketIdSolicitacaoTransporte, "name": "ticketIdSolicitacaoTransporte"}
    if ticketIdSolicitacaoDiaria:
        variables["ticketIdSolicitacaoDiaria"] = {"value": ticketIdSolicitacaoDiaria, "name": "ticketIdSolicitacaoDiaria"}
    if ticketIdSolicitacaoAdiantamento:
        variables["ticketIdSolicitacaoAdiantamento"] = {"value": ticketIdSolicitacaoAdiantamento, "name": "ticketIdSolicitacaoAdiantamento"}
    if ticketIdSolicitacaoInsumosKits:
        variables["ticketIdSolicitacaoInsumosKits"] = {"value": ticketIdSolicitacaoInsumosKits, "name": "ticketIdSolicitacaoInsumosKits"}

    return variables

variables = setVariables()
print(variables)