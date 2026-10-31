"""Petit convertisseur d'unités utilisable en ligne de commande."""

import argparse
import math


# Dimension, multiplicateur et décalage vers l'unité de référence.
UNITS = {
    "mm": ("longueur", 0.001, 0),
    "cm": ("longueur", 0.01, 0),
    "m": ("longueur", 1, 0),
    "km": ("longueur", 1000, 0),
    "mg": ("masse", 0.000001, 0),
    "g": ("masse", 0.001, 0),
    "kg": ("masse", 1, 0),
    "c": ("température", 1, 273.15),
    "f": ("température", 5 / 9, 273.15 - 32 * 5 / 9),
    "k": ("température", 1, 0),
}


def convert(value, source, target):
    """Convertit une valeur entre deux unités de même dimension."""
    source_kind, source_scale, source_offset = UNITS[source]
    target_kind, target_scale, target_offset = UNITS[target]
    if source_kind != target_kind:
        raise ValueError("Choisis deux unités de même dimension.")
    if not math.isfinite(value):
        raise ValueError("La valeur doit être un nombre fini.")
    reference = value * source_scale + source_offset
    if source_kind == "température" and reference < 0:
        raise ValueError("La température est inférieure au zéro absolu.")
    result = (reference - target_offset) / target_scale
    if not math.isfinite(result):
        raise ValueError("Le résultat dépasse la capacité numérique.")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("value", help="Valeur numérique, par exemple 2.5")
    parser.add_argument("source", choices=UNITS, help="Unité de départ")
    parser.add_argument("target", choices=UNITS, help="Unité d'arrivée")
    args = parser.parse_args()
    try:
        value = float(args.value.replace(",", "."))
        result = convert(value, args.source, args.target)
    except ValueError as error:
        parser.error(str(error))
    print(f"{result:.10g} {args.target}")


if __name__ == "__main__":
    main()
