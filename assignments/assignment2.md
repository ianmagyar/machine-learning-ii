# Zadanie 2
V druhom zadaní vytvoríte agentov, ktorí dokážu hrať jednoduché hry pre dvoch hráčov s vysokou úspešnosťou. Agentov môžete natrénovať ľubovoľnou metódou učenia posilňovaním. V rámci zadania budete vyvíjať agentov pre tri prostredia: Tic-Tac-Toe, Connect Four a Preteky. Pri trénovaní potrebujete vyriešiť dve úlohy, a to natrénovať čo najlepšieho agenta a optimalizovať trénovanie pre najlepší výkon.

## Prostredia
Agentov potrebujete pripraviť pre tieto prostredia:

* [Tic-Tac-Toe](tictactoe.md)
* [Connect Four](connect.md)
* [Preteky](racing.md)

## Úloha
Vašou úlohou je natrénovať agenta, ktorý bude hrať dané hry s čo najvyššiou úspešnosťou. Pre každé prostredie odovzdáte iba jedného agenta (teda v prípade Tic-Tac-Toe a Connect Four ten istý agent bude raz hrať ako hráč 1, raz ako hráč 2), ktorý bude najlepšie vami natrénovaný agent. Natrénovaných agentov uložte do súborov vami zvoleným spôsobom, kódová implementácia ale musí podporovať načítanie uloženého agenta z týchto súborov. Pri trénovaní agentov môžete použiť ľubovoľný algoritmus reinforcement učenia.

## Štruktúra riešenia
[Na tomto odkaze](assignment2.zip) nájdete kostru riešenia, ktorá obsahuje predpripravené prostredia a kostru vášho riešenia.

Súčasťou odovzdávky bude minimálne sedem súborov:

* `solution_tictactoe.py` - kód agenta pre hru Tic-Tac-Toe (riešenie môžete rozdeliť do viacerých súborov)
* `solution_connect.py` - kód agenta pre hru Connect Four (riešenie môžete rozdeliť do viacerých súborov)
* `solution_race.py` - kód agenta pre hru Preteky (riešenie môžete rozdeliť do viacerých súborov)
* `agent_tictactoe` - agent trénovaný pre hru Tic-Tac-Toe;
* `agent_connect` - agent trénovaný pre hru Connect Four;
* `agent_race` - agent trénovaný pre hru Preteky;
* `requirements.txt` - zoznam všetkých potrebných knižníc pre spustenie Vášho riešenia (návod k príprave súboru nájdete [napríklad tu](https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e).

Kódová implementácia agentov môže obsahovať ľubovoľné funkcie a parametre, pričom nemôžete zmeniť tri požiadavky (kompatibilitu môžete otestovať nahradením niektorého agenta v `main.py` vaším agentom):

1. konštruktor musí mať parameter `code`, ktorý určí kód hráča (hráč 1 má kód 1, hráč 2 má kód -1) a žiadne ďalšie povinné parametre;
2. musíte mať definovanú funkciu `act`, ktorá vráti akciu agenta na základe stavu prostredia (rovnaké rozhranie ako pri štandardných riešeniach s OpenAI gym);
3. trieda musí definovať funkciu `load_agent`, ktorá načíta natrénovaného agenta zo súboru, kde máte uloženého agenta.

## Testovanie
Odovzdané riešenia sa otestujú a vyhodnotia na nasimulovaných hrách (ako v súboroch `main.py`). Práve preto odporúčame trénovanie riešiť mimo funkcie `act` (prípadne zadefinovať parameter, ktorý vypína/zapína trénovanie agenta), aby sa agent neučil počas vyhodnocovania. K získaniu bodov musí váš agent vyhrať nad náhodným agentom vo väčšine iterácií (min. 501).

## Odovzdávanie
Vaše riešenie odovzdávate cez MS Teams ako jeden zip s hore uvedenými súbormi. Termín odovzdania je **21. 4. 2021**, alebo koniec semestra (môžete ale prísť o body za turnaj). Po ovodzvdaní vaše riešenie potrebujete aj obhájiť (spolu so zadaním 1) - termíny budú vypísané pre posledné týždne semestra.

## Hodnotenie
Okrem hodnotenia samotného zadania na konci semestra sa usporiada turnaj agentov vo formáte round robin, t.j. agenti každého študenta s agentmi ostatných študentov. V každom dueli sa nasimuluje 1000 hier pre každé prostredie, v polovici z nich váš agent bude hráč 1, pre druhú polovicu sa poradie hráčov vymení (okrem pretekov). Ak viac ako polovica nasimulovaných hier končí remízou, tak body sa delia v rámci duelu. Za vyhratý duel dostane študent 3 body, za remízu 1 bod, a za prehru žiadne body. Podrobnejší popis podmienok pre výhru nájdete v popisoch prostredí.

Na konci turnaja študenti s agentmi v top tretine tabuľky dostanú 3 body, študenti s agentmi v strede tabuľky 2 body, a študenti v poslednej tretine tabuľky 1 bod. Ak študent do turnaja nezapojí natrénovaných agentov, žiadne body nedostane.

Počas semestra usporiadame tri kolá turnajov, prvé v 6. týždni, druhé v 8. týždni a tretie v 10. týždni (v piatky), medzi jednotlivými kolami máte možnosť pracovať na riešeniach a vylepšovať svojich agentov.

Za zadanie môžete získať maximálne 30 bodov, pričom bodové rozdelenie je nasledovné:

* **správna aplikácia algoritmu a metodológia** - 3 * 4 = 12 bodov
* **turnaj** - 3 * 3 = 9 bodov
* **validácia proti náhodnému agentovi** - 3 * 1 = 3 body
* **obhajoba** - 3 * 2 = 6 bodov
