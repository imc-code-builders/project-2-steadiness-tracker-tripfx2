from data.utils import read_accelerometer_data


def calculate_average(values):
    # STEP 1: Return the average of all numbers in the list
    pass


def calculate_wobble_for_axis(values, average):
    # STEP 2: Calculate how much the values vary from the average
    # - Create an empty list for deviations
    # - Loop through values, calculate abs(value - average), add to list
    # - Return the average of the deviations list
    pass


def determine_grade(total_wobble):
    # STEP 3: Return the grade and message based on wobble score
    # Use if/elif/else and return two values separated by a comma:
    #   return "A", "Incredibly smooth! You walk like a robot!"
    #
    # Less than 50:  A - Incredibly smooth! You walk like a robot!
    # Less than 100: B - Very steady walking!
    # Less than 150: C - Pretty good, but there's room for improvement.
    # Less than 200: D - Quite wobbly - try walking more smoothly!
    # 200 or more:   F - Very shaky! Were you running?
    pass


def find_most_stable_axis(x_wobble, y_wobble, z_wobble):
    # STEP 4: Return the name of the axis with the lowest wobble ("X", "Y", or "Z")
    pass


def find_least_stable_axis(x_wobble, y_wobble, z_wobble):
    # STEP 5: Return the name of the axis with the highest wobble ("X", "Y", or "Z")
    pass


def analyze_walking_steadiness(filename):
    # STEP 6: Put it all together
    # 1. Read the data
    x_values, y_values, z_values = read_accelerometer_data(filename)

    # 2. Calculate average for each axis and print them

    # 3. Calculate wobble for each axis and print them

    # 4. Calculate total wobble (add all three wobbles together)

    # 5. Get the grade and message from determine_grade() and print them
    #    grade, message = determine_grade(total_wobble)

    # 6. Find and print the most and least stable axes

    pass


if __name__ == "__main__":
    analyze_walking_steadiness('data/sample_data.csv')