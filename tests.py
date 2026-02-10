"""
Test file for project_work.py

Run this file to test your functions as you complete them.
It will tell you which functions are working correctly.

To run: python tests.py
"""

from project_work import (
    calculate_average,
    calculate_wobble_for_axis,
    determine_grade,
    find_most_stable_axis,
    find_least_stable_axis,
    analyze_walking_steadiness
)


def test_calculate_average():
    """Test the calculate_average function"""
    print("Testing calculate_average()...")

    try:
        # Test 1: Simple numbers
        result = calculate_average([1, 2, 3, 4, 5])
        expected = 3.0
        if abs(result - expected) < 0.001:
            print("PASS Test 1: [1,2,3,4,5] -> 3.0")
        else:
            print(f"FAIL Test 1: Expected {expected}, got {result}")

        # Test 2: Decimal numbers
        result = calculate_average([10.5, 12.3, 9.8])
        expected = 10.866666666666667
        if abs(result - expected) < 0.001:
            print("PASS Test 2: Decimal numbers work correctly")
        else:
            print(f"FAIL Test 2: Expected {expected:.3f}, got {result:.3f}")

        # Test 3: Single number
        result = calculate_average([42])
        expected = 42.0
        if abs(result - expected) < 0.001:
            print("PASS Test 3: Single number works")
        else:
            print(f"FAIL Test 3: Expected {expected}, got {result}")

    except Exception as e:
        print(f"ERROR calculate_average() has an error: {e}")
        print("Hint: Make sure you're using sum() and len()")

    print()


def test_calculate_wobble_for_axis():
    """Test the calculate_wobble_for_axis function"""
    print("Testing calculate_wobble_for_axis()...")

    try:
        # Test 1: Simple case where we know the answer
        values = [8, 10, 12]  # Average is 10, deviations are [2, 0, 2], average deviation is 4/3
        average = 10
        result = calculate_wobble_for_axis(values, average)
        expected = 1.3333333333333333
        if abs(result - expected) < 0.001:
            print("PASS Test 1: Basic wobble calculation works")
        else:
            print(f"FAIL Test 1: Expected {expected:.3f}, got {result:.3f}")

        # Test 2: No wobble (all values same as average)
        values = [5, 5, 5, 5]
        average = 5
        result = calculate_wobble_for_axis(values, average)
        expected = 0.0
        if abs(result - expected) < 0.001:
            print("PASS Test 2: No wobble case works")
        else:
            print(f"FAIL Test 2: Expected {expected}, got {result}")

    except Exception as e:
        print(f"ERROR calculate_wobble_for_axis() has an error: {e}")
        print("Hint: Use a loop to calculate abs(value - average) for each value")

    print()


def test_determine_grade():
    """Test the determine_grade function"""
    print("Testing determine_grade()...")

    try:
        test_cases = [
            (25, "A", "Incredibly smooth! You walk like a robot!"),
            (75, "B", "Very steady walking!"),
            (125, "C", "Pretty good, but there's room for improvement."),
            (175, "D", "Quite wobbly - try walking more smoothly!"),
            (250, "F", "Very shaky! Were you running?")
        ]

        all_passed = True
        for wobble, expected_grade, expected_message in test_cases:
            result = determine_grade(wobble)
            if result is not None and len(result) == 2:
                grade, message = result
                if grade == expected_grade and message == expected_message:
                    print(f"PASS Grade {expected_grade} test (wobble: {wobble})")
                else:
                    print(f"FAIL Grade {expected_grade} test:")
                    print(f"   Expected: {expected_grade}, '{expected_message}'")
                    print(f"   Got: {grade}, '{message}'")
                    all_passed = False
            else:
                print(f"FAIL determine_grade({wobble}) should return two values: grade, message")
                print(f"   Example: return \"A\", \"Incredibly smooth! You walk like a robot!\"")
                all_passed = False

        if all_passed:
            print("PASS All grade tests passed!")

    except Exception as e:
        print(f"ERROR determine_grade() has an error: {e}")
        print("Hint: Use if/elif/else and return two values like: return \"A\", \"message\"")

    print()


def test_stability_functions():
    """Test the stability analysis functions"""
    print("Testing stability analysis functions...")

    try:
        # Test find_most_stable_axis
        result = find_most_stable_axis(2.5, 1.2, 3.8)  # Y should be most stable (lowest)
        expected = "Y"
        if result == expected:
            print("PASS find_most_stable_axis() works correctly")
        else:
            print(f"FAIL find_most_stable_axis(): Expected {expected}, got {result}")

        # Test find_least_stable_axis
        result = find_least_stable_axis(2.5, 1.2, 3.8)  # Z should be least stable (highest)
        expected = "Z"
        if result == expected:
            print("PASS find_least_stable_axis() works correctly")
        else:
            print(f"FAIL find_least_stable_axis(): Expected {expected}, got {result}")

        # Test edge case: all equal
        result = find_most_stable_axis(2.0, 2.0, 2.0)
        if result in ["X", "Y", "Z"]:
            print("PASS find_most_stable_axis() handles equal values")
        else:
            print(f"FAIL find_most_stable_axis() with equal values: got {result}")

    except Exception as e:
        print(f"ERROR stability functions have an error: {e}")
        print("Hint: Compare wobble values and return 'X', 'Y', or 'Z'")

    print()


def test_main_function():
    """Test the complete analyze_walking_steadiness function"""
    print("Testing analyze_walking_steadiness()...")

    try:
        print("Running complete analysis with sample data:")
        print("=" * 50)
        analyze_walking_steadiness('data/sample_data.csv')
        print("=" * 50)
        print("PASS analyze_walking_steadiness() completed without errors!")

    except Exception as e:
        print(f"ERROR analyze_walking_steadiness() has an error: {e}")
        print("Make sure all your other functions are working first")

    print()


def run_all_tests():
    """Run all tests"""
    print("RUNNING ALL TESTS FOR PROJECT_WORK.PY")
    print("=" * 60)
    print()

    test_calculate_average()
    test_calculate_wobble_for_axis()
    test_determine_grade()
    test_stability_functions()
    test_main_function()

    print("=" * 60)
    print("TESTING COMPLETE!")
    print()
    print("Tips for success:")
    print("   - Work on functions one at a time")
    print("   - Test each function as you complete it")
    print("   - Ask for help if you get stuck!")


if __name__ == "__main__":
    run_all_tests()