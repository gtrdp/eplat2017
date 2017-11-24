import psutil
import subprocess
import time

subprocess.Popen("python traffic_controller.py", shell=True, stdout=subprocess.PIPE)

for i in range(15):
    time.sleep(1)

for process in psutil.process_iter():
    if process.cmdline() == ['python', 'traffic_controller.py']:
        print('Process found. Terminating it.')
        process.terminate()
        break
