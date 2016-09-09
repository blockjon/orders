import os
import operator
from itertools import combinations
from collections import defaultdict

"""
Runtime complexity: O(n)
Space complexity: O(n + log n)
"""


if __name__ == "__main__":

    input_file = os.path.dirname(
        os.path.realpath(__file__)
    ) + '/orders.txt'

    # Build a map linking each customer to all drugs ever purchased.
    customer_drug_map = defaultdict(lambda: set([]))
    with open(input_file) as f:
        for line in f:
            parts = line.strip().split(": ")
            customer_id = parts[0]
            drugs = parts[1].split(", ")
            for drug in drugs:
                customer_drug_map[customer_id].add(drug)

    # Count up the times drugs were paired together.
    pairings = defaultdict(int)
    for customer, drugs in customer_drug_map.iteritems():
        if len(drugs) <= 1:
            continue
        for pairing_combination in combinations(drugs, 2):
            pairings[pairing_combination] += 1

    # Sort desc
    sorted = sorted(pairings.items(), key=operator.itemgetter(1))
    sorted_desc = sorted.reverse()

    # Output to stdout
    for drug_combination, num_times_ordered_together in sorted[:2]:
        print ", ".join(drug_combination)
