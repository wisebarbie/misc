# COMP 202 A3
NAME = 'SHAISTA'

################################### Do not edit anything below this ############

from read_votes import *
import matplotlib.pyplot as plt
import numpy as np


################################################################################

def outcome(seats):
    '''(dict) -> str
    Given a dictionary of seat results, return outcome.
    Provided to students. Do not edit.

    >>> outcome({'BLOC': 32, 'CPC': 157, 'GREEN': 3, 'IND': 1, 'LIBERAL': 121, 'NDP': 24})
    'CPC Minority'
    >>> outcome({'LIBERAL': 195, 'GREEN': 14, 'CPC': 103, 'BLOC': 11, 'NDP': 14, 'PPC': 1})
    'LIBERAL Majority'
    >>> outcome({'LIBERAL': 1951, 'GREEN': 141, 'CPC': 1031, 'BLOC': 111, 'NDP': 141, 'PPC': 11})
    'LIBERAL Majority'
    '''
    winner = get_winner(seats)
    s = sum(seats.values()) / 2
    has_majority = has_votes_needed(seats, s)
    if has_majority:
        winner += ' Majority'
    else:
        winner += ' Minority'
    return winner


################################################################################


def get_popular_vote(electorate):
    '''(dict) -> dict
    >>> electorate = read_votes('votes.txt')
    >>> get_popular_vote(electorate)
    {'CPC': 11481, 'GREEN': 2185, 'LIBERAL': 11324, 'NDP': 5504, 'IND': 184, 'PPC': 539, 'BLOC': 2505}
    >>> outcome(get_popular_vote(electorate))
    'CPC Minority'
    '''
    total = {}
    counting_function = count_plurality
    all_ridings = get_ridings(electorate, counting_function)
    
    for riding_id in all_ridings:
        ballots = votes_for_riding(electorate, riding_id, counting_function)

        results = counting_function(ballots)

        total = add_dicts(total, results)

    return total


def single_winner_HOC(electorate, counting_function):
    '''(dict, function) -> dict
    Given an electorate dictionary and single-winner voting system function,
    elect a simulated House of Commons.

    >>> electorate = read_votes('votes.txt')
    >>> single_winner_HOC(electorate, count_plurality)
    {'LIBERAL': 157, 'NDP': 25, 'CPC': 120, 'GREEN': 3, 'BLOC': 32, 'IND': 1}
    >>> outcome(single_winner_HOC(electorate, count_plurality))
    'LIBERAL Minority'
    >>> outcome(single_winner_HOC(electorate, count_approval))
    'CPC Minority'
    >>> outcome(single_winner_HOC(electorate, count_rated))
    'LIBERAL Majority'
    >>> outcome(single_winner_HOC(electorate, count_irv))
    'LIBERAL Majority'
    '''
    seats = {}
    all_ridings = get_ridings(electorate, counting_function)

    for riding_id in all_ridings:
        ballots = votes_for_riding(electorate, riding_id, counting_function)

        results = counting_function(ballots)
        winner = get_winner(results)

        if winner in seats:
            seats[winner] += 1
        else:
            seats[winner] = 1
    
    return seats


################################################################################


def multi_winner_HOC(electorate, counting_function):
    '''(dict, function) -> dict
    Given an electorate dictionary and multi-winner voting system function,
    elect a simulated House of Commons.

    Provided to students. Do not edit.
    '''
    # These doctests can take a while to run and are affected by randomness.
    '''
    >>> electorate = read_votes('votes.txt')
    >>> outcome(multi_winner_HOC(electorate, count_SL))
    'CPC Minority'
    '''
    
    seats = {}
    all_ridings = get_ridings(electorate, counting_function)

    for riding_id in all_ridings:
        ballots = votes_for_riding(electorate, riding_id, counting_function)
        results = counting_function(ballots, all_ridings[riding_id])
        seats = add_dicts(seats, results)
    return seats


