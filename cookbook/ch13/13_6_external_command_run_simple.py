import subprocess

try :
    out_bytes = subprocess.check_output(['netstat','-h'])
    print(out_bytes)
    #byte to text
    out_text = out_bytes.decode('utf-8')
    print(out_text)

except subprocess.CalledProcessError as e :
    out_bytes = e.output
    code = e.returncode

