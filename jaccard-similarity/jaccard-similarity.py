def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a = set(set_a)
    set_b = set(set_b)

    jaccard = 0.0       # default jaccard to 0.0 as required
                        # this will be returned if union is empty
    if (set_a | set_b): # validate if union is empty set befpre proceeding
        # length of set intersection is compared with length of set union
        jaccard = len(set_a & set_b) / len(set_a | set_b)

    return jaccard