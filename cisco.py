#! /usr/bin/env python
from netmiko import ConnectHandler
import re, os, shutil
from datetime import date
from devices_info import *

"""
Script pour sauvegarder la configuration des équipements réseaux cisco sur le réseau.
"""
__author__ = "Philippe Ouellette"
__author_email__ = "philippe.ouellette@groupeaffi.ca"
__copyright__ = "Groupe AFFI"

def CreateDirectory():
    fullDate = str(date.today().strftime("%d-%m-%Y"))
    monthDate = str(date.today().strftime("%m-%Y"))
    dest = "\\\cabcvsdat01\\boucherville\\FichiersCommuns\\Technologies de l'information\\Infrastructures\\Reseaux\\Backup Configs Network\\"

    if monthDate not in os.listdir(dest):
        os.mkdir(dest + monthDate)#Create the directory with the fulldate in the "month-year" folder
    os.mkdir(dest + monthDate + "\\" + fullDate)

def backup_cisco(equipment_name):
    print("Connexion à " + equipment_name + " ...")
    net_connect = ConnectHandler(**cisco[equipment_name])
    print("Génération de la configuration ...")
    config = net_connect.send_command('show running-config')
    print("Sauvegarde de la configuration ...")
    router_config = open(equipment_name + '.txt','w')
    router_config.write(config)
    router_config.close()
    print("Sauvegarde effectuée !")
    print("")
    shutil.move(equipment_name + '.txt', dest)

def backup_fortinet(equipment_name):
    print("Connexion à " + equipment_name + " ...")
    net_connect = ConnectHandler(**fortinet[equipment_name])
    print("Génération de la configuration ...")
    config = net_connect.send_command('show full-configuration')
    print("Sauvegarde de la configuration ...")
    router_config = open(equipment_name + '.txt','w')
    router_config.write(config)
    router_config.close()
    print("Sauvegarde effectuée !")
    print("")
    shutil.move(equipment_name + '.txt', dest)

def main():
    os.system('cls')

    try:
        CreateDirectory()
    except Exception as e:
        print(e)

    for key in cisco:
        backup_cisco(key)

    for key in fortinet:
        backup_fortinet(key)

main()
