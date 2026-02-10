import csv


def read_accelerometer_data(filename):
    """
    Reads accelerometer data from a CSV file.

    This function is provided for you because file reading can be tricky for beginners.
    It reads x, y, z values from a CSV file and normalizes the z values by adding 1000.

    Args:
        filename (str): Path to the CSV file containing accelerometer data

    Returns:
        tuple: Three lists (x_values, y_values, z_values) containing the data

    Example:
        x, y, z = read_accelerometer_data('data.csv')
        print(f"First x value: {x[0]}")
    """
    x_values = []
    y_values = []
    z_values = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            x_values.append(float(row['x']))
            y_values.append(float(row['y']))
            z_values.append(float(row['z']) + 1000)  # Normalize Z

    return x_values, y_values, z_values


def create_sample_data():
    """
    Creates sample data for testing when no CSV file is available.

    Returns:
        tuple: Three lists (x_values, y_values, z_values) with test data
    """
    x_values = [10.5, 12.3, 9.8, 11.2, 10.1]
    y_values = [5.2, 4.8, 5.5, 5.0, 5.3]
    z_values = [1015.6, 1012.4, 1018.9, 1013.7, 1016.2]

    return x_values, y_values, z_values


def read_sample_csv():
    """
    Reads the sample_data.csv file from the project directory.

    Returns:
        tuple: Three lists (x_values, y_values, z_values) from the CSV
    """
    return read_accelerometer_data('sample_data.csv')