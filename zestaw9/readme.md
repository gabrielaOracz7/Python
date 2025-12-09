# Zestaw 9 - Pygame

### Zadanie 9.1
Zaimplementować prostą **grę o topieniu padającego śniegu**. Przy górnej krawędzi ekranu pojawiają się losowo płatki śniegu, które spadają w dół ruchem jednostajnym. Zadaniem gracza jest topienie płatków śniegu przez klikanie na nie myszą. Celem gry jest niedopuszczenie, aby jakiś płatek śniegu dotarł do dolnej krawędzi ekranu.


Można rozważyć wariant gry, w którym tworzą się zaspy śniegu, a gra kończy się, gdy zaspa urośnie do górnej krawędzi ekranu. 

---

#### Przyjęte zasady gry

Zgodnie z tym, co zapisano powyżej, gra polega na topieniu spadających płatków śniegu poprzez klikanie na nie myszą. Gracz zdobywa punkt za każdy stopiony (kliknięty) płatek. Jeżeli nie zdąży on stopić płatka, to ten  opada, gdzie zaczyna tworzyć zaspę śnieżną.

W grze wprowadzono również **mechanizm przyspieszenia**: im więcej punktów zdobywa gracz, tym szybciej spadają kolejne płatki śniegu. Co każde zdobyte `10` punktów prędkość spadania rośnie o `0.3`.

Gra kończy się gdy:
- zaspa z niestopionych płatków urośnie do górnej krawędzi ekranu,
- gracz wciśnie klawisz `q` lub `ESC`.

Po zakończeniu rozgrywki na ekranie zostaje wyświetlony komunikat z informacją o liczbie zdobytych punktów.