import sched, time

def do_something(scheduler): 
    print("Started...")
    # schedule the next call first
    scheduler.enter(2, 1, do_something, (scheduler,))
    print("Doing stuff...")
    # then do your stuff
    print("...Ended")
    
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(3, 1, do_something, (my_scheduler,))
my_scheduler.run()