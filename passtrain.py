import argparse
import time
import getpass
import os


def attempt_submission(true_passphrase):
   guessed_passphrase = getpass.getpass("Enter your passphrase: ")
   if guessed_passphrase == true_passphrase:
      print('[*] Yep!')
      return True
   else:
      print('[!] Nope...')
      return False


if __name__=='__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument("-n", "--num_consec", dest="num_consec", type=int, default="10", 
                       help="number of consecutive successes before exit")
   args = parser.parse_args()

   passphrase = getpass.getpass("Enter passphrase to remember: ")

   # Clear terminal so no cheating ;)  
   os.system('cls' if os.name == 'nt' else 'clear')

   num_success = 0
   print("PASSTRAIN: Upload your passphrase into your brain")
   while num_success < args.num_consec:
       if attempt_submission(passphrase):
           num_success += 1
       else:
           num_success = 0
   print("[*] Looks like you've got it! Exiting.")
   time.sleep(1) 
