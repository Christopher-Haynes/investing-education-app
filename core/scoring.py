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

