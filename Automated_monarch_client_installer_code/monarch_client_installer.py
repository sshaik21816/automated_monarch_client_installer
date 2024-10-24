"""moarch client installtion"""

import sys, os, shutil, subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyQt5', '--quiet'])
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def window():
    """help"""
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(1200, 300, 700, 500)
    win.setWindowTitle("Client_Installer")
    win.setStyleSheet("background-color: silver")
    win.setToolTip("ClientInstaller")
    win.setWindowIcon(QIcon('installer.jpeg'))
    FMS_button = "FMS"; ADMS_button = "ADMS";EMS_button = "EMS/GMS"; Exit_button = "Exit"
    
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Client Installer')
    lbl_name.move(310, 0)
		
    def remove_old_file():
        newpath = r"D:\\client_installation"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        for root, dirs, files in os.walk("D:\\client_installation"):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
	
    def clicked_fms(self):
        print( FMS_button + "  FMS_Client installation started...")
        remove_old_file()

        """ Copying the client.exe file from the server and renamed the client.exe file name in your local system folder """
        try:
            subprocess.run(["pscp", "-pw", "AdminAdmin1", "osiserv_act@fms-awbdac1.sct.local:D:/osi/monarch/products/ITS*.exe", "D:/client_installation/FMS_ITS_Full_Client.exe"], check=True)
        except Exception as error:
            print(f"Error installing FMS client due to: {error}")
        my_list = ["monarchNET.exe -unattended", "taskkill /f /im monarchNET.exe"]
        client_name = "FMS_ITS_Full_Client.exe"
        os.chdir("D:\\client_installation")
        if client_name == "FMS_ITS_Full_Client.exe" and os.path.exists("D:/client_installation/FMS_ITS_Full_Client.exe"):
            """unzipping the client.exe file"""
            subprocess.run(r'"C:\Program Files\7-Zip\7z.exe" x D:\client_installation\FMS_ITS_Full_Client.exe', check=True)
            os.chdir("D:\\client_installation\\installOSImonarchNET")
        else:
            print("File is not available")
            exit()

        for cmd in my_list:
            os.system(cmd)
	
    FMS_button_save = QtWidgets.QPushButton(win)
    FMS_button_save.setText(FMS_button)
    FMS_button_save.move(300, 130)
    FMS_button_save.clicked.connect(clicked_fms)
	
    def clicked_adms(self):
        print( ADMS_button + " ADMS_Client installation started...")
        remove_old_file()
        """ Copying the client.exe file from the server and renamed the client.exe file name in your local system folder """
        try:
            subprocess.run(["pscp", "-pw", "AdminAdmin1", "osiserv_act@adms-wbdac1:D:/osi/monarch/products/ADMS_ITS_*.exe", "D:/client_installation/ADMS_Client.exe"], check=True)
        except Exception as error:
            print(f"Error installing ADMS client due to: {error}")
        my_list = ["monarchNET.exe -unattended", "taskkill /f /im monarchNET.exe"]
        client_name = "ADMS_Client.exe"
        os.chdir("D:\\client_installation")
        if client_name == "ADMS_Client.exe" and os.path.exists("D:/client_installation/ADMS_Client.exe"):
            """unzipping the client.exe file"""
            subprocess.run(r'"C:\Program Files\7-Zip\7z.exe" x D:\client_installation\ADMS_Client.exe', check=True)
            os.chdir("D:\\client_installation\\installOSImonarchNET")
        else:
            print("File is not available")
            exit()

        for cmd in my_list:
            os.system(cmd)
	
    ADMS_button_save = QtWidgets.QPushButton(win)
    ADMS_button_save.setText(ADMS_button)
    ADMS_button_save.move(300, 230)
    ADMS_button_save.clicked.connect(clicked_adms)
	
    def clicked_ems_gms(self):
        print( EMS_button + "EMS_Client installation started...")
        remove_old_file()
        """ Copying the client.exe file from the server and renamed the client.exe file name in your local system folder """
        try:
            subprocess.run(["pscp", "-pw", "AdminAdmin1", "osiserv_act@sct-wbdac1.sct.local:D:/osi/monarch/products/full_client_*.exe", "D:/client_installation/EMS_GMS_Client.exe"], check=True)
        except Exception as error:
            print(f"Error installing EMS_GMS client due to: {error}")
        my_list = ["monarchNET.exe -unattended", "taskkill /f /im monarchNET.exe"]
        client_name = "EMS_GMS_Client.exe"
        os.chdir("D:\\client_installation")
        if client_name == "EMS_GMS_Client.exe" and os.path.exists("D:/client_installation/EMS_GMS_Client.exe"):
            """unzipping the client.exe file"""
            subprocess.run(r'"C:\Program Files\7-Zip\7z.exe" x D:\client_installation\EMS_GMS_Client.exe', check=True)
            os.chdir("D:\\client_installation\\installOSImonarchNET")
        else:
            print("File is not available")
            exit()

        for cmd in my_list:
            os.system(cmd)
	
    EMS_button_save = QtWidgets.QPushButton(win)
    EMS_button_save.setText(EMS_button)
    EMS_button_save.move(300, 330)
    EMS_button_save.clicked.connect(clicked_ems_gms)
	
    Exit_button_save = QtWidgets.QPushButton(win)
    Exit_button_save.setText(Exit_button)
    Exit_button_save.move(300, 430)
    Exit_button_save.clicked.connect(sys.exit)
	
    win.show()
    sys.exit(app.exec_())

window()
