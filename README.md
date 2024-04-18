# Strojové učenie II

**Strojové učenie II** je kurz ponúkaný v letnom semestri tretieho ročníka bakalárskeho štúdia pre študijný program Inteligentné systémy. Predmet nadväzuje na kurzy Umelá inteligencia a Strojové učenie, venuje sa učeniu posilňovaním (*reinforcement learning*).

Informačný list predmetuje je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

## Obsah
1. [Plán prednášok a cvičení](#plan)
2. [Hodnotenie](#grading)
3. [Odporúčaná literatúra](#textbooks)

## Plán prednášok a cvičení <a name="plan"></a>

Prednáška z predmetu je vo štvrtok o 10:50 v miestnosti V102 v budove V4. Cvičenia sú vo štvrtok o 9:10 v miestnosti V102 v budove V4. Účasť na cvičeniach a prednáškach je povinná, študenti môžu mať maximálne tri neúčasti za semester.

|                               |                       Prednáška                       |                  Cvičenie                  |            Termíny             |
|:-----------------------------:|:-----------------------------------------------------:|:------------------------------------------:|--------------------------------|
|  1. týždeň<br>12. 2. - 18. 2. |              Úvod do učenia posilňovaním              |  Úvod do predmetu<br>[Matematické základy](https://marian.mach.website.tuke.sk/presentations/su2/prez-matrep.pdf)   | [Z1 zverejnené](assignments/assignment1.md)                  |
|  2. týždeň<br>19. 2. - 25. 2. |            Markovovské rozhodovacie procesy           | [Návrh a implementácia vlastného prostredia](labs/lab02-creating-environments.ipynb) |                                |
|  3. týždeň<br>26. 2. - 3. 3.  |                Dynamické programovanie                |             [Bellmanove rovnice](labs/lab03-bellman-equation.ipynb)             | [Z2 zverejnené](assignments/assignment2.md)                  |
|  4. týždeň<br>4. 3. - 10. 3.  |                   Monte Carlo metódy                  |       Metódy [policy](labs/lab04a-policy-iteration.ipynb) a [value iteration](labs/lab04b-value-iteration.ipynb)      |                                |
|  5. týždeň<br>11. 3. - 17. 3. |				        TD-metódy  		    			|             [Monte Carlo metódy](labs/lab05-monte-carlo.ipynb)             |                                |
|  6. týždeň<br>18. 3. - 24. 3. |            Aproximácia hodnotových funkcií            |             [Q-Learning a SARSA](labs/lab06-q-learning-and-sarsa.ipynb)             |                                |
|  7. týždeň<br>25. 3. - 31. 3. |                       Veľká Noc                       |                 Veľká Noc                  |                                |
|  8. týždeň<br>1. 4. - 7. 4.   |       Deep RL - Aproximácia hodnotových funkcií       |             [Aproximačné metódy](labs/lab07-discretization-approximation.ipynb)             | Z1 odovzdanie                  |
|  9. týždeň<br>8. 4. - 14. 4.  |                  Aproximácia politiky                 |           [Q-siete, Deep Q-Network](labs/lab08-q-networks.ipynb)          |                                |
| 10. týždeň<br>15. 4. - 21. 4. |                     Medzi TD a MC                     |      [Actor-critic architektúry](labs/lab09-actor-critic.ipynb)    | Z2 odovzdanie                  |

[Ďalšie informácie k prednáškam sú dostupné na tejto stránke.](https://marian.mach.website.tuke.sk/course-mlII-en.html)

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov zo zápočtu a zo skúšky.

Zápočet sa skladá z dvoch zadaní, prvé za 10, druhé za 20 bodov, z piatich domácich úloh a jednej zápočtovej písomky. Zadanie 1 sa odovzdáva do konca ôsmeho týždňa a Zadanie 2 sa preberá v desiatom týždni.

|                  Zložka                 | Body |
|:---------------------------------------:|:----:|
| Domáce úlohy							  |   5  |
| Zápočtová písomka						  |   5  |
| [zadanie 1](assignments/assignment1.md) |  10  |
| [zadanie 2](assignments/assignment2.md) |  20  |
| skúška                                  |  60  |

## Odporúčaná literatúra <a name="textbooks"></a>
* SUTTON, R. S. - Barto A. G.: [*Reinforcement Learning: An Introduction*](http://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf). MIT press, 2018.
* MORALES M.: [*Grokking Deep Reinforcement Learning*](https://www.amazon.com/Grokking-Reinforcement-Learning-Miguel-Morales/dp/1617295450). Manning Publications, 2020.
