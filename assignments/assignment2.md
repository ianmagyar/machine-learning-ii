# Zadanie 2

V rámci druhého zadania budete aplikovať algoritmy učenia posilňovaním na riešenie praktických úloh. Okrem samotného algoritmu a agenta implementujete aj prostredie, pričom musíte navrhnúť stavový priestor, priestor akcií, ako aj funkciu odmeny.

## Úloha
Navrhnite a implementujte prostredie podľa popisu úlohy, nejasnosti prekonzultujte s cvičiacim. Potrebujete navrhnúť množinu stavov a akcií, ako aj spôsob odmeňovania. Tieto metodologické voľby musíte vedieť odôvodniť a obhájiť. Po implementácii prostredia potrebujete natrénovať agenta, ktorý danú úlohu vyrieši minimálne dvomi rôznymi algoritmami. Následne vyhodnoťte efektivitu algoritmov podobným spôsobom, ako ste to robili v prvom zadaní.

### Úlohy

#### 1. Prevoz cez rieku
Dedinčan chce previesť loďkou cez rieku vlka, kozu a kapustu. Pri každom prechode však môže zobrať so sebou iba jednu vec. Na žiadnom brehu nemôže ostať vlk spolu s kozou, inak ju zožerie. Rovnaký osud čaká aj kapustu ak ostane osamote s kozou. Navrhnite riešenie, kde pomocou učenia posilňovaním naučíte agenta nájsť riešenie tohto problému. Všetky štyri postavy začínajú na rovnakom brehu rieky, a potrebujú sa dostať na druhý breh.

#### 2. Autopožičovňa
Ste manažérom dvoch pobočiek autopožičovne, obe sa denne tešia obľube zákazníkov. Za každé vypožičanie získate 10 eur (musíte mať voľné auto), ak žiadne auto nemáte na pobočke, o zisk prídete. Autá sú k dispozícii deň potom, čo ich zákazníci vrátia. Cez noc viete preniesť autá z jednej pobočky do druhej pobočky, avšak za cenu 2 eur za kus.
Navrhnite riešenie, kde pomocou učenia posilňovaním naučíte agenta správne vybrať potrebný počet áut na presun medzi pobočkami. Počet vypožičaných a vrátených áut pre obe pobočky viete nasimulovať na základe Poissonovho rozdelenia, kde pre každé možné číslo *n* sa pravdepodobnosť dá vypočítať ako $$\frac{\lambda^{n}}{n!} \cdot e^{-\lambda}$$, kde λ je očakávaná hodnota daného javu. Túto hodnotu načítajte zo súboru (teda bude slúžiť ako parameter prostredia). Potrebujete určiť očakávanú hodnotu pre počet vypožičaných a vrátených áut na oboch pobočkách (teda celkovo štyri hodnoty). Na každej pobočke môžete mať maximálne 20 áut, a preniesť môžete 5 z nich (z jednej do druhej pobočky).

#### 3. Hanojské veže
Hanojské veže sú logický hlavolam, kde máte tri kolíky. Na začiatku hry máte na jednom z nich tri disky rôzneho priemeru, pričom najväčší je na spodku, a najmenší na vrchu. Vašou úlohou je presunúť vežu diskov na druhý kolík, pričom naraz môžete hýbať iba jedným diskom, môžete hýbať iba diskom, ktorý je na vrchu niektorej veže, a väčší disk nemôžete položiť na menší disk. Navrhnite riešenie, kde pomocou učenia posilňovaním natrénujete agenta, ktorý vyrieši tento problém.

#### 4. Stávkovanie
Máte možnosť vsádzať na to, že padne hlava pre niekoľko hodov mincou. Ak naozaj padne hlava, vyhráte dvojnásobok vsadenej sumy (stávka + ešte raz suma stávky), ak padne znak, prídete o sumu stávky. Hra sa končí, ak dosiahnete 100 eur, alebo prídete o všetky vaše peniaze. Pri každom hode môžete určiť sumu vašej stávky (iba celé eurá), nemôžete ale dať takú stávku, aby ste v prípade výhry mali viac ako 100 eur. Implementujte riešenie, ktoré nájde optimálnu stávkovaciu stratégiu pre rôzne hodnoty kapitálu hráča. Prostredie má pritom jeden parameter, a to pravdepodobnosť toho, že padne hlava (nemusí byť presne 0,5). Túto hodnotu načítajte z konfiguračného súboru.

