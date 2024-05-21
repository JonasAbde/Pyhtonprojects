# Write a program that asks the user to enter a number of seconds and works as follows:
# There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or
# equal to 60, the program should convert the number of seconds to minutes and seconds.

# There are 3600 second in an hour. If the number of seconds entered by the user is greater than or
# equal to 3600, the program should convert the number of seconds to hours, minutes and seconds.

# There are 86400 seconds in a day. If the number of seconds entered by the user is greater than or
# equal to 86400, the program should convert the number of seconds to days, hours, minutes and
# seconds.

def convert_seconds(total_seconds):
    SECONDS_IN_A_MINUTE = 60
    SECONDS_IN_AN_HOUR = 3600
    SECONDS_IN_A_DAY = 86400

    days = total_seconds // SECONDS_IN_A_DAY
    remaining_seconds = total_seconds % SECONDS_IN_A_DAY

    hours = remaining_seconds // SECONDS_IN_AN_HOUR
    remaining_seconds = remaining_seconds % SECONDS_IN_AN_HOUR

    minutes = remaining_seconds // SECONDS_IN_A_MINUTE
    seconds = remaining_seconds % SECONDS_IN_A_MINUTE

    return days, hours, minutes, seconds


def main():
    total_seconds = int(input("Enter the number of seconds: "))

    days, hours, minutes, seconds = convert_seconds(total_seconds)

    result = []
    if days > 0:
        result.append(f"{days} day(s)")
    if hours > 0:
        result.append(f"{hours} hour(s)")
    if minutes > 0:
        result.append(f"{minutes} minute(s)")
    if seconds > 0 or total_seconds == 0:  # To handle the case where total_seconds is 0
        result.append(f"{seconds} second(s)")

    print("Converted time: " + ", ".join(result))
main()
