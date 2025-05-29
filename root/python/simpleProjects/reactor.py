from cc import peripheral
import time
reactor = peripheral.wrap("BigReactors-Reactor_0")
monitor = peripheral.wrap("monitor_0")
while True:
    energystats=reactor.getEnergyStats()
    energy = energystats["energyStored"]
    capacity = energystats["energyCapacity"]
    producing = energystats["energyProducedLastTick"]
    monitor.setCursorPos(1,1)
    monitor.write("REACTOR STATS")
    monitor.setCursorPos(1,2)
    monitor.write("Energy Stored:"+str(energy)+"FE")
    monitor.setCursorPos(1,3)
    monitor.write("Capacity:"+str(capacity)+"FE")
    monitor.setCursorPos(1,4)
    monitor.write("Generating:"+str(producing)+"FE/t")
    monitor.setCursorPos(1,8)
    time.sleep(0.8)


    copacity = 5
    monitor.setCursorPos(2, 2)
    monitor.write("[")
    for i in range(28):
        if(copacity<i):
            monitor.write('-')
        else:
            monitor.write('#')
    monitor.write("]")

    time.sleep(0.5)
    monitor.clear()