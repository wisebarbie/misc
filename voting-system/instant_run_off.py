from single_winner import *


def votes_needed_to_win(ballots, num_winners):
    # note total votes as number of elements in the list ballots
    total_votes = len(ballots)
    # calculate droop quota as suggested and round down
    output = int(total_votes/(num_winners+1)+1)
    return output


def has_votes_needed(result, votes_needed):
    '''
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True
    '''
    # accept if max of vote counts is greater than votes needed
    if len(result.values()) != 0:
        if max(result.values()) >= votes_needed:
            return True
    return False
    

def eliminate_candidate(ballots, to_eliminate):
    '''
    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    '''
    output = []
    for ballot in ballots:
        new_ballot = []
        for candidate in ballot:
            # only account for candidates that should not be eliminated
            if candidate not in to_eliminate:
                new_ballot.append(candidate)
        # append changed ballot into new list of ballots
        output.append(new_ballot)
    return output


def count_irv(ballots):
    '''
    >>> count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'], ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP']])
    {'BLOC': 0, 'CPC': 0, 'GREEN': 0, 'LIBERAL': 3, 'NDP': 5}
    '''
    first_choice_votes = count_first_choices(ballots)
    needed_votes = votes_needed_to_win(ballots, 1)
    other_ballots = {}
    new_ballots = ballots
    while not has_votes_needed(first_choice_votes, needed_votes):
        loser = last_place(first_choice_votes)
        other_ballots[loser] = 0
        new_ballots = eliminate_candidate(new_ballots, other_ballots.keys())
        first_choice_votes = count_first_choices(new_ballots)
    product = {}
    for sorted_key in sorted(add_dicts(other_ballots, first_choice_votes)):
        product[sorted_key] = add_dicts(other_ballots, first_choice_votes)[sorted_key]
    return product
    
    
if __name__ == '__main__':
    doctest.testmod()
