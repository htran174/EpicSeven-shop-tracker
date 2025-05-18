# backend.py

def calculate_roi(start, end, regular, mystic):
    spent = start - end
    regular_roi = spent / regular if regular > 0 else "N/A"
    mystic_roi = spent / mystic if mystic > 0 else "N/A"

    result_text = (
        f"Skystone Spent: {spent}\n\n"
        f"Regular Pulls: {regular}\n"
        f"Regular ROI (Skystone per Pull): {regular_roi if regular_roi == 'N/A' else f'{regular_roi:.2f}'}\n\n"
        f"Mystic Pulls: {mystic}\n"
        f"Mystic ROI (Skystone per Pull): {mystic_roi if mystic_roi == 'N/A' else f'{mystic_roi:.2f}'}"
    )
    return result_text


def check_luck(start, end, regular, mystic):
    spent = start - end
    regular_msg = get_luck_message(regular, spent, 70, "Regular")
    mystic_msg = get_luck_message(mystic, spent, 270, "Mystic")

    full_message = f"📊 Regular Pulls:\n{regular_msg}\n\n🔮 Mystic Pulls:\n{mystic_msg}"
    return full_message


def get_luck_message(pulls, spent, avg_cost, pull_type):
    if pulls == 0:
        ratio = spent / avg_cost
        if ratio < 0.5:
            return (
                f"You haven’t spent enough for a single {pull_type} pull yet.\n"
                f"Average cost is {avg_cost} Skystones.\n"
                f"Too early to tell 🎲"
            )
        elif ratio < 1.0:
            return (
                f"You’ve spent {spent} Skystones on {pull_type} pulls, but haven’t gotten one yet.\n"
                f"Average cost is {avg_cost} Skystones.\n"
                f"A bit unlucky 😕"
            )
        elif ratio < 2.0:
            return (
                f"You’ve spent {spent} Skystones on {pull_type} pulls, but haven’t gotten one yet.\n"
                f"Average cost is {avg_cost} Skystones.\n"
                f"Unlucky... 😢"
            )
        else:
            return (
                f"You’ve spent {spent} Skystones on {pull_type} pulls, but haven’t gotten one yet.\n"
                f"Average cost is {avg_cost} Skystones.\n"
                f"SUPER Unlucky... 💀"
            )
    else:
        avg = spent / pulls
        diff = avg - avg_cost
        abs_diff = abs(diff)

        # Thresholds scale with avg_cost
        t_bit = (6 / 70) * avg_cost
        t_lucky = (12 / 70) * avg_cost
        t_super = (30 / 70) * avg_cost

        if abs_diff <= t_bit:
            tier = "About average"
            emoji = "⚖️"
        elif abs_diff <= t_lucky:
            tier = "A bit lucky" if diff < 0 else "A bit unlucky"
            emoji = "🙂" if diff < 0 else "😕"
        elif abs_diff <= t_super:
            tier = "Lucky!" if diff < 0 else "Unlucky..."
            emoji = "🎉" if diff < 0 else "😢"
        else:
            tier = "SUPER Lucky!!" if diff < 0 else "SUPER Unlucky... 💀"
            emoji = "🍀" if diff < 0 else "💸"

        return (
            f"You’ve got {pulls} {pull_type} pulls.\n"
            f"Your average cost per pull is {avg:.2f} Skystones.\n"
            f"{tier} {emoji}\n"
            f"Average ROI for {pull_type} pulls is {avg_cost:.2f} Skystones per pull"
        )