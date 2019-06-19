
#Source: Python Essential Reference by David M. Beazley

enable_tracing = True
if enable_tracing:
  debug_log = open("debug.log","w+")

def trace(func):
  if enable_tracing:
    def callf(*args,**kwargs):
      debug_log.write(f"Calling {func.__name__}: {args}, {kwargs}\n")
      r = func(*args,**kwargs)
      debug_log.write(f"{func.__name__} returned {r}\n")
      return r
    return callf
  else:
    return func

@trace
def square(x):
  return x*x

square(3)
