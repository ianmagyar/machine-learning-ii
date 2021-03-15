# Zadanie 2
V druhom zadaní vytvoríte agenta, ktorý bude ovládať jednoduchú hru Tic-Tac-Toe. Agenta natrénujete ľubovoľnou metódou učenia posilňovaním. Počas riešenia potrebujete vyriešiť dve úlohy, a to natrénovať čo najlepšieho agenta a optimalizovať trénovanie tak, aby čím skôr sa natrénovala dobrá politika.

## Tic-Tac-Toe
Tic-Tac-Toe je jednoduchá hra, v ktorej hráči striedavo umiestňujú znaky `O` a `X` na hracom poli 3x3, a vyhrá ten, ktorému sa skôr podarí umiestniť vedľa seba tri rovnaké znaky, pričom tieto znaky môžu byť v tom istom riadku, v tom istom stĺpci alebo na rovnakej diagonále. Pre hru neexistuje výherná politika, existuje ale spôsob, ako predísť prehre (aspoň  pre prvého hráča).

## Úloha
Vašou úlohou je natrénovať agenta, ktorý dokáže hrať hru Tic-Tac-Toe, pričom odovzdáte troch natrénovaných agentov. Prvý agent bude trénovaný na maximálne 10 000 iteráciach, druhý agent na maximálne 20 000 iteráciach, a tretí agent môžete trénovať na toľkých iteráciach, koľko len chcete (tretí agent by nemal byť horší, ako prví agenti). Natrénovaných agentov uložte do súborov Vami zvoleným spôsobom. Pri trénovaní môžete použiť ľubovoľný algoritmus reinforcement učenia s ľubovoľnými nastaveniami (okrem počtu iterácií pri agentoch 1 a 2).

## Štruktúra riešenia
[Na tomto odkaze](assignment2.zip) nájdete kostru riešenia, ktorá obsahuje nasledovné súbory:

* `tictactoe.py` - implementácia hry Tic-Tac-Toe s rozhraním, ktoré poznáte z OpenAI gym. Vaši agenti môžu komunikovať s týmto prostredím cez funkcie `reset` (pre získanie počiatočného stavu - prázdne hracie pole) a `step` (pre aktualizáciu prostredia na základe akcie agenta).
* `bots.py` - niekoľko botov, ktorých môžete ale nemusíte využiť pri trénovaní, resp. pri vyhodnocovaní Vášho riešenia. `RandomBot` vždy vyberie náhodnú pozíciu a svoj znak umiestní na danú pozíciu. `OneStepBot` vyberie výhernú akciu, ak taká existuje, v opačnom prípade svoj znak umiestní náhodne. `TwoStepBot` vždy vyberie výhernú akciu, alebo zablokuje možnú výhernú akciu protihráča, v opačnom prípade svoj znak umiestní náhodne.
* `main.py` - obsahuje ukážkové testovanie hry s dvomi agentami. Nasimuluje sa 1000 hier, a určí sa, v koľkých vyhrá hráč 1, hráč 2, a koľkokrát nastane remíza.
* `solution.py` - skript pre Vaše riešenie, zadefinujte vlastným spôsobom agenta, teda triedu `StudentAgent`.

Vaše riešenie môže obsahovať ľubovoľné funkcie a parametre, pričom nemôžete zmeniť tri požiadavky (kompatibilitu môžete otestovať nahradením niektorého agenta v `main.py` Vaším agentom):

1. konštruktor musí mať parameter `code`, ktorý určí kód hráča (hráč jeden má kód 1, druhý hráč má kód -1);
2. musíte mať definovanú funkciu `act`, ktorá vráti akciu agenta na základe stavu prostredia (rovnaké rozhranie ako pri štandardných riešeniach s OpenAI gym);
3. trieda musí definovať funkciu `load_agent`, ktorá načíta natrénovaného agenta zo súboru (kde máte uloženého agenta).

Súčasťou odovzdávky bude minimálne šesť súborov:

* `solution.py` - kód agenta (riešenie môžete rozdeliť do viacerých súborov)
* `requirements.txt` - zoznam všetkých potrebných knižníc pre spustenie Vášho riešenia (návod k príprave súboru nájdete [napríklad tu](https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e);
* `agent10000` - agent trénovaný na 10 000 iteráciach;
* `agent20000` - agent trénovaný na 20 000 iteráciach;
* `agent_best` - najlepší natrénovaný agent;
* krátka dokumentácia s popisom použitého algoritmu, spôsobu trénovania a skúsenosťami (na jednu A4).

## Testovanie
Odovzdané riešenia sa otestujú a vyhodnotia na nasimulovaných hrách (ako v súbore `main.py`). Práve preto odporúčame trénovanie riešiť mimo funkcie `act` (prípadne zadefinovať parameter, ktorý vypína/zapína trénovanie agenta), aby agent sa neučil počas vyhodnotenia. K získaniu bodov musí Váš najlepší agent vedieť poraziť náhodného agenta vo väčšine iterácií (min. 501).

## Odovzdávanie
Vaše riešenie odovzdávate cez MS Teams ako jeden zip s hore uvedenými súbormi. Termín odovzdania je **18. 4. 2021**, alebo koniec semestra. Zápočet môžete získať ešte v prvých dvoch týždňoch skúškového obdobia, prídete ale o možnosť získať maximálny počet bodov. Po ovodzvdaní Vaše riešenie potrebujete aj obhájiť (spolu so zadaním 1) - termíny budú vypísané pre posledné dva týždne semestra.

## Hodnotenie
Okrem hodnotenia samotného zadania na konci semestra sa usporiada turnaj Vašich agentov vo formáte round robin, t.j. agenti každého študenta s agentmi ostatných študentov. Každý duel bude mať formu best-of-three, teda postupne sa nasimuluje 1000 hier dvoch agentov trénovaných na 10 000 iteráciach, dvoch agentov trénovaních na 20 000 iteráciach, a dvoch najlepších agentov. Body získa študent, ktorého agenti vyhrajú dva zápasy. Ak viac ako polovica nasimulovaných hier končí remízou, tak body sa delia v rámci zápasu. Za vyhratý duel dostane študent 3 body, za remízu 1 bod, a za prehru žiadne body.

Na konci turnaja študenti s agentmi v top tretine tabuľky dostanú 3 body, študenti s agentmi v strede tabuľky 2 body, a študenti v poslednej tretine tabuľky jeden bod.

Za zadanie môžete získať maximálne 15 bodov, pričom bodové rozdelenie je nasledovné:

* **správna aplikácia algoritmu** - 3 body
* **metodológia pri trénovaní** - 3 body
* **dokumentácia** - 2 body
* **obhajoba** - 2 body
* **validácia proti náhodnému agentovi** - 2 body
* **turnaj** - max. 3 body