#### 5. 8 Puzzle
8 Puzzle je logická úloha, kde je na mriežke 3x3 usporiadaných 8 štvorčekov označených číslami a jedna voľná pozícia, ktorá umožňuje presúvať štvorčeky hore, dole, doľava alebo doprava. Cieľom hry je usporiadať štvorčeky od 1 po 8 tak, že štvorček s číslom 1 bude v ľavom hornom rohu. Je to zjednodušená verzia hry 15 puzzle. Navrhnite riešenie, kde pomocou učenia posilňovaním natrénujete agenta vyriešiť problém z ľubovoľného platného nastavenia.

Pri simulácii dbajte na to, aby počiatočné nastavenie bolo platné a riešiteľné.

#### 6. Flow Free
Flow Free je logická hra, kde sú na mriežke umiestnené bodky rôznych farieb (každej farby po dve), a cieľom je prepojiť ich tak, aby potrubia vyplnili celú mriežku, a zároveň aby sa nekrížili. Navrhnite riešenie, kde sa agent naučí vyriešiť ľubovoľnú riešiteľnú úlohu s mriežkou 5x5. Mapu si načítajte zo súboru.

[Flow Free si môžete zahrať napríklad na tejto stránke](https://www.silvergames.com/en/flow-free).

#### 7. Žiarliví manželia
Na brehu rieky stoja tri páry novomanželov a potrebujú sa dostať na druhú stranu, pričom môžu použiť iba loďku, ktorá unesie maximálne dvoch ľudí (a samozrejme nemôže prejsť na druhú stranu ak v nej nikto nesedí). Natrénujte reinforcement learning agenta, ktorý vyrieši tento problém, pričom počas celého trvania prechodu cez rieku nemôže ostať žiadna manželka na brehu bez svojho manžela, ak tam zároveň stojí iný muž. V loďke takisto môžu sedieť iba so svojím mužom, alebo inou ženou.

### Algoritmy
Pri vypracovaní zadania môžete použiť ľubovoľný algoritmus pre učenie posilňovaním. Musíte porovnať aspoň minimálne dva algoritmy.

## Štruktúra riešenia
Vaše riešenie musí mať nasledovnú štruktúru:

1. kódová implementácia prostredia - Python skript s implementáciou prostredia ako triedy. Môžete ale nemusíte dodržiavať API knižnice `Gymnasium`.
2. kódová implementácia algoritmov - skripty v Python 3, jeden súbor na každý algoritmus. Kód musí byť spustiteľný. Ak používate pomocné knižnice, všetky musíte uviesť v osobitnom súbore `requirements.txt` s príslušnou verziou knižnice. Skript musí podporiť aj načítanie uloženého agenta.
3. uložení natrénovaní agenti - minimálne jeden (najlepší) agent natrénovaný pre každý algoritmus. Môžete odovzdať aj viac riešení, tieto ale musia byť jednoznačne označené.
4. dokumentácia - súbor s nasledovným obsahom:

    * úvod a popis riešeného problému (stavový priestor, možné akcie, podmienky vyriešenia problému) - podrobne popíšte, ako ste uvažovali o možných návrhoch a ako ste nakoniec implementovali prostredie.
    * použitá funkcia odmeny (*reward function*) - kedy a akú odmenu dostane agent.
    * popis algoritmov - všetky informácie, ktoré človek potrebuje k zreprodukovaniu vášho riešenia.
    * dokumentácia experimentov - s akými hodnotami hyperparametrov ste testovali jednotlivé algoritmy spolu s výsledkami.
    * porovnanie algoritmov na základe vami zvolených kritérií - tabuľková alebo grafová podoba.

## Odovzdávanie
Vaše riešenia odovzdávate cez MS Teams ako jeden zip súbor s hore uvedenou štruktúrou. Termín odovzdania je **19. 4. 2024** (piatok). Po odovzdaní vaše riešenie musíte aj obhájiť - termíny budú vypísané pre posledné dva týždne semestra.

## Hodnotenie
Za zadanie môžete získať maximálne 20 bodov, pričom bodové rozdelenie je nasledovné:

* **návrh a implementácia prostredia**: 8 bodov - hodnotí sa návrh stavového priestoru a priestoru akcií spolu s funkciou odmeny
* **použité metódy a algoritmy**: 2 x 3 body - hodnotí sa správnosť prístupu a riešenia
* **dokumentácia**: 3 body - hodnotí sa kvalita dokumentácie vašej práce
* **obhajoba**: 3 body - hodnotí sa pochopenie kódu, obhajoba slúži aj ako kontrola originality; pri riešení môžete vychádzať z dostupných tutoriálov a ukážok, avšak predpoklad je, že kódu budete aj rozumieť a budete ho vedieť vysvetliť
