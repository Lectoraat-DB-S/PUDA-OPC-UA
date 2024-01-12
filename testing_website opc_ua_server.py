import requests
import paramiko
import json
from opcua import Server
#from opcua import Server, ua
i = 0
server = Server()
# Setup server endpoint
server.set_endpoint("opc.tcp://10.38.4.227:4840/freeopcua/server/")
# Setup server namespace
uri = "http://example.org"
idx = server.register_namespace(uri)
# Create a new object and variable
myobj = server.nodes.objects.add_object(idx, "MyObject")
myvar = myobj.add_variable(idx, "MyVariable", 0.0)
myvar1 = myobj.add_variable(idx, "MyVariable1", 0.0)
myvar2 = myobj.add_variable(idx, "MyVariable2", 0.0)
# Start the server
server.start()
string_test = ""
JSON_test1 = "json1"
JSON_test2 = "json2"
JSON_test3 = "json3"
JSON_File_Test = '{JSON_test1, JSON_test2, JSON_test3}'
jsondump = json.dumps(JSON_File_Test)
octoprint_api_key_1 = "46094ADCA1E34CB1A43DA34F0F5D33EB "
octoprint_ip_1 = "10.38.4.145"
ubuntu_file_path_1 = '/home/Bingus/Octoprint/ExampleData.json'
octoprint_api_key_2 = "B8CBA95AD6B04954A161C38EF689C9BA"
octoprint_ip_2 = "10.38.4.178:5000"
ubuntu_file_path_2 = '/home/Bingus/Octoprint/Data.json'

