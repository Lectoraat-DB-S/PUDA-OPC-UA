Versie van libraries  

paramiko           	3.3.1 
pip                	23.3.1 
requests           	2.31.0 
freeopcua	0.90.6   

Volg de volgende stappen om alles te installeren. 

Run eerst de volgende comando's om pyhton 3 te krijgen 

	cd ~ 
	sudo apt update 
	sudo apt install python3 python3-pip python3-dev python3-setuptools python3-venv git libyaml-dev build-essential libffi-dev libssl-dev 
	mkdir OctoPrint && cd OctoPrint 
	python3 -m venv venv 
	source venv/bin/activate 

Op de raspberry Pi os 64bit zitten de libraries requests en json er al op dus die kun je importen. Mocht dat niet zo zijn kun je ze instaleren via 

	Sudo apt install python-requests	
en  

	sudo apt install python-json  

Om de paramiko library en de freeopcua library te krijgen moet je de volgende commands runnen. 

	Sudo apt install python-paramiko   
	Sudo apt install pyhton-freeopcua 

 start eerst de OPC UA server en daarna pas de OPC UA client. 

 

 
