import statistics

def main():
    values = []

    print("Please enter integers. Press Enter when you are done.")
    
    while True:
        user_input = input("Enter an integer: ")
        
        if user_input == "":
            break
        
        try:
            value = int(user_input)
            values.append(value)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    if len(values) > 0:
        mean_value = statistics.mean(values)
        median_value = statistics.median(values)
        try:
            mode_value = statistics.mode(values)
        except statistics.StatisticsError:
            mode_value = "No unique mode (multiple modes)"
        
        max_value = max(values)
        min_value = min(values)
        range_value = max_value - min_value
        variance_value = statistics.variance(values)
        stdev_value = statistics.stdev(values)
        
        print("\nStatistics for your entered numbers:")
        print(f"Mean: {mean_value}")
        print(f"Median: {median_value}")
        print(f"Mode: {mode_value}")
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")
        print(f"Range: {range_value}")
        print(f"Variance: {variance_value}")
        print(f"Standard Deviation: {stdev_value}")
    else:
        print("No numbers were entered. Please try again.")

if __name__ == "__main__":
    main()
