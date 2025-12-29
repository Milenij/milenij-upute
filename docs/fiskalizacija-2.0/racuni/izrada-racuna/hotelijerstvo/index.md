---
title: Hotelijerstvo
tags:
  - fiskalizacija 2.0
keywords:
  - hotelijerstvo
---
### Računi za smještaj

Sve do zadnjeg koraka naplate smještaja (izrade računa) nema bitnih promjena. Promjene su vidljive u zadnjem koraku vezano uz Fiskalizaciju 2.0.

* **Nova polja**: Vidjet ćete *Tip računa* (i *Tip poslovnog procesa* ako se radi o eRačunu).
* **KPD šifre**: Važno je da sve usluge imaju upisanu KPD šifru.
* **Datum isporuke**: Kod upisa virmanskog plaćanja, program će ponuditi zadnji datum boravka gosta (ili datum računa, ako je manji).

!!! important "Najvažnije za virmansko plaćanje"
    Kod izrade računa za virmansko plaćanje važno je ispravno postaviti tip kupca:
    * **Strane firme**: Postavite tip *Obveznik PDV-a* (ne fiskalizira se).
    * **Fizičke osobe**: Postavite tip *Građani* (fiskalizira se s F1).

### Avansni računi

Izrada računa za avans nema značajnih promjena. Promjena će se najviše odraziti na virmanske račune firmama iz Hrvatske koje će se (ili neće, ako tako odredite) automatski poslati nakon knjiženja računa.

* **Firme iz EU/ostalih zemalja**: Šalju se na dosadašnji način (PDF, pošta...).
* **KPD šifre**: Nisu potrebne kod avansnih računa.
* **Tip poslovnog procesa**: Uvijek bi trebao biti **P4**.
* **Fizičke osobe (građani)**: Kad fizička osoba (domaći ili stranac) virmanski uplati rezervaciju, **NIJE potrebno upisivati OIB** jer se fiskalizacija računa za građane izvodi kao F1 bez OIB-a.
