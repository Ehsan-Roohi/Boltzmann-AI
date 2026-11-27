"""Command-line access to the equilibrium benchmark and research catalog."""

import argparse
import csv
import sys
from math import isfinite

from . import maxwellian_1d
from .publications import PUBLICATIONS


def finite_velocity(value: str) -> float:
    velocity = float(value)
    if not isfinite(velocity):
        raise argparse.ArgumentTypeError("velocity must be finite")
    return velocity


def main() -> None:
    parser = argparse.ArgumentParser(prog="boltzmann-ai")
    commands = parser.add_subparsers(dest="command", required=True)
    profile = commands.add_parser("maxwellian", help="Print the 1-D equilibrium profile as CSV")
    profile.add_argument(
        "velocities", type=finite_velocity, nargs="+", metavar="c",
        help="Dimensionless molecular velocity component relative to the bulk flow",
    )
    commands.add_parser("publications", help="Print citations and access links")
    args = parser.parse_args()
    if args.command == "maxwellian":
        writer = csv.writer(sys.stdout, lineterminator="\n")
        writer.writerow(("c", "probability_density"))
        for velocity in args.velocities:
            writer.writerow((velocity, maxwellian_1d(velocity)))
    else:
        for paper in PUBLICATIONS:
            print(f"{paper.author}. {paper.title}. {paper.citation}.")
            print(paper.url)
            if paper.preprint_url != paper.url:
                print(paper.preprint_url)


if __name__ == "__main__":
    main()