def get_seats(electorate, counting_function, multi_winner = False):
    '''(dict, list, funct) -> dict
    Given an electorate directory and a voting system function,
    elect a simulated House of Commons.

    Provided to students. Do not edit.
    '''
    # These doctests can take a while to run and are affected by randomness.
    '''
    >>> electorate = read_votes()
    >>> get_seats(electorate, count_plurality)
    {'LIBERAL': 157, 'NDP': 24, 'CPC': 121, 'GREEN': 3, 'BLOC': 32, 'IND': 1}
    >>> get_seats(electorate, count_approval)
    {'LIBERAL': 115, 'CPC': 140, 'GREEN': 50, 'BLOC': 26, 'NDP': 7}
    >>> get_seats(electorate, count_irv)
    {'LIBERAL': 195, 'GREEN': 14, 'CPC': 103, 'BLOC': 11, 'NDP': 14, 'PPC': 1}
    >>> get_seats(electorate, count_rated) 
    {'LIBERAL': 192, 'GREEN': 25, 'CPC': 98, 'BLOC': 19, 'NDP': 4}
    >>> get_seats(electorate, count_SL, True)
    {'CPC': 115, 'GREEN': 22, 'LIBERAL': 114, 'NDP': 55, 'IND': 2, 'PPC': 5, 'BLOC': 25}
    '''
    '''
    This can take a while to run:
    >>> get_seats(electorate, count_stv, True)
    {'CPC': 115, 'GREEN': 22, 'LIBERAL': 114, 'NDP': 55, 'IND': 2, 'PPC': 5, 'BLOC': 25}
    '''
    if multi_winner:
        return multi_winner_HOC(electorate, counting_function)
    else:
        return single_winner_HOC(electorate, counting_function)


################################################################################


def plot_party_results(grid_list, plot_name, show_graph = True):
    '''(lst, str) -> np.array
    Given a matrix in list form, plot it as bar plot.
    Provided to students. Do not edit.

    >>> r = [[5504, 2505, 2185, 11324, 11481, 539, 184], [24, 33, 3, 156, 121, 0, 1], [8, 26, 51, 117, 136, 0, 0], [4, 19, 25, 194, 96, 0, 0], [14, 11, 16, 195, 101, 1, 0], [52, 25, 39, 93, 79, 50, 0], [55, 25, 22, 114, 115, 5, 2]]
    >>> plot_party_results(r, '', False)
    array([[ 55,  25,  22, 114, 115,   5,   2],
           [ 24,  33,   3, 156, 121,   0,   1],
           [  8,  26,  51, 117, 136,   0,   0],
           [  4,  19,  25, 194,  96,   0,   0],
           [ 14,  11,  16, 195, 101,   1,   0],
           [ 52,  25,  39,  93,  79,  50,   0],
           [ 55,  25,  22, 114, 115,   5,   2]])
    '''

    seats = np.array(grid_list)

    colours = ('#ff6600', '#00e5ee', '#006400', '#ff0000', '#0000ff', '#800080', '#333333')

    seats = seats.astype('float')

    seats[0,:] = np.around(338* (seats[-1,:] / np.sum(seats[-1,:])))
    seats = seats.astype('int')

    col_ind = np.arange(seats.shape[1])
    row_ind = np.arange(seats.shape[0])
    for i in col_ind:
        plt.bar(row_ind, seats[:, i], color=colours[i], bottom=np.sum(seats[:, :i], axis=1))

    plt.xlabel('Voting System')
    plt.ylabel('Number of Seats')
    plt.title('Seats in Simulated Election (with popular vote for comparison)\nWith Code By: ' + NAME)

    # More things to share
    plt.xticks(row_ind + 0.0, ('PopVote', 'Plurality', 'Approval', 'Score', 'IRV', 'STV', 'SL'))
    if show_graph:
        plt.show()
    if plot_name:
        plt.savefig(plot_name)

    return seats


################################################################################


def simulate():
    print('Simulating elections with different systems!')
    print('This could take 1-5 mins to run.')
    electorate = read_votes('votes.txt')
    
    parties = {'NDP':0, 'BLOC':1, 'GREEN':2, 'LIBERAL':3, 'CPC':4, 'PPC':5, 'IND':6}

    counting_functions = [get_popular_vote,
                          count_plurality, count_approval, count_rated, count_irv,
                          count_stv, count_SL]

    grid = []

    for f in counting_functions:
        print('\tStarted counting with', f.__name__)
        if f == get_popular_vote:
            seats = get_popular_vote(electorate)
        else:
            seats = get_seats(electorate, f, f in [count_stv, count_SL])

        as_list = [0]*len(parties)
        for s in seats:
            as_list[ parties[s] ] = seats[s]
        grid.append(as_list)
        print('\tDone counting with', f.__name__)

    print('Results as list')
    print(grid)

    a = plot_party_results(grid, 'HOC.png', False)
    print('Results as array')
    print(a)
    print('See visualization in HOC.png!')


################################################################################

if __name__ == '__main__':
    # doctest.testmod()

    simulate()  # Could take 1-5 mins to run.
    # Then have a look at HOC.png :)
