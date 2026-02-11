from data.utils import read_accelerometer_data

def calculate_average(values):
    # STEP 1: Return the average of all numbers in the list
    if not values:
        return 0
    return sum(values) / len(values)

def calculate_wobble_for_axis(values, average):
    # STEP 2: Calculate how much the values vary from the average
    # - Create an empty list for deviations
    deviations = []
    # - Loop through values, calculate abs(value - average), add to list
    for v in values:
        deviations.append(abs(v - average))
    # - Return the average of the deviations list
    return calculate_average(deviations)

def determine_grade(total_wobble):
    # STEP 3: Return the grade and message based on wobble score
    # Less than 50: A - Incredibly smooth! You walk like a robot!
    if total_wobble < 50:
        return "A", "Incredibly smooth! You walk like a robot!"
    # Less than 100: B - Very steady walking!
    elif total_wobble < 100:
        return "B", "Very steady walking!"
    # Less than 150: C - Pretty good, but there's room for improvement.
    elif total_wobble < 150:
        return "C", "Pretty good, but there's room for improvement."
    # Less than 200: D - Quite wobbly - try walking more smoothly!
    elif total_wobble < 200:
        return "D", "Quite wobbly - try walking more smoothly!"
    # 200 or more: F - Very shaky! Were you running?
    else:
        return "F", "Very shaky! Were you running?"

def find_most_stable_axis(x_wobble, y_wobble, z_wobble):
    # STEP 4: Return the name of the axis with the lowest wobble ("X", "Y", or "Z")
    wobbles = {"X": x_wobble, "Y": y_wobble, "Z": z_wobble}
    return min(wobbles, key=wobbles.get)

def find_least_stable_axis(x_wobble, y_wobble, z_wobble):
    # STEP 5: Return the name of the axis with the highest wobble ("X", "Y", or "Z")
    wobbles = {"X": x_wobble, "Y": y_wobble, "Z": z_wobble}
    return max(wobbles, key=wobbles.get)

def analyze_walking_steadiness(filename):
    # STEP 6: Put it all together
    # 1. Read the data
    x_values, y_values, z_values = read_accelerometer_data(filename)

    # 2. Calculate average for each axis and print them
    avg_x = calculate_average(x_values)
    avg_y = calculate_average(y_values)
    avg_z = calculate_average(z_values)
    print(f"Averages -> X: {avg_x:.2f}, Y: {avg_y:.2f}, Z: {avg_z:.2f}")

    # 3. Calculate wobble for each axis and print them
    wobble_x = calculate_wobble_for_axis(x_values, avg_x)
    wobble_y = calculate_wobble_for_axis(y_values, avg_y)
    wobble_z = calculate_wobble_for_axis(z_values, avg_z)
    print(f"Wobble -> X: {wobble_x:.2f}, Y: {wobble_y:.2f}, Z: {wobble_z:.2f}")

    # 4. Calculate total wobble (add all three wobbles together)
    total_wobble = wobble_x + wobble_y + wobble_z
    print(f"Total Wobble: {total_wobble:.2f}")

    # 5. Get the grade and message from determine_grade() and print them
    grade, message = determine_grade(total_wobble)
    print(f"Grade: {grade} - {message}")

    # 6. Find and print the most and least stable axes
    most = find_most_stable_axis(wobble_x, wobble_y, wobble_z)
    least = find_least_stable_axis(wobble_x, wobble_y, wobble_z)
    print(f"Most stable axis: {most}")
    print(f"Least stable axis: {least}")

if __name__ == "__main__":
    # Ensure 'data/sample_data.csv' exists or update the path
    analyze_walking_steadiness('data/sample_data.csv')