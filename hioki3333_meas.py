#!/usr/bin/env python3


import threading
import time
import pyvisa

rm = pyvisa.ResourceManager()
resources = rm.list_resources() # Discover available instruments
print(resources)

# Open connections to specific instruments
analyzer = rm.open_resource('ASRL/dev/ttyUSB0::INSTR') # hioki_3333
analyzer.timeout = 5000
#print(analyzer.query('*IDN?'))
#smu = rm.open_resource('ASRL1::INSTR')

# Send commands and read data from each instrument
analyzer.write('*RST')
analyzer.write('*IDN?')
analyzer.write('*TST?')
analyzer.write('RS232c?')
analyzer.write('SCALE?')
analyzer.write('SCALe:CT 2')
analyzer.write('SCALe:VT 10')
##print(analyzer.query('SCALE?')
analyzer.write('VOLTage:RANge <200>')
##volts=analyzer.query('VOLTage:RANge?')
#print(analyzer.query('VOLTage:RANge?')
analyzer.write('CURRent:RANge 0.5')
analyzer.write('CURRent:RANge?')
#print(analyzer.query('CURRent:RANge?')
analyzer.write('DISPLAY: U,I,P')
analyzer.write('MEAS? U,I,P')
#VIP=analyzer.query('MEAS? U,I,P')

#analyzer.read('\n')
#print(analyzer.query('*IDN?'))


# Close the serial port
analyzer.close()

# with threading

#def control_instrument(instrument_name, delay):
#	print(f"Controlling {instrument_name}...")
	#time.sleep(delay)  # Simulate instrument operation
	#print(f"{instrument_name} finished.")

# Create threads for different instruments
	#thread1 = threading.Thread(target=control_instrument, args=('Oscilloscope', 2))
	#thread2 = threading.Thread(target=control_instrument, args=('Power Supply', 1))

# Start the threads
	#thread1.start()
	#thread2.start()

# Wait for threads to complete
	#thread1.join()
	#thread2.join()
	#print("All instruments controlle
