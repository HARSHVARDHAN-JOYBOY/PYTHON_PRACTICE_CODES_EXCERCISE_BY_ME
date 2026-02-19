def summon_the_mistake(depth):
    # Recursive call to simulate deep stack trace
    if depth == 0:
        unleash_the_beast("not_a_number")  # Will raise a TypeError
    else:
        summon_the_mistake(depth - 1)

def unleash_the_beast(thing):
    # Cause a deliberate error
    return thing + 42  # Can't add str and int, raises TypeError

def begin_the_chaos():
    try:
        summon_the_mistake(30)  # Create deep recursion for long traceback
    except Exception as e:
        print("🔥🔥🔥 A wild error has appeared! 🔥🔥🔥\n")
        raise  # Let Python print the entire error stack

begin_the_chaos()
