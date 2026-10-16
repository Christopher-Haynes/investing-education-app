import pytest
from core.scoring import calculate_risk_score


def test_conservative_profile_scores_low():
    score = calculate_risk_score(time_horizon_years=2, goal="income", loss_reaction="sell_all")
    assert score == 0


def test_invalid_goal_raises_error():
    with pytest.raises(ValueError):
        calculate_risk_score(time_horizon_years=10, goal="not_a_real_goal", loss_reaction="hold")


def test_aggressive_profile_scores_high():
    score = calculate_risk_score(time_horizon_years=20, goal="retirement", loss_reaction="buy_more")
    assert score == 9
