def main():
    # Prompt user for task description
    task = input("Enter your task: ")

    # Prompt user for task priority
    priority = input("Priority (high/medium/low): ").lower()

    # Prompt user for time-bound status
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
    reminder_message = f"'{task}' is a {priority} priority task"

    match priority:
        case 'high':
            if time_bound == 'yes':
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += ". Consider completing it as soon as possible."
        case 'medium':
            if time_bound == 'yes':
                reminder_message += " that requires attention soon."
            else:
                reminder_message += ". You can complete it based on your schedule."
        case 'low':
            if time_bound == 'yes':
                reminder_message += " that requires attention today."
            else:
                reminder_message += ". Consider completing it when you have free time."
        case _:
            reminder_message = "Invalid priority entered. Please choose from high, medium, or low."

    # Print the customized reminder message
    print("\nReminder:", reminder_message)

if __name__ == "__main__":
    main()

