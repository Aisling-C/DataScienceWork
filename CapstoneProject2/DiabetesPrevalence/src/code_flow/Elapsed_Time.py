def time_elapsed(start,end):
    #start is a datetime object that should be called at the 'start' reference point
    #requires "from datetime import datetime" to be called
    #prints the elapsed time between the start point and the time this function is called.
    import datetime as datetime
    diff=end-start
    s=diff.seconds
    secs_in_a_day = 86400
    secs_in_a_hour = 3600
    secs_in_a_min = 60
    days, seconds = divmod(s, secs_in_a_day)
    hours, seconds = divmod(seconds, secs_in_a_hour)
    minutes, seconds = divmod(seconds, secs_in_a_min)
    time_fmt = f"This process took {hours:02d} Hours {minutes:02d} Minutes {seconds:02d} Seconds "
    print(time_fmt)