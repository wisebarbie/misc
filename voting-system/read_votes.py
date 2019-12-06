from proportional_representation import *


SHORTHANDS = {'G':'GREEN', 'N':'NDP', 'L':'LIBERAL', 'C':'CPC', 'B':'BLOC',
              'P':'PPC', 'I':'IND'}


def process_to_string(raw):
    '''(str) -> str
    Unpack the short hand used in votes.txt.
    >>> process_to_string('N')
    'NDP'
    '''
    return SHORTHANDS[raw]


def process_to_list(raw):
    '''(str) -> lst
    Turn a raw list to an actual list.
    >>> process_to_list('NLG')
    ['NDP', 'LIBERAL', 'GREEN']
    '''
    l = []
    for c in raw:
        l.append( SHORTHANDS[c] )
    return l


def process_to_dict(raw):
    '''(str) -> dict
    Turn a raw rated ballot into a nice dictionary.
    >>> process_to_dict('N4G5L4C3P1')
    {'NDP': 4, 'GREEN': 5, 'LIBERAL': 4, 'CPC': 3, 'PPC': 1}
    '''
    d = {}
    for i, c in enumerate(raw):
        if i % 2 == 0:
            d[SHORTHANDS[c]] = int(raw[i+1])    
    return d


def read_votes(fname):
    '''(str) -> dict
    Read in a file of voters and all their possible ballots.
    Provided to students. Do not edit.
    '''
    electorate = {}
    with open(fname, 'r') as f:
        for line in f:
            info = line.strip().split(' ')
            riding = int(info[1])
            stv_riding = int(info[2])
            voter_id = int(info[0])
            pref = float(info[3])
            q_pref = float(info[4])
            plurality_ballot = process_to_string(info[5])
            approval_ballot = process_to_list(info[6])
            rated_ballot = process_to_dict(info[7])
            ranked_ballot = process_to_list(info[8])
            
            electorate[voter_id] = [riding, stv_riding, pref, q_pref, plurality_ballot, 
                                    approval_ballot, rated_ballot, ranked_ballot]

    return electorate


def votes_for_riding(electorate, riding_id, ballot_type):
    '''(dict, int, func) -> list
    Given riding_id and ballot type (represented by its associated counting
    function, e.g. count_plurality for plurality ballots),
    return all of those votes for the riding.

    Provided to students. Do not edit this function.

    >>> electorate = read_votes('votes.txt')
    >>> votes_for_riding(electorate, 62001, count_plurality)
    ['CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'CPC', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'NDP', 'GREEN', 'GREEN']
    >>> votes_for_riding(electorate, 10001, count_approval)
    [['CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['CPC', 'PPC'], ['CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['CPC', 'PPC'], ['LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['LIBERAL', 'CPC', 'PPC'], ['NDP', 'GREEN', 'LIBERAL'], ['GREEN', 'LIBERAL', 'CPC'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN', 'LIBERAL'], ['GREEN', 'LIBERAL', 'CPC'], ['LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['NDP', 'GREEN', 'LIBERAL'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN', 'LIBERAL'], ['LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['LIBERAL', 'CPC', 'PPC'], ['NDP', 'GREEN', 'LIBERAL'], ['GREEN', 'LIBERAL', 'CPC'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN', 'LIBERAL'], ['LIBERAL', 'CPC', 'PPC'], ['NDP', 'GREEN', 'LIBERAL'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['NDP', 'GREEN', 'LIBERAL'], ['GREEN', 'LIBERAL', 'CPC'], ['LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['NDP', 'GREEN', 'LIBERAL'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC', 'PPC'], ['GREEN', 'LIBERAL', 'CPC'], ['GREEN', 'LIBERAL', 'CPC'], ['LIBERAL', 'CPC', 'PPC'], ['NDP', 'GREEN'], ['NDP'], ['NDP'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN'], ['NDP', 'GREEN'], ['NDP', 'GREEN'], ['NDP', 'GREEN'], ['NDP'], ['NDP'], ['NDP'], ['NDP', 'GREEN', 'LIBERAL'], ['NDP', 'GREEN'], ['NDP', 'GREEN']]
    '''
    ballot_types = {count_plurality:-4, count_approval:-3, count_rated:-2, count_irv:-1,
                    count_SL:-4, count_stv:-1}
    ballots = []

    for voter in electorate:
        info = electorate[voter]
        if info[0] == riding_id or riding_id == 0 or info[1] == riding_id:
            index = ballot_types[ballot_type]
            ballots.append( info[index] )
    return ballots


def get_ridings(electorate, counting_function):
    '''(dict, function) -> dict
    Return the unique set of riding ids in the electorate, given the system.

    Provided to students. Do not edit.

    >>> electorate = read_votes('votes.txt')
    >>> all_ridings = get_ridings(electorate, count_plurality)
    >>> len(all_ridings)
    338
    >>> all_ridings = get_ridings(electorate, count_SL)
    >>> all_ridings
    {0: 338}
    >>> all_ridings = get_ridings(electorate, count_stv)
    >>> len(all_ridings)
    30
    '''
    ridings = {}
    seen = []
    for voter in electorate:
        info = electorate[voter]
        if counting_function in [count_plurality, count_approval, count_irv, count_rated]:
            ridings[ info[0] ] = 1 # 1 MP for the riding in these systems. Not a typo.
        if counting_function == count_stv:
            if info[0] not in seen:
                if info[1] not in ridings:
                    ridings[ info[1] ] = 0
                ridings[ info[1] ] += 1
                seen.append(info[0])
        if counting_function == count_SL:
            if info[0] not in seen:
                if 0 not in ridings:
                    ridings[0] = 1
                else:
                    ridings[ 0 ] += 1
                seen.append(info[0])

    return ridings


if __name__ == '__main__':
    doctest.testmod()
