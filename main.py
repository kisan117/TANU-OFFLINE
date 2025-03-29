import requests
import json
import time
import pytz
import datetime
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
class MyHandler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          self.wfile.write(b"<h1> CREDIT :- SONU LEGEND<br> <br> <h1> OWNER => SONU <br> <br> <h1> WATSAPP :- +")
def execute_server():
      PORT = int(os.environ.get('PORT', 4000))
      with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
          print("Server running at http://localhost:{}".format(PORT))
          httpd.serve_forever()

# Get current time in UTC
utc_now = datetime.datetime.utcnow()
# Localize to Indian Standard Time
indian_timezone = pytz.timezone('Asia/Kolkata')
ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(indian_timezone)
# Format the time
formatted_time = ist_now.strftime("\033[1;38;5;208m Time :- %Y-%m-%d %I:%M:%S %p")
print(formatted_time)

def send_messages_from_file():

    with open('A-token.txt', 'r') as file:
      tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\033[1;92m' + '[[ 🩷]] 💔]] [[🌼]] [[😘]]𝗦𝗢𝗡𝗨=𝗦𝟯𝗥𝗩𝟯𝗥=𝗥𝗨𝗡𝗡𝗜𝗡𝗚=[[💔]][[ 😘]] =')

    headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

    liness()

    access_tokens = [token,strip() for token in tokens]


    with open('A-convo.txt', 'r') as file:
      convo_id = file.read().strip()

    with open('A-file.txt', 'r') as file:
      messages = file.readlines()

      num_messages = len(messages)

      max_tokens = min(num_tokens, num_messages)

    with open('A-name.txt', 'r') as file:
      haters_name = file.read().strip()

    with open('A-speed.txt', 'r') as file:
      speed = int(file.read().strip())

    liness()


    while True:
      try:
            for message_index in range(num_messages):
              token_index = message_index % max_tokens
              access_token = tokens[token_index].strip()

              message = messages[message_index].strip()

              url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
              parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
              response = requests.post(url, json=parameters, headers=headers)

              if response.ok:
                    print("\033[1;36m[✓] Ha Bhai Chla Gya Tera Massage No. {} of Convo {} Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print(formatted_time)
                    liness()
                    liness()
              else:
                    print("\033[1;35m[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print(formatted_time)
                    liness()
                    liness()
              time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")
      except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      send_messages_from_file()

if __name__ == '__main__':
      main()
