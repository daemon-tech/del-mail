import imaplib

email= ""
pwd = ""
imserver = "imap.gmail.com"

def delmail(user, password, IMAP):
	mail = imaplib.IMAP4_SSL(IMAP)
	mail.login(user, password)
	mail.select("inbox")
	typ, data = mail.search(None, 'ALL')
	for num in data[0].split():
		mail.store(num, '+FLAGS', r'(\Deleted)')
	mail.expunge()
	mail.close()
	mail.logout()
    
deleteEmailIMAP(email, pwd, imaserver)
