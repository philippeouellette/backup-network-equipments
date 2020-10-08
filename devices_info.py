#! /usr/bin/env
from credentials import *

"""
Contient les équipements réseaux dont on sauvegarde la configuraton réseau.
"""
__author__ = "Philippe Ouellette"
__author_email__ = "philippe.ouellette@groupeaffi.ca"
__copyright__ = "Groupe AFFI"


cisco = {
      'CABCVRPRV100' :
                  {
                  'device_type': 'cisco_ios',
                  'host':   '10.68.80.1',
                  'username': cisco_username,
                  'password': cisco_password
                  },
      'CABCVCPRV101' :
          {
              'device_type': 'cisco_ios',
              'host':   '10.68.80.101',
              'username': cisco_username,
              'password': cisco_password
          },
      'CABCVCPRV110' :
          {
              'device_type': 'cisco_ios',
              'host':   '10.68.80.110',
              'username': cisco_username,
              'password': cisco_password,
          },
      'CABCVCPRV120' :
          {
              'device_type': 'cisco_ios',
              'host':   '10.68.80.120',
              'username': cisco_username,
              'password': cisco_password,
          }
  }

fortinet = {
      'CABCVFPBL01-HAUT' :
                  {
                  'device_type': 'fortinet',
                  'host':   '10.68.95.254',
                  'username': fortinet_username,
                  'password': fortinet_password
                  },
        'CASTH1FBL01' :
                    {
                    'device_type': 'fortinet',
                    'host':   '10.68.114.1',
                    'username': fortinet_username,
                    'password': fortinet_password
                    },

        'CATERFPBL01' :
                    {
                    'device_type': 'fortinet',
                    'host':   '10.68.96.1',
                    'username': fortinet_username,
                    'password': fortinet_password
                    },
        'CAANJFPBL01' :
                    {
                    'device_type': 'fortinet',
                    'host':   '10.68.34.1',
                    'username': fortinet_username,
                    'password': fortinet_password
                    },
  }
