def calculate_risk_score(time_horizon_years: int, goal: str, loss_reaction: str) -> int:
    if time_horizon_years < 3:
        horizon_points = 0
    elif time_horizon_years <= 7:
        horizon_points = 1
    elif time_horizon_years <= 15:
        horizon_points = 2
    else:
        horizon_points = 3

    if goal == "income":
        goal_points = 0
    elif goal == "house":
        goal_points = 1
    elif goal == "general_growth":
        goal_points = 2
    elif goal == "retirement":
        goal_points = 3
    else:
        raise ValueError(f"Unknown goal: {goal!r}")


    if loss_reaction == "sell_all":
        loss_points = 0
    elif loss_reaction == "sell_some":
        loss_points = 1
    elif loss_reaction == "hold":
        loss_points = 2
    elif loss_reaction == "buy_more":
        loss_points = 3
    else:
        raise ValueError(f"Unknown loss: {loss_reaction!r}")
    
    return horizon_points + goal_points + loss_points


def categorize_risk(score: int) -> dict:
    if score < 0 or score > 9:
        raise ValueError(f"Score must be between 0 and 9, got {score}")

    if score <= 3:
        return {
            "category": "Conservative",
            "reasoning": (
                "Your answers suggest you'd rather protect what you have than chase higher returns. "
                "A conservative approach favors steadier investments, even if it means slower growth."
            ),
        }
    elif score <= 6:
        return {
            "category": "Moderate",
            "reasoning": (
                "Your answers suggest you're comfortable with some ups and downs in exchange for "
                "better long-term growth, while still limiting how much you could lose at once."
            ),
        }
    else:
        return {
            "category": "Aggressive",
            "reasoning": (
                "Your answers suggest you have the time and temperament to ride out significant "
                "market swings in pursuit of the highest long-term growth potential."
            ),
        }

