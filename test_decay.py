"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    # Check that calling simulate with a negative lam raises a ValueError
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    # Check that the simulation is close to the physical law N0 * exp(-lam * t)
    N0 = 1000
    lam = 0.3
    t = 2.0
    expected = N0 * np.exp(-lam * t)
    
    # Run multiple simulations and check the average value
    runs = [simulate(N0, lam, t_max=t)[-1] for _ in range(50)]
    avg_result = np.mean(runs)
    
    assert avg_result == pytest.approx(expected, rel=0.05)