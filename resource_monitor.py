import psutil, notify2

THRESHOLD = 1000 * 1024 * 1024
APP_NAME = "sysmoniker"
TITLE = "RAM Usage"
MESSAGE = "RAM usage is too much... Close down some apps!!!"

def show_app(app_name, title, message):
	""" Function to display notification """
	
	notify2.init(app_name)
	n = notify2.Notification(title, message)
	n.show()
	
def main():
	""" Starter function to run the program """
	
	mem_available = psutil.virtual_memory().available
	if mem_available >= THRESHOLD:
		show_app(APP_NAME, TITLE, MESSAGE)
		
		

if __name__ == "__main__":
	main()