def versturen(octoprint_api_key, octoprint_ip, ubuntu_file_path, printerNummer):
    # Instellingen voor de OctoPrint-server
    #octoprint_api_key = "46094ADCA1E34CB1A43DA34F0F5D33EB "
    #octoprint_ip = "10.38.4.145"

    # Instellingen voor de Ubuntu-server
    ubuntu_ip = "10.38.4.167"
    ubuntu_user = "Bingus"
    ubuntu_password = "Bongus"

    # URL om de JSON-gegevens op te halen van de OctoPrint-server
    octoprint_url_printer = f"http://{octoprint_ip}/api/printer"
    octoprint_url_print = f"http://{octoprint_ip}/api/job"

    # Ophalen van JSON-gegevens van OctoPrint
    response_printer = requests.get(octoprint_url_printer, headers={"X-Api-Key": octoprint_api_key})
    response_print = requests.get(octoprint_url_print, headers={"X-Api-Key": octoprint_api_key})
    
    if response_printer.status_code == 200 and response_print.status_code == 200:
        data = response_printer.json()
        print(data)
        data_print = response_print.json()
        #print(data_print)
        #print("")
        #changebleJSON = json.loads(data)
        #print(data)
        SDReady = data["sd"]["ready"]
        StateError = data["state"]["error"]
        StateFlagsCancelling =data["state"]["flags"]["cancelling"]
        StateFlagsClosedOrError =data["state"]["flags"]["closedOrError"]
        StateFlagsError =data["state"]["flags"]["error"]
        StateFlagsFinishing =data["state"]["flags"]["finishing"]
        StateFlagsOperational =data["state"]["flags"]["operational"]
        StateFlagsPaused =data["state"]["flags"]["paused"]
        StateFlagsPausing =data["state"]["flags"]["pausing"]
        StateFlagsPrinting =data["state"]["flags"]["printing"]
        StateFlagsReady =data["state"]["flags"]["ready"]
        StateFlagsResuming =data["state"]["flags"]["resuming"]
        StateFlagsSdReady =data["state"]["flags"]["sdReady"]
        CurrentState = data["state"]["text"]
        try:
            if "temperature" in data_print and "bed" in data_print["temperature"] and "actual" in data_print["temperature"]["bed"]:
                temperatureBedActual = data["temperature"]["bed"]["actual"]
            else:
                temperatureBedActual = data["temperature"]["bed"]["actual"]
        except:
            temperatureBedActual =  "none"
        try:
            if "temperature" in data_print and "bed" in data_print["temperature"] and "offset" in data_print["temperature"]["bed"]:
                temperatureBedOffset = data["temperature"]["bed"]["offset"]
            else:
                temperatureBedOffset = data["temperature"]["bed"]["offset"]
        except:
            temperatureBedOffset = "None"
        try:
            if "temperature" in data_print and "bed" in data_print["temperature"] and "target" in data_print["temperature"]["bed"]:
                temperatureBedTarget = data["temperature"]["bed"]["target"]
            else:
                temperatureBedTarget = data["temperature"]["bed"]["target"]
        except:
            temperatureBedTarget = "None"
        try:
            if "temperature" in data_print and "tool0" in data_print["temperature"] and "actual" in data_print["temperature"]["tool0"]:
                temperatureTool0Actual = data["temperature"]["tool0"]["actual"]
            else:
                temperatureTool0Actual = data["temperature"]["tool0"]["actual"]
        except:
            temperatureTool0Actual = "None"
        try:
            if "temperature" in data_print and "tool0" in data_print["temperature"] and "offset" in data_print["temperature"]["tool0"]:
                temperatureTool0Offset = data["temperature"]["tool0"]["offset"]
            else:
                temperatureTool0Offset = data["temperature"]["tool0"]["offset"]
        except:
            temperatureTool0Offset = "None"
        try:
            if "temperature" in data_print and "tool0" in data_print["temperature"] and "target" in data_print["temperature"]["tool0"]:
                temperatureTool0Target = data["temperature"]["tool0"]["target"]
            else:
                temperatureTool0Target = data["temperature"]["tool0"]["target"]
        except:
            temperatureTool0Target = "None"
        try:
            if "job" in data_print and "averagePrintTime" in data_print["job"]:
                averagePrintTime = data_print["job"]["averagePrintTime"]
            else:
                #print("Sleutels bestaan niet in de verwachte structuur. word null gemaakt")
                averagePrintTime = "None"
        except KeyError:
            #print("bestaat niet")
            averagePrintTime = data_print["job"]["averagePrintTime"]

        if data_print["job"]["estimatedPrintTime"] != None:
            estimatedPrintTime = data_print["job"]["estimatedPrintTime"]
        else:
            estimatedPrintTime = "None"

        try:
            if "job" in data_print and "filament" in data_print["job"] and data_print["job"]["filament"] != None and "tool0" in data_print["job"]["filament"]:
                toolLengh = data_print["job"]["filament"]["tool0"]["length"]
                toolVolume = data_print["job"]["filament"]["tool0"]["volume"]
            else:
                #print("Sleutels bestaan niet in de verwachte structuur. word null gemaakt")
                toolLengh = "none"
                toolVolume = "None"
        except KeyError:
            print("bestaat niet")

        #toolLengh = data_print["job"]["filament"]["tool0"]["length"]
        #toolVolume = data_print["job"]["filament"]["tool0"]["volume"]
        if data_print["job"]["file"]["date"] != None:
            fileDate = data_print["job"]["file"]["date"]
        else:
            fileDate = "None"
        try:
            if "job" in data_print and "file" in data_print["job"] and "display" in data_print["job"]["file"]:
                fileDisplay = data_print["job"]["file"]["display"]
            else:
                #print("Sleutels bestaan niet in de verwachte structuur. word null gemaakt")
                fileDisplay = "None"
        except KeyError:
            print("bestaat niet")

        #fileDisplay = data_print["job"]["file"]["display"]
        if data_print["job"]["file"]["name"] != None:
            fileName = data_print["job"]["file"]["name"]
        else:
            fileName = "None"
        if data_print["job"]["file"]["origin"] != None:
            fileOrigin = data_print["job"]["file"]["origin"]
        else: 
            fileOrigin = "None"
        if data_print["job"]["file"]["path"] != None:
            filePath = data_print["job"]["file"]["path"]
        else:
            filePath = "None"
        if data_print["job"]["file"]["size"] != None:
            fileSize = data_print["job"]["file"]["size"]
        else:
            fileSize = "None"
        if data_print["job"]["lastPrintTime"] != None:
            LastPrintTime = data_print["job"]["lastPrintTime"]
        else:
            LastPrintTime = "None"
        if data_print["job"]["user"] != None:
            printUser = data_print["job"]["user"]
        else:
            printUser = "None"
        if data_print["progress"]["completion"] != None: 
            printcompletion = data_print["progress"]["completion"]
        else:
            printcompletion = "None"
        if data_print["progress"]["filepos"] != None:
            filePos = data_print["progress"]["filepos"]
        else:
            filePos = "None"
        if data_print["progress"]["printTime"] != None:
            printTime = data_print["progress"]["printTime"]
        else: 
            printTime = "None"
        if data_print["progress"]["printTimeLeft"] == None:
            printTimeLeft = "none"
        else:
            printTimeLeft = data_print["progress"]["printTimeLeft"]           
        try:
            if "progress" in data_print and "printTimeLeftOrigin" in data_print["progress"]:
                printTimeLeftOrigin = data_print["progress"]["printTimeLeftOrigin"]
            else:
                #print("Sleutels bestaan niet in de verwachte structuur. word null gemaakt")
                printTimeLeftOrigin = "None"
        except KeyError:
            print("bestaat niet")
        #printTimeLeftOrigin = data_print["progress"]["printTimeLeftOrigin"]
        SendFile = {"SDReady": SDReady,
                    "StateError": StateError,
                    "StateFlagsCancelling": StateFlagsCancelling,
                    "StateFlagsClosedOrError": StateFlagsClosedOrError,
                    "StateFlagsError": StateFlagsError,
                    "StateFlagsFinishing" : StateFlagsFinishing,
                    "StateFlagsOperational" : StateFlagsOperational,
                    "StateFlagsPaused": StateFlagsPaused,
                    "StateFlagsPausing": StateFlagsPausing,
                    "StateFlagsReady": StateFlagsReady,
                    "StateFlagsResuming": StateFlagsResuming,
                    "StateFlagsSdReady": StateFlagsSdReady,
                    "CurrentState": CurrentState,
                    #"temperatureWActual": temperatureWActual,
                    #"temperatureWOffset": temperatureWOffset,
                    #"temperatureWTarget": temperatureWTarget,
                    "temperatureBedActual": temperatureBedActual,
                    "temperatureBedOffset": temperatureBedOffset,
                    "temperatureBedTarget": temperatureBedTarget,
                    "temperatureTool0Actual": temperatureTool0Actual,
                    "temperatureTool0Offset": temperatureTool0Offset,
                    "temperatureTool0Target": temperatureTool0Target,
                    "averagePrintTime": averagePrintTime,
                    "estimatedPrintTime": estimatedPrintTime,
                    "toolLengh": toolLengh,
                    "toolVolume": toolVolume,
                    "fileDate": fileDate,
                    "fileDisplay": fileDisplay,
                    "fileName": fileName,
                    "fileOrigin": fileOrigin,
                    "filePath": filePath,
                    "fileSize": fileSize,
                    "LastPrintTime": LastPrintTime,
                    "printUser": printUser,
                    "printcompletion": printcompletion,
                    "filePos": filePos,
                    "printTime": printTime,
                    "printTimeLeft": printTimeLeft,
                    "printTimeLeftOrigin": printTimeLeftOrigin
                    }
        #print(SendFile)
        #print("")

        # Maak een verbinding met de Ubuntu-server via SSH (SCP)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ubuntu_ip, username=ubuntu_user, password=ubuntu_password)

        # SCP de JSON-gegevens naar de Ubuntu-server
        with ssh_client.open_sftp() as sftp:
            with sftp.file(ubuntu_file_path, "w") as f:
                f.write(json.dumps(SendFile))
        jsondump = json.dumps(SendFile)
        myvar.set_value(i)
        if (printerNummer == 1):
            myvar1.set_value(jsondump)
        if (printerNummer == 2):
            myvar2.set_value(jsondump)
            #f.write(json.dumps(data))

        ssh_client.close()
        
        #print("")
        print("JSON-gegevens zijn met succes naar de Ubuntu-server verzonden. naar ip bestand")
        print( ubuntu_file_path)
        print("*************************************")
        print(SendFile)
        print("*************************************")


    else:
        print("Fout bij het ophalen van de JSON-gegevens:", response_printer.status_code)
        print(ubuntu_file_path + "is nog niet aangepast")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ubuntu_ip, username=ubuntu_user, password=ubuntu_password)

        # SCP de JSON-gegevens naar de Ubuntu-server
        #with ssh_client.open_sftp() as sftp:
        #with sftp.file(ubuntu_file_path, "w") as f:
        #f.write(json.dumps(SendFile))
        myvar.set_value(i)
        if (printerNummer == 1):
            myvar1.set_value("printer uit")
        if (printerNummer == 2):
            myvar2.set_value("printer uit ")
            #f.write(json.dumps(data))

while(1):
    versturen(octoprint_api_key_1, octoprint_ip_1, ubuntu_file_path_1, 1)
    versturen(octoprint_api_key_2, octoprint_ip_2, ubuntu_file_path_2, 2)
    i = i+1
