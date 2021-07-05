# outlook_mail_send_automation.py

# works well in windows platform, soon will try to debug/develop a code for ubutnu platform.

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:51:21 2020
@author: girishsj
"""

import win32com.client as win32

 
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'recipient@company.com'
mail.Subject = 'Temprovary Mail Subject'
mail.Body = 'Temprovary Mail Body'
attachment  = 'Attach some screenshot/documents'
mail.Attachments.Add(attachment)
mail.Send()
