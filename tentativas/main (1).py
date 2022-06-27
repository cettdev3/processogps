from email import charset
from unicodedata import name
from caworker import Worker
import time
import MySQLdb
from matplotlib.font_manager import json_dump, json_load


worker=Worker()

#ATUALIZA FORMULÁRIO DE INSPEÇÃO
def update_form(idSql,
                nome,
                endereco,
                curso,
                qtd_salas,
                capacidade,
                qtd_cadeiras,
                qtd_tomadas,
                qtd_janelas,
                tipo_climatizacao,
                qualidade_iluminacao,
                turnos_disponiveis,
                qtd_banheiro,
                rede_eletrica,
                qualidade_bebedouro,
                acessibilidade,
                internet,
                data_show,
                limpeza,
                link_imagens,
                parecer,
                possui_cozinha,
                capacidade_cozinha,
                qtd_tomadas_cozinha,
                funcionalidade_fogao,
                refrigeracao,
                gas,
                bancadas_mesas,
                capacidade_fornos,
                qtd_fornos,
                ventilacao_cozinha,
                torneiras_funcionam,
                area_complementar,
                observacao_cozinha,
                laboratorio_informatica,
                qtd_computadores,
                cabeamento_internet,
                qtd_computadores_wifi,
                obs_informatica,
                lavatorio,
                qtd_lavatorio_sb,
                cadeiras_de_sb,
                qtd_cadeiras_sb,
                tipoAvaliacao
                ):
    mydb = MySQLdb.connect(
        host="200.137.215.82",	   # seu host
        user="c3selecao3bd",	  # seu user
        passwd="q#b3FgZ3A",		# sua senha
        db="c3selecao3bd")		 # nome do seu banco de dados
    # Cria Cursor
    c = mydb.cursor()

    sql = "UPDATE solicitacao_infra SET nome='"+ nome + "',endereco='"+ endereco + "',curso='"+ curso + "',qtd_salas='"+ qtd_salas + "',capacidade='"+ capacidade + "',qtd_cadeiras='"+ qtd_cadeiras + "',qtd_tomadas='"+ qtd_tomadas + "',qtd_janelas='"+ qtd_janelas + "',tipo_climatizacao='"+ tipo_climatizacao + "',qualidade_iluminacao='"+ qualidade_iluminacao + "',turnos_disponiveis='"+ turnos_disponiveis + "',qtd_banheiro='"+ qtd_banheiro + "',rede_eletrica='"+ rede_eletrica + "',qualidade_bebedouro='"+ qualidade_bebedouro + "',acessibilidade='"+ acessibilidade + "',internet='"+ internet + "',data_show='"+ data_show + "',limpeza='"+ limpeza + "',link_imagens='"+ link_imagens + "',parecer='"+ parecer + "',possui_cozinha='"+ possui_cozinha + "',capacidade_cozinha='"+ capacidade_cozinha + "',qtd_tomadas_cozinha='"+ qtd_tomadas_cozinha + "',funcionalidade_fogao='"+ funcionalidade_fogao + "',refrigeracao='"+ refrigeracao + "',gas='"+ gas + "',bancadas_mesas='"+ bancadas_mesas + "',capacidade_fornos='"+ capacidade_fornos + "',qtd_fornos='"+ qtd_fornos + "',ventilacao_cozinha='"+ ventilacao_cozinha + "',torneiras_funcionam='"+ torneiras_funcionam + "',area_complementar='"+ area_complementar + "',observacao_cozinha='"+ observacao_cozinha + "',laboratorio_informatica='"+ laboratorio_informatica + "',qtd_computadores='"+ qtd_computadores + "',cabeamento_internet='"+ cabeamento_internet + "',qtd_computadores_wifi='"+ qtd_computadores_wifi + "',obs_informatica='"+ obs_informatica + "',lavatorio='"+ lavatorio + "',qtd_lavatorio_sb='"+ qtd_lavatorio_sb + "',cadeiras_de_sb='"+ cadeiras_de_sb + "',qtd_cadeiras_sb='"+ qtd_cadeiras_sb + "' WHERE id = '" + str(idSql)+"'"

    c.execute(sql)

    mydb.commit()
    print('Update realizado com sucesso!')

