import subprocess
p = subprocess.Popen(["ping", "-c", "10", "www.cyberciti.biz"], stdout=subprocess.PIPE)
output, err = p.communicate()
print  output
 
