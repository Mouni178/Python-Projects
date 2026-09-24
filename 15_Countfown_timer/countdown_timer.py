import time


def countdown(seconds):
    while seconds > 0:
        minutes = seconds // 60
        remaining_seconds = seconds % 60

        print(
            f"Time Remaining: {minutes:02d}:{remaining_seconds:02d}",
            end="\r"
        )

        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")


print("===== COUNTDOWN TIMER =====")

seconds = int(input("Enter time in seconds: "))

if seconds <= 0:
    print("Please enter a positive number.")
else:
    countdown(seconds)
