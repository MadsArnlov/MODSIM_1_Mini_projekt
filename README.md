# MODSIM_1_Mini_projekt
Lufthavns-kø-problem

Ved anvendelse af program vær opmærksom på:

Ved mange simulationer kan der opstå overflow problemer da der summeres over mange beregninger.
Hold gerne mængden af simulationer under 100 når der simuleres for mere end 15 år.

Programmet kan køres fra kommandolinjen såfremt at indlæsningsfilerne:

* `interarrival.dat`
* `duration.dat`

er i samme mappe som `airport.py` filen.

Køres programmet uden argumenter i kommandolinjen returneres en beskrivelse for anvendelsen af programmet.

OBS: Hvis programmet køres flere gange med samme argumenter, overskrives det forrige plot hver gang. Hvis et bestemt plot skal gemmes,
	er det derfor vigtigt at flytte denne fil ud af mappen.