#INSERE UM NOVO FORMULÁRIO DE INSPEÇÃOA
def insert_form(nome,
                endereco,
                curso,
                qtd_salas,
                capacidade,
                qtd_cadeiras,
                qtd_tomadas,
                qtd_janelas,
                tipo_climatizacao,
                qualidade_iluminacao,
                turnos_disponiveis,
                qtd_banheiro,
                rede_eletrica,
                qualidade_bebedouro,
                acessibilidade,
                internet,
                data_show,
                limpeza,
                link_imagens,
                parecer,
                possui_cozinha,
                capacidade_cozinha,
                qtd_tomadas_cozinha,
                funcionalidade_fogao,
                refrigeracao,
                gas,
                bancadas_mesas,
                capacidade_fornos,
                qtd_fornos,
                ventilacao_cozinha,
                torneiras_funcionam,
                area_complementar,
                observacao_cozinha,
                laboratorio_informatica,
                qtd_computadores,
                cabeamento_internet,
                qtd_computadores_wifi,
                obs_informatica,
                lavatorio,
                qtd_lavatorio_sb,
                cadeiras_de_sb,
                qtd_cadeiras_sb
):
    mydb = MySQLdb.connect(
        host="200.137.215.82",	   # seu host
        user="c3selecao3bd",	  # seu user
        passwd="q#b3FgZ3A",		# sua senha
        db="c3selecao3bd")			 # nome do seu banco de dados
    # Cria Cursor
    c = mydb.cursor()

    sql = "INSERT INTO solicitacao_infra (nome,endereco,curso,qtd_salas,capacidade,qtd_cadeiras,qtd_tomadas,qtd_janelas,tipo_climatizacao,qualidade_iluminacao,turnos_disponiveis,qtd_banheiro,rede_eletrica,qualidade_bebedouro,acessibilidade,internet,data_show,limpeza,link_imagens,parecer,possui_cozinha,capacidade_cozinha,qtd_tomadas_cozinha,funcionalidade_fogao,refrigeracao,gas,bancadas_mesas,capacidade_fornos,qtd_fornos,ventilacao_cozinha,torneiras_funcionam,area_complementar,observacao_cozinha,laboratorio_informatica,qtd_computadores,cabeamento_internet,qtd_computadores_wifi,obs_informatica,lavatorio,qtd_lavatorio_sb,cadeiras_de_sb,qtd_cadeiras_sb) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s)"
    val = (nome,endereco,curso,qtd_salas,capacidade,str(qtd_cadeiras),qtd_tomadas,qtd_janelas,tipo_climatizacao,qualidade_iluminacao,turnos_disponiveis,qtd_banheiro,rede_eletrica,qualidade_bebedouro,acessibilidade,internet,str(data_show),limpeza,link_imagens,parecer,possui_cozinha,capacidade_cozinha,qtd_tomadas_cozinha,funcionalidade_fogao,refrigeracao,gas,bancadas_mesas,capacidade_fornos,qtd_fornos,ventilacao_cozinha,torneiras_funcionam,area_complementar,observacao_cozinha,laboratorio_informatica,qtd_computadores,cabeamento_internet,qtd_computadores_wifi,obs_informatica,lavatorio,qtd_lavatorio_sb,cadeiras_de_sb,qtd_cadeiras_sb)
    c.execute(sql, val)

    mydb.commit()

