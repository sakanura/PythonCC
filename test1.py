def generate_permutations(string):
    if len(string) == 1:
        return [string]
    permutations = []
    for i, char in enumerate(string):
        remaining_chars = string[:i] + string[i+1:]
        sub_permutations = generate_permutations(remaining_chars)
        for sub_permutation in sub_permutations:
            permutations.append(char + sub_permutation)
    
    return permutations
# Input
input_string = "abcde"
# Output
print("All permutations of", input_string, "are:", generate_permutations(input_string))
