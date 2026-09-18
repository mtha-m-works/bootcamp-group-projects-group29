RANK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11,
}


def hand_value(cards):
    total = sum(RANK_VALUES[card] for card in cards)
    aces = cards.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def parse_state(text):
    hand_str, dealer_upcard, flag = [part.strip() for part in text.split("|")]
    hand = [rank.strip() for rank in hand_str.split(",")]

    return ...


def generate_actions(state):
    raise NotImplementedError("This function is not implemented yet.")
if is_first_decision:
        actions.append("double")     # only allowed on your original two cards
        actions.append("surrender")  # only allowed before you've taken any other action

        # Restricting split options by checking if the hand has exactly two cards.
        if len(hand) == 2 and hand[0] == hand[1]:
            actions.append("split")


def apply_action(state, action, next_card=None):
    raise NotImplementedError("This function is not implemented yet.")
