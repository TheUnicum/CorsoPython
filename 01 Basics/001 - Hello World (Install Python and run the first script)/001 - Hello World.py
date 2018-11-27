# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""

Prima lezione pyhton !!!!!

1. Installare i programmi necessari per l'esecuzione di "scripts" python sul proprio PC

    1.A
        Installare il traduttore python.
        Su internet ci sono molte versioni python che si possono raggrupare in 2 famiglie:
            -python 2.7
            -python 3.4

        Noi installeremo la versione python 2.7 perchè è quella preinstallata sul controllo iTNC640
        In windows per installare python è sufficiente eseguire il file:
            -"python-2.7.3.msi"

    1.B
        Aggiungere il path (percorso dove risiede l'eseguibile python) alle variabili di sistema di Windows.
        Questa modifica permette l'esecuzione di "python.exe" da qualsiasi cartella senza dover specificare
        ogni volta l'intero percorso.
        Questa modifica alle variabili di sistema ci semplificherà molto l'integrazione di python a IDE esterni (esemp: Sublimetex3).

            - Window 7:
                -> Sistema
                    -> Imporstazioni di sistema avanzate
                        -> [tab "Avanzate"] Variabili d'ambiente
                            -> Nella finestea "Variabili si sistema" selezionare la voce "Path" e cliccare su "Modifica..."
                                -> Nel campo Valore Variabili agguingere (alla fine della lista separando con un puntoEvirgola ;)
                                    "C:\Python\Python27"   [oppore l'attuale percorso se è stato modificato in fase di installazione]

                                -> SALVARE E RIAVVIARE IL SISTEMA!

        Al termine del riavvio è possibile verificare il corretto inserimento del path:
            Aprire la finestra command(cmd) e digitare "python" in qualsiasi percorso, se il comando viene riconosciuto
            la procedura è stata eseuita correttamente. [PS: per usciore da python digitare "quit()"]

    1.C
        Installare le librerie aggiuntive GTK!:

        Sui Controlli iTNC640 si utilizzano le librerie 'gtk' e 'gtk.glade',
        ed è possibilie installere le stesse (o analoghe) librerie anche sui nostri pc.
        Queste librerie servono per l'interfaccia grafica , creazione di finestre (windows), pulsanti a video etcc

        In windows è sufficiente installare il file
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


3. Scrivere il primo programma python

    Questo file stesso "001 - Hello World.py" è uno script python funzionante

    Comandi Base Elementari:

        -       print <var>                 :   stampa sul terminale di uscita la variabile <var>
        -       #                           :   inserire un commenta alla riga, (analogo al ';' nel PLCDesign )
        -       '''	                        :   digitare 3 apostrofi (''') consecutivi per INIZIARE a inserire un commento nello script
        -   +<- '''	                        :   digitare 3 apostrofi (''') consecutivi per TERMINARE il commento nello script
        -   |   '''   /   "" "              :   (<"> <'> l'apostrofo può essere singolo oppure doppio indifferentemente)
        -   |   #-*- coding: utf-8 -*-      :   [Come ultima nota riguardante i commenti NON CANCELLARE le prime righe tipo [#-*- coding: utf-8 -*-]
            |                                    anche se sembrano commenti sono in realta comandi Python]
            |                                    Nello specifico questa serve al compilatore python per la codifica dei caratteri non ASCII tipo <è,à,ù>
            |
            +-------------------> Ovviamente in questo commento non posso scrivere 3 apostrofi, consecutivi altrimenti verrebbe interpretato come comando


4.  Eseguire lo script python

    Ora è possibile testare se python è installato correttamente sul proprio PC

    - In Sublime Text 3 premere [CTRL + 'B'] e verificare che nella finestra di debug compaia il testo 'Hello World!'
        -> In caso di probleme nell'avvio di python verificare: -l'installazione di python              1.A
                                                                -le variabili di ambiente di Windows    1.B

    - Se il programma termina senza errori , dopo il testo 'Hello World' dovrebbe comparire il testo "[Finished in x.0s]"
        Nota: E' importante verificare sempre che il programma termini senza errori e che non si blocchi in loop infiniti .



Per scrivere il mio primo comando Python devo prima effettuare la chiusura del commento con 3 apostrofi
[PS: per evitare problemi e sempre consigliabile mantenere l'itentazione anche sull'apertuta/chiusura commento ]
"""
print 'Hello World!'
