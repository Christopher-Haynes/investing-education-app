import pytest
from core.scoring import calculate_risk_score, categorize_risk


def test_conservative_profile_scores_low():
    score = calculate_risk_score(time_horizon_years=2, goal="income", loss_reaction="sell_all")
    assert score == 0


def test_invalid_goal_raises_error():
    with pytest.raises(ValueError):
        calculate_risk_score(time_horizon_years=10, goal="not_a_real_goal", loss_reaction="hold")


def test_aggressive_profile_scores_high():
    score = calculate_risk_score(time_horizon_years=20, goal="retirement", loss_reaction="buy_more")
    assert score == 9


def test_score_three_is_conservative():
    result = categorize_risk(3)
    assert result["category"] == "Conservative"


def test_score_four_is_moderate():
    result = categorize_risk(4)
    assert result["category"] == "Moderate"


def test_score_six_is_moderate():
    result = categorize_risk(6)
    assert result["category"] == "Moderate"


def test_score_seven_is_aggressive():
    result = categorize_risk(7)
    assert result["category"] == "Aggressive"


def test_invalid_score_raises_error():
    with pytest.raises(ValueError):
        categorize_risk(10)
