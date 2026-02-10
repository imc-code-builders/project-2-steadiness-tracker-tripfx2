# Walking Steadiness 🚶

## What is Walking Steadiness?

When you walk, your body naturally wobbles — side to side, forward and back, and up and down. A fitness tracker or phone can measure this movement using an **accelerometer**, a sensor that detects changes in motion along three directions:

- **X axis**: Left and right
- **Y axis**: Forward and backward
- **Z axis**: Up and down

A perfectly steady walk would show very little change in these values. The more you wobble, the more the numbers jump around. In this project, you'll measure *how much* the accelerometer values jump around to give a walking steadiness score.

### What is "Wobble"?

Wobble is a measure of how far each reading strays from the average. If your X values are mostly around 50, but they keep jumping to 20 and 80, that's a lot of wobble. If they stay between 45 and 55, that's very steady.

We calculate wobble by:

1. Finding the **average** of all the readings
2. For each reading, finding **how far it is from the average**
3. Taking the **average of those distances**

A small wobble number = steady. A large wobble number = shaky.

## Part 1: Micro:bit Data Collection

### The Challenge

Hold your micro:bit flat in your hands like a tray. Take a few steps around the room and try to keep it as **steady** as possible. How smooth can you keep it? This is harder than it sounds!

### Setup

Open `microbit_starter.py` and copy the code to the micro:bit editor at https://python.microbit.org/v/3/

Complete the tasks in the starter code to make the micro:bit log accelerometer data:

1. **Toggle logging on/off** with Button A
2. **Delete the log** with Button B
3. **Log accelerometer data** while logging is on — log `x`, `y`, and `z` values from the accelerometer

### Collecting Your Data

1. Flash the completed code onto your micro:bit
2. Hold the micro:bit flat in your hands
3. Press Button A to start logging (you should see a checkmark)
4. Walk 10-15 steps, keeping the micro:bit as steady as you can
5. Press Button A to stop logging (you should see an X)
6. Plug the micro:bit into your laptop
7. Follow the instructions on the slides to download the CSV file
8. Move the CSV file into the `data/` folder in your project

## Part 2: Analyzing the Data

You'll work in `project_work.py` to build a program that reads the accelerometer data, calculates wobble for each axis, and gives you a grade.

The code is set up to read from `data/sample_data.csv` by default. Once you've collected your own data, change the filename at the bottom of `project_work.py` to point to your file.

---

### Step 1: calculate_average()

**Goal:** Return the average of all numbers in a list.

**How:** Use `sum(values) / len(values)`

**Example:** `[10, 20, 30]` → `20.0`

**Test it:** Run `python tests.py` — first test should pass.

---

### Step 2: calculate_wobble_for_axis()

**Goal:** Calculate how much the values vary ("diviate") from the average.

**How:**
1. Create an empty list to store your calculated "deviations"
2. Loop through the values
3. For each value, calculate the deviation with `abs(value - average)` and add it to your list
4. Return the average of the deviations list (HINT: you just wrote a function for this!)

`abs()` gives you the absolute value — it turns negative numbers positive. We care about *how far* each reading is from average, not *which direction*.

**Example:** Values `[10, 20, 30]` with average `20` → deviations are `[10, 0, 10]` → wobble is `6.67`

**Test it:** Run `python tests.py` — second test should pass.

---

### Step 3: determine_grade()

**Goal:** Return a grade letter and message based on the total wobble score.

**How:** Use if/elif/else. Print the resulting grade and message

| Total Wobble | Grade | Message |
|---|---|---|
| Less than 50 | A | Incredibly smooth! You walk like a robot! |
| Less than 100 | B | Very steady walking! |
| Less than 150 | C | Pretty good, but there's room for improvement. |
| Less than 200 | D | Quite wobbly - try walking more smoothly! |
| 200 or more | F | Very shaky! Were you running? |

**Test it:** Run `python tests.py` — third test should pass.

---

### Step 4: find_most_stable_axis()

**Goal:** Return the name of the axis with the **lowest** wobble — `"X"`, `"Y"`, or `"Z"`.

**How:** Compare the three wobble values using if statements to find the smallest.

**Test it:** Run `python tests.py` — fourth test should pass.

---

### Step 5: find_least_stable_axis()

**Goal:** Return the name of the axis with the **highest** wobble — `"X"`, `"Y"`, or `"Z"`.

**How:** Same idea as Step 4, but find the largest instead.

**Test it:** Run `python tests.py` — fifth test should pass.

---

### Step 6: analyze_walking_steadiness()

**Goal:** Put it all together. This function reads the data, calls all your other functions, and prints a full report.

**How:**
1. Read the data: `x_values, y_values, z_values = read_accelerometer_data(filename)`
2. Calculate the average for each axis
3. Print the averages (use `f"{value:.2f}"` to show 2 decimal places)
4. Calculate wobble for each axis using the averages
5. Print the wobbles
6. Calculate total wobble by adding x + y + z wobbles together
7. Get the grade and message from `determine_grade()`
8. Find the most and least stable axes
9. Print the total wobble, grade, message, and stability analysis

**Test it:** Run `python project_work.py` — you should see a full report.

## Testing

Run `python tests.py` after completing each step. It will tell you what passed and give hints if something is wrong.

Run `python project_work.py` to see your final results.

## Challenge

Try walking again with a different strategy — shorter steps? Slower pace? Bent knees? Can you beat your score? Compare with your classmates and see who has the steadiest walk!

## Challenge #2 (Once You've Finished All Three Parts of the Project)

Let's combine your data logging code and your calculations and display the steadiness grade on the Micro:Bit in real time as you walk around!

Here are some suggestions to get started:
- Instead of using the Micro:Bit log, store your XYZ accerlation values in three different lists.
- Update your `analyze_walking_steadiness` function:
  - Instead of reading data from the filename argument, use your three lists of acceleration values.
  - Remove the print statements and modify the function to return just the letter grade.
- Call `analyze_walking_steadiness` after you take a new accelerometer reading and `display.show()` the current letter grade before the `sleep(100)` statement.

Flash your Micro:Bit, then turn on logging and walk around to see your letter grade on the screen changing as you go!

Once you have this working, experiment with your code a bit more!
- What happens if you change the numeric ranges for each letter grade? Increase the numbers? Decrease the numbers?
- As you leave the Micro:Bit collecting data for longer, does it get easier or harder to change your letter grade? Why?
  - If you only kept a smaller amount of data at a time (ex: keep only the last 30 readings instead of forever growing your list), would that make it easier or harder to change your letter grade?