#FAZ A CONSULTA NO BANCO FORMULARIO ESPECIFICO
def select_form(id):
    mydb = MySQLdb.connect(
        host="200.137.215.82",	   # seu host
        user="c3selecao3bd",	  # seu user
        passwd="q#b3FgZ3A",		# sua senha
        db="c3selecao3bd")			 # nome do seu banco de dados
    # Cria Cursor
    c = mydb.cursor()

    # Executa o comando SQL
    c.execute('SELECT * FROM solicitacao_infra WHERE id ="'+str(id)+'"')

    # Imprimir toda a primeira c�lula de todas as linhas
    fatura = ''
    for l in c.fetchall():
        nome = str(l[1])
        endereco = str(l[2])
        curso = str(l[3])
        qtd_salas = str(l[4])
        capacidade = str(l[5])
        qtd_cadeiras = str(l[6])
        qtd_tomadas = str(l[7])
        qtd_janelas = str(l[8])
        tipo_climatizacao = str(l[9])
        qualidade_iluminacao = str(l[10])
        turnos_disponiveis = str(l[11])
        qtd_banheiro = str(l[12])
        rede_eletrica = str(l[13])
        qualidade_bebedouro = str(l[14])
        acessibilidade = str(l[15])
        internet = str(l[16])
        data_show = str(l[17])
        limpeza = str(l[18])
        link_imagens =  str(l[19])
        parecer =  str(l[20])
        possui_cozinha = str(l[21])
        capacidade_cozinha = str(l[22])
        qtd_tomadas_cozinha = str(l[23])
        funcionalidade_fogao = str(l[24])
        refrigeracao = str(l[25])
        gas = str(l[26])
        bancadas_mesas = str(l[27])
        capacidade_fornos = str(l[28])
        qtd_fornos = str(l[29])
        ventilacao_cozinha = str(l[30])
        torneiras_funcionam = str(l[31])
        area_complementar = str(l[32])
        observacao_cozinha = str(l[33])
        laboratorio_informatica = str(l[34])
        qtd_computadores = str(l[35])
        cabeamento_internet = str(l[36])
        qtd_computadores_wifi = str(l[37])
        obs_informatica = str(l[38])
        lavatorio = str(l[39])
        qtd_lavatorio_sb = str(l[40])
        cadeiras_de_sb = str(l[41])
        qtd_cadeiras_sb = str(l[42])
        
        #MONTAGEM DO JSON
        #payload = '{"variables":{"cursos": {"value": "'+str(curso)+'" },"cidade_realizacao": {"value": "'+str(cidade_realizacao)+'" },"endereco_realizacao": {"value": "'+str(endereco_realizacao)+'" },"data_inicio": {"value": "'+str(data_inicio)+'" },"data_fim": {"value": "'+str(data_final)+'" },"previsao_alunos": {"value": "'+str(previsao_alunos)+'" },"carga_horaria": {"value": "'+str(carga_horaria)+'" },"num_turmas": {"value": "'+str(qtd_turmas)+'" },"user_login": {"value": "'+str(user)+'" },"user": {"value": "'+str(instancia)+'" }  }  }'
        payload = {
                
                "nome": {"value": nome,"name":"nome"},
                "endereco": {"value": endereco, "name": "endereco"},
                "curso": {"value": curso, "name": "curso"},
                "qtdSalasDisponiveis": {"value": qtd_salas, "name": "qtd_salas"},
                "capacidadeMediaSalas": {"value": capacidade, "name": "capacidade"},
                "qtdCadeiras": {"value": qtd_cadeiras, "name": "qtd_cadeiras"},
                "qtdTomadas": {"value": qtd_tomadas, "name": "qtd_tomadas"},
                "qtdJanelas": {"value": qtd_janelas, "name": "qtd_janelas"},
                "ventilacao": {"value": tipo_climatizacao, "name": "tipo_climatizacao"},
                "boaIluminacao": {"value": qualidade_iluminacao, "name": "qualidade_iluminacao"},
                "turnosDisponiveis": {"value": turnos_disponiveis, "name": "turnos_disponiveis"},
                "qtdBanheiros": {"value": qtd_banheiro, "name": "qtd_banheiro"},
                "redeEletricaAdequada": {"value": rede_eletrica, "name": "rede_eletrica"},
                "bebedor": {"value": qualidade_bebedouro, "name": "qualidade_bebedouro"},
                "acessivelPCD": {"value": acessibilidade, "name": "acessibilidade"},
                "internetWifi": {"value": internet, "name": "internet"},
                "datashow": {"value": data_show, "name": "data_show"},
                "equipeLimpeza": {"value": limpeza, "name": "limpeza"},
                "parecerTecnico": {"value": link_imagens, "name": "link_imagens"},
                "parecerInfra": {"value": parecer, "name": "parecer"},
                "possuiCozinha": {"value": possui_cozinha, "name": "possui_cozinha"},
                "qtdTrabalhadoresCozinha": {"value": capacidade_cozinha, "name": "capacidade_cozinha"},
                "qtdTomadasCozinha": {"value": qtd_tomadas_cozinha, "name": "qtd_tomadas_cozinha"},
                "fogaoFuncional": {"value": funcionalidade_fogao, "name": "funcionalidade_fogao"},
                "possuiGeladeira": {"value": refrigeracao, "name": "refrigeracao"},
                "gasCozinha": {"value": gas, "name": "gas"},
                "bancadas_mesas": {"value": bancadas_mesas, "name": "bancadas_mesas"},
                "capacidadeFornosQuarenta": {"value": capacidade_fornos, "name": "capacidade_fornos"},
                "qtdFornos": {"value": qtd_fornos, "name": "qtd_fornos"},
                "cozinhaArejada": {"value": ventilacao_cozinha, "name": "ventilacao_cozinha"},
                "piasTorneiras": {"value": torneiras_funcionam, "name": "torneiras_funcionam"},
                "espacoFrenteCozinha": {"value": area_complementar, "name": "area_complementar"},
                "obsEspecialidadeCozinha": {"value": observacao_cozinha, "name": "observacao_cozinha"},
                "laboratorioInformatica": {"value": laboratorio_informatica, "name": "laboratorio_informatica"},
                "qtdComputadoresLaboratorio": {"value": qtd_computadores, "name": "qtd_computadores"},
                "cabeamentoInternetLaboratorio": {"value": cabeamento_internet, "name": "cabeamento_internet"},
                "qtdComputadoresCaboWifi": {"value": qtd_computadores_wifi, "name": "qtd_computadores_wifi"},
                "obsEspecialidadeLaboratorio": {"value": obs_informatica, "name": "obs_informatica"},
                "lavatorio": {"value": lavatorio, "name": "lavatorio"},
                "qtdLavatorios": {"value": qtd_lavatorio_sb, "name": "qtd_lavatorio_sb"},
                "cadeirasSalaoCurso": {"value": cadeiras_de_sb, "name": "cadeiras_de_sb"},
                "qtdCadeirasCurso": {"value": qtd_cadeiras_sb, "name": "qtd_cadeiras_sb"}
                
                  

        }
       
    mydb.close()
    return payload

