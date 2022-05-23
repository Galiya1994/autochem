""" AMChI (AutoMech Chemical Identifier) strings

Closely follows the InChI format, although canonicalizations may differ.
Extends InChI to allow for resonance double-bond stereo.
"""

# L2
# # constructor
from automol.amchi.base._core import from_data
# # recalculate/standardize
from automol.amchi.base._core import standard_form
# # getters
from automol.amchi.base._core import prefix
from automol.amchi.base._core import version
from automol.amchi.base._core import formula_string
from automol.amchi.base._core import main_layers
from automol.amchi.base._core import charge_layers
from automol.amchi.base._core import stereo_layers
from automol.amchi.base._core import isotope_layers
# # setters
from automol.amchi.base._core import reflect
from automol.amchi.base._core import with_inchi_prefix
# # conversions
from automol.amchi.base._core import formula
from automol.amchi.base._core import connectivity
from automol.amchi.base._core import without_stereo
from automol.amchi.base._core import are_enantiomers
from automol.amchi.base._core import are_diastereomers
# # properties
# # # formula layer
from automol.amchi.base._core import symbols
from automol.amchi.base._core import canonical_indices
# # # main layers
from automol.amchi.base._core import bonds
from automol.amchi.base._core import hydrogen_valences
# # # charge layers
from automol.amchi.base._core import charge
# # # stereo layers
from automol.amchi.base._core import bond_stereo_parities
from automol.amchi.base._core import atom_stereo_parities
from automol.amchi.base._core import is_inverted_enantiomer
# # # isotope layers
from automol.amchi.base._core import bond_isotope_stereo_parities
from automol.amchi.base._core import atom_isotope_stereo_parities
from automol.amchi.base._core import is_inverted_isotope_enantiomer
# # other properties
from automol.amchi.base._core import has_multiple_components
from automol.amchi.base._core import has_stereo
from automol.amchi.base._core import has_mobile_hydrogens
from automol.amchi.base._core import low_spin_multiplicity
from automol.amchi.base._core import is_chiral
# # comparisons
from automol.amchi.base._core import same_connectivity
from automol.amchi.base._core import equivalent
# # split/join
from automol.amchi.base._core import split
from automol.amchi.base._core import join
# # sort
from automol.amchi.base._core import sorted_
from automol.amchi.base._core import argsort
# # helpers
from automol.amchi.base._core import version_pattern
# reaction functions
from automol.amchi.base._reac import filter_enantiomer_reactions
from automol.amchi.base._reac import sort_reactions
# L4
# # conversions
from automol.amchi._conv import amchi_key
from automol.amchi._conv import smiles
from automol.amchi._conv import graph
from automol.amchi._conv import geometry
from automol.amchi._conv import conformers
# # derived properties
from automol.amchi._conv import is_complete
# # derived transformations
from automol.amchi._conv import add_stereo
from automol.amchi._conv import expand_stereo
# drawing tools
from automol.amchi._draw import draw
from automol.amchi._draw import draw_grid
# assessment tools
from automol.amchi._assess import is_valid_multiplicity


__all__ = [
    # L2
    # # constructor
    'from_data',
    # # recalculate/standardize
    'standard_form',
    # # getters
    'prefix',
    'version',
    'formula_string',
    'main_layers',
    'charge_layers',
    'stereo_layers',
    'isotope_layers',
    # # setters
    'reflect',
    'with_inchi_prefix',
    # # conversions
    'formula',
    'connectivity',
    'without_stereo',
    'are_enantiomers',
    'are_diastereomers',
    # # properties
    # # # formula layer
    'symbols',
    'canonical_indices',
    # # # main layers
    'bonds',
    'hydrogen_valences',
    # # # charge layers
    'charge',
    # # # stereo layers
    'bond_stereo_parities',
    'atom_stereo_parities',
    'is_inverted_enantiomer',
    # # # isotope layers
    'bond_isotope_stereo_parities',
    'atom_isotope_stereo_parities',
    'is_inverted_isotope_enantiomer',
    # # other properties
    'has_multiple_components',
    'has_stereo',
    'has_mobile_hydrogens',
    'low_spin_multiplicity',
    'is_chiral',
    # # comparisons
    'same_connectivity',
    'equivalent',
    # # split/join
    'split',
    'join',
    # # sort
    'sorted_',
    'argsort',
    # # helpers
    'version_pattern',
    # reaction functions
    'filter_enantiomer_reactions',
    'sort_reactions',
    # L4
    # # conversions
    'amchi_key',
    'smiles',
    'graph',
    'geometry',
    'conformers',
    # # derived properties
    'is_complete',
    # # derived transformations
    'add_stereo',
    'expand_stereo',
    # drawing tools
    'draw',
    'draw_grid',
    # assessment tools
    'is_valid_multiplicity',
]
