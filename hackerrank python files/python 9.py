if __name__ == '__main__':
    n = int(input())  # Read the number of scores (not needed in logic, but part of input)
    scores = list(map(int, input().split()))  # Read the scores as a list of integers

    # Use set to remove duplicates, then convert back to list and sort in descending order
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)

    # The second element is the runner-up score
    print(unique_scores[1])
