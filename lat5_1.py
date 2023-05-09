# Case Study: Virtual Assistant using Python (main.py)
# Link terkait SMTP Module : https://docs.python.org/3/library/smtplib.html 

from Assistant import Assistant

def main():
    
    jarvis = Assistant(name='Jarvis')
    jarvis.run()

if __name__ == "__main__":
    main()