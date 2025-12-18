def main():
    with open("D5_input.txt", "r") as f:
        fresh_ingredients_id_ranges = []
        fresh_ingredients_count = 0
        id_list_reached = False
        for line in f:
            if not line.strip() and not id_list_reached:
                 id_list_reached = True
                 continue
                 
            if id_list_reached:
                curr_id = int(line.strip())
                for start, end in fresh_ingredients_id_ranges:
                    if start <= curr_id and curr_id <= end:
                        fresh_ingredients_count += 1
                        break
            else:
                range_start, range_end = map(int, line.split("-"))
                fresh_ingredients_id_ranges.append((range_start, range_end))

        return fresh_ingredients_count


if __name__ == "__main__":
    print(main())