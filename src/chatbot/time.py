def tell_time():
    from datetime import datetime
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."