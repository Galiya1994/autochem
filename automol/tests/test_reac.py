"""Test automol.reac
"""
import automol
from automol import reac


def test__reactant_graphs():
    """Test reac.reactant_graphs
    """
    def _test(rct_smis, prd_smis):
        rct_gras0 = tuple(map(automol.smiles.graph, rct_smis))
        prd_gras0 = tuple(map(automol.smiles.graph, prd_smis))
        rxns = reac.find(rct_gras0, prd_gras0, stereo=False)
        for rxn in rxns:
            rct_gras1 = reac.reactant_graphs(rxn, shift_keys=False)
            prd_gras1 = reac.product_graphs(rxn, shift_keys=False)
            assert rct_gras1 == rct_gras0
            assert prd_gras1 == prd_gras0

    _test(['FC=CF', '[OH]'], ['F[CH]C(O)F'])
    _test(['C1CCC1', '[CH3]'], ['C', 'C1[CH]CC1'])


if __name__ == "__main__":
    test__reactant_graphs()
