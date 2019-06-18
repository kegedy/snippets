import multiprocessing
import time

def clock(interval):
  while True:
    print(f"The time is {time.ctime()}")
    time.sleep(self.interval)

class ClockProcess(multiprocessing.Process):
  def __init__(self,interval):
    multiprocessing.Process.__init__(self)
    self.interval = interval

  def run(self):
    while True:
      print(f"The time is {time.ctime()}")
      time.sleep(self.interval)

if __name__ == '__main__':
  #p = multiprocessing.Process(target=clock, args=(15,))
  p = ClockProcess(15)
  p.start()
      