def get_variables():
    idQuery = task.variables['idFormularioInfra'].value
    nome = task.variables['nome'].value
    endereco = task.variables['endereco'].value
    curso = task.variables['curso'].value
    qtd_salas = task.variables['qtd_salas'].value
    capacidade = task.variables['capacidade'].value
    qtd_cadeiras = task.variables['qtd_cadeiras'].value
    qtd_tomadas = task.variables['qtd_tomadas'].value
    qtd_janelas = task.variables['qtd_janelas'].value
    tipo_climatizacao = task.variables['tipo_climatizacao'].value
    qualidade_iluminacao = task.variables['qualidade_iluminacao'].value
    turnos_disponiveis = task.variables['turnos_disponiveis'].value
    qtd_banheiro = task.variables['qtd_banheiro'].value
    rede_eletrica = task.variables['rede_eletrica'].value
    qualidade_bebedouro = task.variables['qualidade_bebedouro'].value
    acessibilidade = task.variables['acessibilidade'].value
    internet = task.variables['internet'].value
    data_show = task.variables['data_show'].value
    limpeza = task.variables['limpeza'].value
    link_imagens = task.variables['link_imagens'].value
    #-------------------------------------------------------------
    parecer = task.variables['parecer'].value
    possui_cozinha = task.variables['possui_cozinha'].value
    capacidade_cozinha = task.variables['capacidade_cozinha'].value
    qtd_tomadas_cozinha = task.variables['qtd_tomadas_cozinha'].value
    funcionalidade_fogao = task.variables['funcionalidade_fogao'].value
    refrigeracao = task.variables['refrigeracao'].value
    gas = task.variables['gas'].value
    bancadas_mesas = task.variables['bancadas_mesas'].value
    capacidade_fornos = task.variables['capacidade_fornos'].value
    qtd_fornos = task.variables['qtd_fornos'].value
    ventilacao_cozinha = task.variables['ventilacao_cozinha'].value
    torneiras_funcionam = task.variables['torneiras_funcionam'].value
    area_complementar = task.variables['area_complementar'].value
    observacao_cozinha = task.variables['observacao_cozinha'].value
    laboratorio_informatica = task.variables['laboratorio_informatica'].value
    qtd_computadores = task.variables['qtd_computadores'].value
    cabeamento_internet = task.variables['cabeamento_internet'].value
    qtd_computadores_wifi = task.variables['qtd_computadores_wifi'].value
    obs_informatica = task.variables['obs_informatica'].value
    lavatorio = task.variables['lavatorio'].value 
    qtd_lavatorio_sb = task.variables['qtd_lavatorio_sb'].value
    cadeiras_de_sb = task.variables['cadeiras_de_sb'].value
    qtd_cadeiras_sb = task.variables['qtd_cadeiras_sb'].value
    
    tipoAvaliacao = task.variables['tipoAvaliacao'].value
    return idQuery,nome,endereco,curso,qtd_salas,capacidade,qtd_cadeiras,qtd_tomadas,qtd_janelas,tipo_climatizacao,qualidade_iluminacao,turnos_disponiveis,qtd_banheiro,rede_eletrica,qualidade_bebedouro,acessibilidade,internet,data_show,limpeza,link_imagens,parecer,possui_cozinha,capacidade_cozinha,qtd_tomadas_cozinha,funcionalidade_fogao,refrigeracao,gas,bancadas_mesas,capacidade_fornos,qtd_fornos,ventilacao_cozinha,torneiras_funcionam,area_complementar,observacao_cozinha,laboratorio_informatica,qtd_computadores,cabeamento_internet,qtd_computadores_wifi,obs_informatica,lavatorio,qtd_lavatorio_sb,cadeiras_de_sb,qtd_cadeiras_sb,tipoAvaliacao,


