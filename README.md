# Mini convertisseur d'unités

Un petit outil Python pour convertir des longueurs, des masses et des températures.
Il fonctionne en ligne de commande, sans dépendance externe et sans connexion réseau.

## Utilisation

Python 3.9 ou plus récent suffit.

```bash
python3 convert.py 2.5 km m
# 2500 m

python3 convert.py 750 g kg
# 0.75 kg

python3 convert.py 25 c f
# 77 f

python3 convert.py 273.15 k c
# 0 c
```

La virgule décimale est également acceptée : `python3 convert.py 2,5 km m`.

## Unités disponibles

| Grandeur | Unités |
| --- | --- |
| Longueur | `mm`, `cm`, `m`, `km` |
| Masse | `mg`, `g`, `kg` |
| Température | `c` (Celsius), `f` (Fahrenheit), `k` (kelvin) |

Les conversions entre des grandeurs différentes et les températures inférieures
au zéro absolu sont refusées. Le calcul utilise les nombres flottants de Python ;
cet outil est destiné aux conversions courantes.

Pour afficher l'aide :

```bash
python3 convert.py --help
```
