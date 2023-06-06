# netprog-p4

Project developed for the NetProg course

## Requirements

Ciascun gruppo dovrà creare una soluzione che combina le due esercitazioni di:
- Asymmetric Flow
- My Tunnel

In particolare lo scopo dell'esame è creare una soluzione p4 che preveda:
- La possibilità di monitorare l'asimmetria tra flussi nel REGOLARE traffico ipv4 senza header modificato.
- La possibilità di processare del traffico con un header customizzato ( like My Tunnel ) che, tra i vari header necessari, contenga:
  * Un campo IP_Mal che possa contenere un indirizzo ip ( di default inizializzato a 0.0.0.0)
  * Un camp TIME che possa contenere un valore Unix Time ( di default inizializzato a 0 )
  * Un campo flag che possa contenere un intero ( inizializzato a 0 ).

Il programma deve quindi comportarsi come asymmetric flow nel caso generale con ipv4, quando però la treshold della differenza viene raggiunta il programma deve:
- Prima di tutto registrare in un opportuno registro ( chiamato TRESHOLD) i dati relativi all'ultimo pacchetto che ha causato la treshold ovvero:
  - Ip sorgente
  - Ip destinazione
  - Timestamp ultimo pacchetto
- Secondo NON deve droppare i pacchetti ma devo comunque continuare a forwardarli correttamente.

**CONTEMPORANEAMENTE**

Il programma deve essere in grado di processare i pacchetti del protocollo custom, che per quanto riguarda l'indirizzamento si comporta esattamente come myTunnel ( quindi la porta di destinazione è specificata con *--dst-id* ) ma che abbia una funzionalità in più.

Ogni volta che processata un pacchetto myTunnel, prima di "accettarlo" ( ovvero fare l'apply della tabella ) dove controllare se nel registro TRESHOLD definito precedentemente è stato scritto un valore che segnala il raggiungimento della treshold per un determinato flusso. IN CASO POSITIVO dovete, prima di accettare il pacchetto, scrivere dei valori nel campo dell'header corrispondende del pacchetto.

In particolare:

Gruppo E: (Serafini Andrea – Sanchi Piero – Mazzanti Gustavo)
- Scrivere nel campo TIME il timestamp del pacchetto che ha raggiunto la treshold
- Scrivere nel campo flag il valore 1

Modalità di consegna

Il gruppo dovrà consegnare TUTTA la cartella coi file e le configurazioni scritte, unitamente ad un report (file report.pdf) con tutte le spiegazioni su come è stata svolta la prova e sugli step necessari per poterla eseguire e testare inclusi i comandi di eventuali scripts python.
