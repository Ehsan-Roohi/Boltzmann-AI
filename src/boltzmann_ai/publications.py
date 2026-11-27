"""Bibliographic records for the first two studies in the collection."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Publication:
    title: str
    author: str
    citation: str
    url: str
    preprint_url: str


PUBLICATIONS = (
    Publication(
        title=(
            "Physics-informed neural networks for strong normal shocks in kinetic "
            "relaxation models and the hard-sphere Boltzmann equation"
        ),
        author="Ehsan Roohi",
        citation="arXiv:2611.31996 (2026), preprint",
        url="https://arxiv.org/abs/2611.31996",
        preprint_url="https://arxiv.org/abs/2611.31996",
    ),
    Publication(
        title=(
            "Accelerating kinetic Fokker-Planck simulations via a GPU-native deep neural "
            "network surrogate: Application to rarefied internal and hypersonic external flows"
        ),
        author="Ehsan Roohi",
        citation="Journal of Computational Physics 566 (2026), 115261",
        url="https://doi.org/10.1016/j.jcp.2026.115261",
        preprint_url="https://arxiv.org/abs/2606.15622",
    ),
)
