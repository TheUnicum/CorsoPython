#-*- coding: utf-8 -*-

'''

Prima lezione pyhton !!!!!


1. Installare i programmi necessari per il python sul proprio PC

	1.A
		Installare il traduttore del linguaggio python.
		Su internet ci sono molte versioni python che però si possono raggrupare in 2 famiglie:
			-python 2.7
			-python 3.4
		Noi installeremo la versione python 2.7 perchè è quella preinstallata sul controllo iTNC640

		Per windows installare il file
		"python-2.7.3.msi"

	1.B
		Installare le librerie aggiuntive:

		Sui Controlli iTNC640 si utilizzano le librerie delle librerie chiamata 'gtk' e 'gtk.glade' ,
		e quindi le installeremo anche siu nostri pc.
		Queste librerie servono per l'interfaccia grafica , creazione di finestre (windows), bottoni a video etcc

		Per windows installare il file
		"pygtk-all-in-one-2.24.2.win32-py2.7.msi"

2. Installere un IDE (Integrated development environment)

	Un IDE è un ambiente di sviluppo dove editare e scrivere i nostri programmi python.
	Potrebbe essere sufficente il "Notepad" di windows ma gli IDE forniscono molte funzionalita aggiuntive.

	Su internet ci trovano molti IDE come :

	-PyCharm
	-Pydev
	-Sublime Text 3
	-Ninja-IDE
	....

	la scelta è molto soggettiva .Personalmente a me piace molto "Sublime Text 3"

3. Scrivere il promo programma python

	Questo file stesso "01 - Hello World.py" è uno script python funzionanete

	Comandi Base Elementari:


		-		print <var> 			    : 	stampa sul terminale di uscita la variabile <var>
		-		#							:	inserire un commenta alla riga, (analoga al ';' nel PLCDesign )
		-		'' '						:   digitare 3 apostrofi ('' ') consecutivi per INIZIARE a inserire un commento nello script
		-		'' '						:	digitare 3 apostrofi ('' ') consecutivi per TERMINARE il commento nello script
		-		#-*- coding: utf-8 -*-		:	[Come ultima nota sui commenti non cancellare le prime righe tipo 	[#-*- coding: utf-8 -*-]
				  |								anche se sembrano commenti sono in realta comandi Python]
				  |								Nello specifico questa serve al compilatore python per la codifica dei caratteri non ASCII tipo è
				  |
				  +-----> Ovviamente in questo commento non posso scrivere 3 apostrofi, consecutivi altrimenti verrebbe interpretato come comando




4.	Eseguire lo script python

	Ora è possibile testare se python è installato correttamente sul proprio PC

	- In Sublime Text 3 premere [CTRL + 'B'] e verificare che nella finestra di debug compaia il testo 'Hello World!'

	- Se il programma termina senza errori , dopo il testo 'Hello World' dovrebbe comparire [Finished in x.0s]




Per scrivere il mio primo comando Python devo prima effettuare la chiusura del commento con 3 apostrofi
[PS: per evitare problemi e sempre consigliabile mantenere l'itentazione anche sull'apertuta/chiusura commento ]
'''



print 'Hello World!'

