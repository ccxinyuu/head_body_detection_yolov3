from detect import * 
import subprocess


    
def run_command():
    r = subprocess.Popen(['python', 'detect.py', '--source', '..\\testimage1.jpg'])
    out, err = r.communicate()
    return out

    
if __name__ == '__main__':
    print("output:" , run_command()) 
    
    