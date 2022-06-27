<?php

	$curl = curl_init();

	curl_setopt_array($curl, [
		CURLOPT_RETURNTRANSFER => 1,
		CURLOPT_URL => 'https://protocolo2.cett.dev.br/plugins/jssupportticket/js_support_ticket_API/js_support_ticket_API.php',
		// CURLOPT_URL => 'https://protocolo.cett.org.br/plugins/jssupportticket/js_support_ticket_API/js_support_ticket_API.php',
		CURLOPT_POST => 1,
		CURLOPT_POSTFIELDS => [
			'authentication' => json_encode([
				'api_key' => '5cb26ec436a9ddd89ae9cc4499914a5c',
				// 'api_key' => '4157603089f949dcb76aea92088823e0',
				'api_secret' => '928c4c70ff438d5a683ca4d5bbe9cca8bd6535c12eac9960cff4f08f1fa0aea2'
				// 'api_secret' => '20d4a4959a421a4615d8f7aca545a0457800354268559e3ed3fc724ef1dc8c29'
			]),
			'data' => json_encode([
				'email' => 'diegosantos.2001@alunos.utfpr.edu.br',
				'priorityid' => '3',
				'name' => 'Diego Godina Santos',
				'phone' => '13996437301',
				'departmentid' => '27',
				'projeto' => 'EFG',					//ufield_20
				'instituicao' => 'site',			//ufield_22
				'subject' => 'Teste',
				'message' => 'Demanda de teste da API',
				'etapa' => 'Cadastrado',			//ufield_31
				'limite_execucao' => '2022-06-10',	//ufield_25
			])
		]
	]);

	$response = curl_exec($curl);
	curl_close($curl);

	print_r($response);
?>