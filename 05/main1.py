filename = 'input.txt'
garden: dict = {}
seeds: list

current_header = str
with open(filename) as file:
    first_line = True
    for line in file:
        line = line.strip()
        if first_line:
            first_line = False
            seeds = line.split()[1:]
        else:
            if line:
                if '-' in line:
                    current_header = line.split()[0]
                    # Its a title
                    garden[current_header] = []
                else:
                    soil_info = line.split()
                    if len(soil_info) == 3:
                        source = current_header.split('-')[0]
                        destination = current_header.split('-')[-1]
                        data = {
                                "source": int(soil_info[1]),
                                "destination": int(soil_info[0]),
                                "range": int(soil_info[2])
                            }
                        if current_header in garden.keys():
                            garden[current_header].append(data)
                        else:
                            garden[current_header] = [data]


def source_to_destination_recursive(
    source_no: int,
    source_header: str,
    garden: dict):
        result: int = None
        destination: str

        for key, val in garden.items():
            if source_header == key.split('-')[0]:
                destination = key.split('-')[2]
                for info in val:
                    if source_no >= info["source"] \
                    and source_no < info["source"] + info["range"]:
                        # If within this range, we can find its destination number here
                        result = (source_no - info["source"]) + info["destination"]
                        break
                if result is None:
                    result = source_no
                break

        if destination == 'location':
            return result
        else:
            return source_to_destination_recursive(result, destination, garden)

locations = []

for seed in seeds:
    locations.append(source_to_destination_recursive(int(seed), "seed", garden))
    locations = sorted(locations)
print(locations[0])