if __name__ == '__main__':
    print('Worker started')
    while True:
        
        tasks = worker.fetch_tasks()

        for task in tasks:
            try:
                nome = task.variables['user_login'].value
                endereco = task.variables['endereco_realizacao'].value
                curso = task.variables['cursos'].value
                qtd_salas = task.variables['qtdSalasDisponiveis'].value
                capacidade = task.variables['capacidadeMediaSalas'].value
                qtd_cadeiras = task.variables['qtdCadeiras'].value
                qtd_tomadas = task.variables['qtdTomadas'].value
                qtd_janelas = task.variables['qtdJanelas'].value
                tipo_climatizacao = task.variables['ventilacao'].value
                qualidade_iluminacao = task.variables['boaIluminacao'].value
                turnos_disponiveis = task.variables['turnosDisponiveis'].value
                qtd_banheiro = task.variables['qtdBanheiros'].value
                rede_eletrica = task.variables['redeEletricaAdequada'].value
                qualidade_bebedouro = task.variables['bebedor'].value
                acessibilidade = task.variables['acessivelPCD'].value
                internet = task.variables['internetWifi'].value
                data_show = task.variables['datashow'].value
                limpeza = task.variables['equipeLimpeza'].value
                link_imagens = task.variables['parecerTecnico'].value
                #-------------------------------------------------------------
                parecer = task.variables['parecerInfra'].value
                possui_cozinha = task.variables['possuiCozinha'].value
                capacidade_cozinha = task.variables['qtdTrabalhadoresCozinha'].value
                qtd_tomadas_cozinha = task.variables['qtdTomadasCozinha'].value
                funcionalidade_fogao = task.variables['fogaoFuncional'].value
                refrigeracao = task.variables['possuiGeladeira'].value
                gas = task.variables['gasCozinha'].value
                bancadas_mesas = task.variables['bancadas'].value
                capacidade_fornos = task.variables['capacidadeFornosQuarenta'].value
                qtd_fornos = task.variables['qtdFornos'].value
                ventilacao_cozinha = task.variables['cozinhaArejada'].value
                torneiras_funcionam = task.variables['piasTorneiras'].value
                area_complementar = task.variables['espacoFrenteCozinha'].value
                observacao_cozinha = task.variables['obsEspecialidadeCozinha'].value
                laboratorio_informatica = task.variables['laboratorioInformatica'].value
                qtd_computadores = task.variables['qtdComputadoresLaboratorio'].value
                cabeamento_internet = task.variables['cabeamentoInternetLaboratorio'].value
                qtd_computadores_wifi = task.variables['qtdComputadoresCaboWifi'].value
                obs_informatica = task.variables['obsEspecialidadeLaboratorio'].value
                lavatorio = task.variables['lavatorios'].value 
                qtd_lavatorio_sb = task.variables['qtdLavatorios'].value
                cadeiras_de_sb = task.variables['cadeirasSalaoCurso'].value
                qtd_cadeiras_sb = task.variables['qtdCadeirasCurso'].value
                
                tipoAvaliacao = task.variables['tipoAvaliacao'].value
            except:
                pass

            tipoAvaliacao = task.variables['tipoAvaliacao'].value
            if tipoAvaliacao == 'novo' and task.activity_id != 'editUpdate':
                insert_form(nome,
                endereco,
                curso,
                qtd_salas,
                capacidade,
                qtd_cadeiras,
                qtd_tomadas,
                qtd_janelas,
                tipo_climatizacao,
                qualidade_iluminacao,
                turnos_disponiveis,
                qtd_banheiro,
                rede_eletrica,
                qualidade_bebedouro,
                acessibilidade,
                internet,
                data_show,
                limpeza,
                link_imagens,
                parecer,
                possui_cozinha,
                capacidade_cozinha,
                qtd_tomadas_cozinha,
                funcionalidade_fogao,
                refrigeracao,
                gas,
                bancadas_mesas,
                capacidade_fornos,
                qtd_fornos,
                ventilacao_cozinha,
                torneiras_funcionam,
                area_complementar,
                observacao_cozinha,
                laboratorio_informatica,
                qtd_computadores,
                cabeamento_internet,
                qtd_computadores_wifi,
                obs_informatica,
                lavatorio,
                qtd_lavatorio_sb,
                cadeiras_de_sb,
                qtd_cadeiras_sb)
                worker.complete_task(task_id=task.id_)
            
            elif tipoAvaliacao == 'editar' and task.activity_id != 'editUpdate':
                idQuery = task.variables['idFormularioInfra'].value
                payload = select_form(idQuery)
                
                worker.complete_task(task_id=task.id_,variables=payload)
            
            elif task.activity_id == 'editUpdate':
                variaveis = get_variables()
                update_form(variaveis[0],variaveis[1],variaveis[2],variaveis[3],variaveis[4],variaveis[5],variaveis[6],variaveis[7],variaveis[8],variaveis[9],variaveis[10],variaveis[11],variaveis[12],variaveis[13],variaveis[14],variaveis[15],variaveis[16],variaveis[17],variaveis[18],variaveis[19],variaveis[20],variaveis[21],variaveis[22],variaveis[23],variaveis[24],variaveis[25],variaveis[26],variaveis[27],variaveis[28],variaveis[29],variaveis[30],variaveis[31],variaveis[32],variaveis[33],variaveis[34],variaveis[35],variaveis[36],variaveis[37],variaveis[38],variaveis[39],variaveis[40],variaveis[41],variaveis[42],variaveis[43])
                payload = select_form(variaveis[0])
                worker.complete_task(task_id=task.id_,variables=payload)

            print('Inserção realizada com sucesso!')
        time.sleep(5)


