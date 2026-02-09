def assign_segment(R: int, F: int, M: int) -> str:
    """
    Assign customer segment based on RFM scores.
    """

    if R >= 4 and F >= 4 and M >= 4:
        return "Champions"
    elif R >= 3 and F >= 3:
        return "Loyal Customers"
    elif R <= 2 and F >= 3:
        return "Potential Loyalists"
    elif R <= 2 and F <= 2:
        return "At Risk"
    else:
        return "Others"


if __name__ == "__main__":
    print(assign_segment(5, 5, 5))   # Champions
    print(assign_segment(1, 2, 2))   # At Risk
