import mechanize
import os
import time

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
url = "http://www.freesms.com.pk"

def banner():
    clear()
    print '''
 ________  ___ _____                _           
/  ___|  \/  |/  ___|              | |          
\ `--.| .  . |\ `--.  ___ _ __   __| | ___ _ __ 
 `--. \ |\/| | `--. \/ _ \ '_ \ / _` |/ _ \ '__|
/\__/ / |  | |/\__/ /  __/ | | | (_| |  __/ |   
\____/\_|  |_/\____/ \___|_| |_|\__,_|\___|_|   
                                                
                                                
Select from (1-2):
1)-SMS Bomber
2)-Send Message
3)-Exit
    '''
    option = raw_input("Option:")
    option = int(option)
    if option == 1:
        print "Not Yet"
        #_input(option)
    elif option == 2:
        _input(option)
    elif option == 3:
        br.close()
        exit()
    else:
        print "Invalid Input"
        time.sleep(2)
        banner()

#------COLLECTER--------------------------------
def collect():
    print "Starting ...."
    res = br.open(url)
    br.select_form("form1")
    br["mnumber"] = "03144910578"
    br["password"] = "95855"
    rpns = br.submit()
    if rpns.geturl() == "http://www.freesms.com.pk/sms0.php":
        br.select_form("form1")
        clear()
    else:
        print "Check your Internet connection"

#-------INPUT--------------------------------  
def _input(x):
    r_number = raw_input("Receiver Number:")
    message = raw_input("Your Message:")
    br["rnumber"] = r_number
    br["msg"] = message
    if x == 1:
        print "Feature Not added yet!"
    elif x == 2:
        times = 1
        send_sms(times)
    else: print "Error Connection"

#-------SMS SEND--------------------------------        
def send_sms(x):
    for i in range(x):
        sms_sender()

#--------Single SMS----------------------------
def sms_sender():
    rpns2 = br.submit()
    if rpns2.geturl() == "http://www.freesms.com.pk/sms1.php":
        print "checking..."
    else:
        print "Fail..."
    br.select_form("form1")
    rpns3 = br.submit()
    if rpns3.geturl() == "http://www.freesms.com.pk/send_sms.php":
        print "sent successfully!"
        banner()
    else: print "falied"

#-------Clear--------------------------
def clear():
    os.system("cls")

collect()
banner()

