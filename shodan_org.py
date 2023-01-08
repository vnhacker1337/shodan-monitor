from shodan import Shodan
from shodan.cli.helpers import get_api_key
from termcolor import colored
import sys
import os

header1 = r'''
				   _   _   _   _   _   _   _   _   _  
				  / \ / \ / \ / \ / \ / \ / \ / \ / \ 
				 ( s | h | o | l | i | s | t | e | r )
				  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ v0.1
'''
header2 = r'''
Hostname search using [Org] Filter.
Coded By: Mr.X (@vnhacker1337)
'''
print(colored(header1, 'red', attrs=['bold']))
print(colored(header2, 'white', attrs=['bold']))
main_domains_file = sys.argv[1]
api = Shodan(get_api_key())
limit = 1000
counter = 0
results = []
ips = []

with open(main_domains_file, 'r') as domains:
	try:
		for line in domains:
			line = line.strip()
			output = os.getcwd() + "/output"
			if os.path.exists(output) == False:
				os.makedirs(output)

			_line = line.replace(" ", "_")
			filename = output + "/" + line + '_shodan.txt'
			filename01 = output + "/" + line + '_ip_shodan.txt'


			f = open(filename, 'a+')
			f1 = open(filename01, 'a+')

			print(colored("[+] Searching for: ", 'green') + line)
		   
			# org search 
			org_query = 'org:"' + line + '" 200'
			for banner in api.search_cursor(org_query):
				for hostname in banner['hostnames']:
					results.append(hostname)
				
				ip = banner['ip_str']
				if ip not in ips:
					f.write(ip + "\n")
					ips.append(ip)
					
				counter += 1
				if counter >= limit:
					break
		   
			results_length = len(results)
			print(colored("-> Found " + str(results_length) + " unique result for Organization ["+ line + "] responds with status code [200 OK]", 'cyan'))
			print(colored("-> Output file name: " + filename, 'cyan') + "\n")
			# get results to output file
			for line in results:
				f.write(line + "\n")
			f.close()
			results = []
	  

	except KeyboardInterrupt:
		print(colored("\nKeyboardInterrupt detected! GoodBye", 'red'))
		pass
