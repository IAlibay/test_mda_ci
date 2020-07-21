"""
Unit and regression test for the MDRestraintsGenerator package.
"""

# Import package, test suite, and other packages as needed
import MDAnalysis as mda
from MDAnalysisTests.datafiles import PSF, DCD, TPR, TRR, GRO, XTC
from MDAnalysis.analysis import rms, align
from numpy.testing import assert_almost_equal
import warnings
import pytest


#@pytest.mark.parametrize('run', [
#    1, 2
#])
#def test_rmsf_psf(run):
#    """Align multiple times + RMSF"""
#
#    u = mda.Universe(PSF, DCD)
#
#    average = align.AverageStructure(u, u, select='protein and name CA',
#                                     ref_frame=0).run()
#
#    ref = average.universe
#
#    aligner = align.AlignTraj(u, ref,
#                              select='protein and name CA',
#                              in_memory=True).run()
#
#    c_alphas = u.select_atoms('protein and name CA')
#    R = rms.RMSF(c_alphas).run()
#
#    assert 1 == 1


#@pytest.mark.parametrize('run', [
#    1, 2
#])
#def test_rmsf_nc(run):
#    """Align multiple times + RMSF"""
#
#    u = mda.Universe(PSF, DCD)
#
#    u2 = u.copy()
#
#    average = align.AverageStructure(u2, u2, select='protein and name CA',
#                                     ref_frame=0).run()
#
#    ref = average.universe
#
#    aligner = align.AlignTraj(u2, ref,
#                              select='protein and name CA',
#                              in_memory=True).run()
#
#    c_alphas = u2.select_atoms('protein and name CA')
#    R = rms.RMSF(c_alphas).run()
#
#    assert 1 == 1
#
#
#@pytest.mark.parametrize('run', [
#    1, 2
#])
#def test_rmsf_xtc(run):
def test_rmsf_xtc():
    """Align multiple times + RMSF"""

    u = mda.Universe(TPR, XTC)

    u2 = u.copy()

    average = align.AverageStructure(u2, u2, select='protein and name CA',
                                     ref_frame=0).run()

    ref = average.universe

    aligner = align.AlignTraj(u2, ref,
                              select='protein and name CA',
                              in_memory=True).run()

    c_alphas = u2.select_atoms('protein and name CA')
    R = rms.RMSF(c_alphas).run()

    assert 1 == 1
