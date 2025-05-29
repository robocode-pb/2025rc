from cc import peripheral
import time
peripheral.registerPeripheral('diesel_generator')
generator = peripheral.wrap('diesel_generator_0')
monitor = peripheral.wrap("monitor_1")
while True:
    fluid = generator.get('getFluid')
    fluidlevel = fluid.get('amount')
    monitor.clear()
    monitor.setCursorPos(1,1)
    monitor.write("Diesel generator")

    monitor.setCursorPos(1,2)
    monitor.write(str(fluidlevel))
    time.sleep(0.8)