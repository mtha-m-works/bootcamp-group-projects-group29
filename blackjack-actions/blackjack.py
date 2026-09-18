import random

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
    # flag is where the decision timing will be displayed
    # split into the plays hand,the dealers face-up card and the flag at the end
    hand_str, dealer_upcard, flag = [part.strip() for part in text.split("|")]
    # validates the flag to return first or later
    if flag not in('first','later'):
        raise NotImplemented(f'Invalid flag: {flag!r} (expected "first" or "later")')
    
    #parse takes the results and returns it in the format asked for in the test document
    hand = [rank.strip() for rank in hand_str.split(",")]

    # brings back the results as a dictionary
    return {
        'hand': hand_value,
        'hand_value': hand_value(hand),
        'dealer_upcard': dealer_upcard,
        'flag': flag
    }


def generate_actions(state):
    hand = state['hand']

    # if your hand is greater than 21 is busted, so your turn is over
    if state['hand_value'] > 21:
        return[]
    
    actions = ['hit', 'stand'] #these moves are always allowed(legal)

    #sorting out surrendering,insurance and split
    is_first_decision = state['flag'] == 'first'

    raise NotImplementedError("This function is not implemented yet.")
    if is_first_decision:
        actions.append("double")     # only allowed on your original two cards
        actions.append("surrender")  # only allowed before you've taken any other action

        # Restricting split options by checking if the hand has exactly two cards.
        if len(hand) == 2 and hand[0] == hand[1]:
            actions.append("split")


def apply_action(state, action, next_card=None):
    raise NotImplementedError("This function is not implemented yet.")
