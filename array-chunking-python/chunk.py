"""
Method to chunk a list in python into chunks of size chunk_size
"""
def chunking(input: list[int], chunk_size: int):
    out = []

    for i in range(0, len(input), chunk_size):
        out.append(input[i:i + chunk_size])

    return out

"""
The above but as a one-liner
"""
def chunking_oneliner(input: list[int], chunk_size: int):
    return [input[i:i+chunk_size] for i in range(0, len(input), chunk_size)]

"""
Method to chunk a list in python into a specified number of buckets. If the 
input cannot be evenly divided, the extra will be put into an extra bucket.
"""
def chunking_even_size(input: list[int], buckets: int):
    chunk_size = len(input) // buckets
    out = []

    for i in range(0, len(input), chunk_size):
        out.append(input[i:i + chunk_size])

    return out

"""
The above but as a one-liner, this really is ugly and hard to 
read but I like trying
"""
def chunking_even_size_oneliner(input: list[int], buckets: int):
    return [input[i:i + chunk_size] for i in range(0, len(input), len(input) // buckets)]

"""
Method to chunk a list in python into a specified number of buckets. If the 
input cannot be evenly divided, the extra will be put into the last bucket
"""
def chunking_even_size_forced(input: list[int], buckets: int):
    out = chunking_even_size(input, buckets)

    # Check if we couldn't evenly divide
    if len(out[-1]) != len(input) // buckets:
        # Append the last bucket to the 2nd to last
        out[-2] += out[-1]
        # Remove the last bucket
        out.pop()

    return out

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(chunking(my_list, 2))
    assert chunking(my_list, 2) == chunking_oneliner(my_list, 2)

    print(chunking(my_list, 4))
    print(chunking_even_size(my_list, 3))
    print(chunking_even_size_forced(my_list, 3))
