def sum_ranges(ranges: list[tuple[int, int]]) -> int:
    '''
    Accepts a sorted list of non-overlapping ranges.
    Calculates sum of ranges.
    
    :param ranges: List of sorted ranges.
    :type ranges: list[list[int]]
    :return: Sum of ranges.
    :rtype: int
    '''
    total_sum = 0
    for start, end in ranges:
        total_sum += end - start + 1
    
    return total_sum

def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    '''
    Merges all overlapping ranges in a passed list of ranges.
    
    :param ranges: Sorted list of ranges.
    :type ranges: list[list[int]]
    :return: List of merged ranges.
    :rtype: list[list[int]]
    '''
    if not ranges:
        return []
    merged = [ranges[0]]

    for curr_start, curr_end in ranges[1:]:
        last_start, last_end = merged[-1]
        if last_end >= curr_start:
            merged[-1] = (last_start, max(last_end, curr_end))
        else:
            merged.append((curr_start, curr_end))
    return merged

def main() -> int:
    '''
    Reads a text file of a list of ranges.
    Turns them into integers and returns the sum of all ranges without overlaps.
    
    :return: Sum of all ranges without overlaps.
    :rtype: int
    '''
    with open("D5_input.txt", "r") as f:
        fresh_ingredients_id_ranges: list[tuple[int, int]] = []
        for line in f:
            if not line.strip():
                break
            
            start: int
            end: int
            start, end = map(int, line.split("-"))
            fresh_ingredients_id_ranges.append((start, end))
        
        fresh_ingredients_id_ranges.sort()

        fresh_ingredients_id_ranges_merged: list[tuple[int, int]] = merge_ranges(fresh_ingredients_id_ranges)

        range_sum: int = sum_ranges(fresh_ingredients_id_ranges_merged)

        return range_sum

if __name__ == "__main__":
    print(main())