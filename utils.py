from collections import defaultdict


def compute_balances(roommates, expenses, payer_index=0):
    """Calculate how much each roommate owes the payer.

    Parameters
    ----------
    roommates : list[str]
        List of roommate names.
    expenses : iterable[Mapping]
        Sequence of expense mappings each having an ``amount`` key.
    payer_index : int, optional
        Index of the roommate who paid, by default 0.

    Returns
    -------
    dict[str, float]
        Mapping of debt descriptions to amounts rounded to 2 decimals.
    """
    if not roommates:
        return {}

    payer = roommates[payer_index]
    debts = defaultdict(float)

    for exp in expenses:
        amount = exp['amount']
        share = amount / len(roommates)
        for rm in roommates:
            if rm != payer:
                debts[f"{rm} owes {payer}"] += share

    return {k: round(v, 2) for k, v in debts.items()}
