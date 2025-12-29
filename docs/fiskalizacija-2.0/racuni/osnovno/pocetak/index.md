---
title: Početak
tags:
  - fiskalizacija 2.0
keywords:
  - pocetak
  - racuni
  - osnovno
---
## UVOD

Nakon što ste uspješno napravili prethodna 3 koraka pripreme za uvođenje F2, vrijeme je da napravite posljednji, 4-ti korak. A to je provjera pristupne točke i upoznavanje s načinom rada F2.

!!! danger "Važna napomena"
    Odmah na početku moramo vam reći da **NIJE MOGUĆE TESTIRATI** slanje eRačuna po pravilima F2. To je bilo moguće samo programerima i to u ograničenom obimu.

??? question "Kako ćete provjeriti imate li novu verziju programa?"
    **Metoda 1:**
    Ako u izborniku **Matični-Ostalo** vidite novu opciju **Parametri za eRačun**, onda sigurno imate novu verziju.

    **Metoda 2:**
    Provjera se nalazi na opciji **Pomoć-Promjene u programu**. Ako je verzija za module programa koji su vezani uz izdavanje i primanje računa **25.12.22** (zadnji broj 22 ili veći), imate novu verziju.

    !!! failure "Što ako nemate novu verziju?"
        Ako otkrijete da nemate novu verziju, izađite iz Milenij programa i ponovno ga pokrenite. Ukoliko niti nakon novog pokretanja ne budete imali novu verziju, javite nam se mailom ili telefonom pa ćemo provjeriti zbog čega je nastao problem s nadogradnjom.

## Provjera pristupne točke

Ako ste do sada već koristili slanje eRačuna preko MeR-a, vrlo vjerojatno imate postavljeno korisničko ime i lozinku u programu za pristupnu točku koju ste odabrali.

Za provjeru otvorite **Matični-Ostalo-Parametri za eRačun**. Otvorit će se novi prozor gdje možete provjeriti upisane podatke. Ako nisu upisani, upišite ih i spremite. Dobili ste ih kada ste s MeR-om potpisali ugovor.

## Kome se izdaje kakav račun?

Odluku o tome kome šaljete kakav račun automatski donosi program na temelju podataka koje mu pripremite. Tip računa ovisi o dva faktora: kome izdajete račun i koji je način plaćanja računa.

Evo kratkog podsjetnika kako će se računi knjižiti:

=== "Gotovina / Kartica"

    * **Firme iz Hrvatske**: Fiskalizacija 1.0
    * **Firme iz EU i ostalih zemalja**: Fiskalizacija 1.0
    * **Građani**: Fiskalizacija 1.0

    !!! note "Podsjetnik"
        Fiskalizacija 1.0 je fiskalizacija putem certifikata za fiskalizaciju, a kao potvrda ispravno napravljene fiskalizacije na računu se ispisuje **ZKI** i **JIR**.

    Za gotovinu/kartice svi računi se fiskaliziraju na stari način (F1), ali je važno naglasiti sljedeće:

    !!! warning "OIB je obavezan"
        Za firme iz Hrvatske u adresaru mora biti upisan ispravan OIB. U protivnom firma neće dobiti ispravan račun. Ali, to nije ništa novo, to je vrijedilo i do sada. Razlika je u tome što se sada taj OIB zajedno s ostalim podacima o fiskalizaciji računa šalje u Poreznu upravu.

=== "Transakcijsko plaćanje"

    * **Firme iz Hrvatske**: eRačun (Fiskalizacija 2.0)
    * **Firme iz EU i ostalih zemalja**: papirnati račun/PDF
    * **Građani**: Fiskalizacija 1.0

    Za ispravnu izradu računa koji se plaćaju putem transakcijskog načina plaćanja veliku važnost imaju podaci o kupcu koje ste upisali u adresar. Evo kako treba ispravno upisati svakog od ovih kupaca:

    !!! tip "Ako se radi o firmi iz Hrvatske"
        * **OIB**: 11 brojeva
        * **Tip kupca**: *Obveznik PDV-a*, *Obveznik PDV- po naplati* ili *Nije obveznik PDV-a*. (Ako imate našu knjigovodstvenu aplikaciju, znat ćete koji tip odabrati. Ako nemate, svejedno je koji ćete od ova tri odabrati.)
        * **eRačun F 2.0**: *Obavezno slanje eRačuna*

        > Najbolje je da klikom miša na tekst **eRačun F 2.0** pomoću programa u AMS-u provjerite je li za tog kupca obavezno slanje eRačuna. Za sve firme u Hrvatskoj trebali bi postaviti da su obveznici primanja eRačuna. Problem može nastati samo za one koji se još nisu prijavili u AMS (po zakonu su to bili obavezni).

    !!! tip "Ako se radi o firmi iz EU ili izvan EU"
        * **OIB**: njihov PDV broj (obično sadrži i ime zemlje, npr. SI45631782)
        * **Tip kupca**: svejedno je koji od prva tri postavite, samo da nije *Građani*
        * **eRačun F 2.0**: *Ostali*

    !!! tip "Ako se radi o građanima (fizičkim osobama)"
        * **OIB**: nepotrebno
        * **Tip kupca**: *Građani, potrošači, ostali*
        * **eRačun F 2.0**: *Ostali*

---

!!! info "Savjet prije zaključivanja"
    Prije zaključenja svakog računa poželjno je provjeriti koje kriterije račun zadovoljava (informacija se prikazuje u zaglavlju računa), pa možete na vrijeme reagirati ako prepoznate da nije onako kako bi trebalo biti.

!!! warning "Ispravak pogrešaka"
    Ako uočite da nešto nije u redu, ispravak možete napraviti **samo prije zaključenja računa**, i to ispravnim podešavanjem tri spomenuta ključna podatka u adresaru kupaca.
    
    Ako podatke promijenite u adresaru nakon zaključenja računa, tip tog računa se neće promijeniti. Račun će ostati zapisan s parametrima kakvi su bili u trenutku zaključenja računa.

!!! important "NOVA VERZIJA PROGRAMA"
    U NOVOJ VERZIJI PROGRAMA, PROZORI ZA IZRADU RAČUNA ĆE BITI ISTI KAO I DO SADA SVE DO KRAJA 2025. GODINE.
    
    NOVI ĆE BITI ADRESAR KUPACA/DOBAVLJAČA I PARAMETRI ZA E RAČUN KAKO BISTE TE PODATKE MOGLI POČETI UPISIVATI VEĆ SADA.

    OSTALE MOGUĆNOSTI IZRADE ERAČUNA OPISANE U DALJNJEM TEKSTU UPUTA IMAT ĆETE NA ŽALOST TEK OTVARANJEM NOVE 2026. GODINE.
