import os,sys
import pty
import threading
import serial
import time

ser = serial.Serial(sys.argv[1],int(sys.argv[2]),timeout=3)



class serialSniff():
	def __init__(self):
		self.readlogfile = open("readlog.txt","wb")
	        self.writelogfile = open("writelog.txt","wb")
        	self.master,self.slave= pty.openpty()
		s_name = os.ttyname(self.slave)
		print "Configured to virtual device "+s_name
		self.th1=threading.Thread(target=self.write)
		self.th2=threading.Thread(target=self.read)
		self.exit=False
		self.s=serial.Serial(s_name)

	def write(self):
		print "In thread 1"
		while not self.exit:
			wr_data=os.read(self.master,1000)
			ser.write(wr_data)
			print wr_data
			self.writelogfile.write(wr_data+"\n")
		print "Exiting thread 1"
		return 0			

	def read(self):
		print "In thread 2"
		while not self.exit:
			rd_data=ser.read()
			while(rd_data!='\r'):
				os.write(self.master,rd_data)
				self.readlogfile.write(rd_data)
				sys.stdout.write(rd_data)
				rd_data=ser.read()
				if self.exit:
					rd_data='\r'
			os.write(self.master,rd_data)
			self.readlogfile.write("\n")
			print ""
		print "Exititng thread 2"
		return 0

	def startThread(self):
		self.th1.start()
		self.th2.start()
		while not self.exit:
			try:
				#print "looking for ctrl+c"
				time.sleep(1)
			except KeyboardInterrupt:
				self.exit=True
				self.s.write('a')
				#print "found ctrl+c"
		self.th1.join()
		self.th2.join()
		ser.close()
		self.readlogfile.close()
		self.writelogfile.close()
		if self.th1.isAlive():
			print "Thread 1 not closed"
		else:
			print "Thread 1 closed"
		if self.th2.isAlive():
			print "Thread 2 not closed"
		else:
			print "Thread 2 closed"

if __name__ == '__main__':
	sniff = serialSniff()
	sniff.startThread()

