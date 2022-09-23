import psutil, os

THRESHOLD = 1000 * 1024 * 1024

def main():
	while True:
		mem_available = psutil.virtual_memory().available
		if mem_available <= THRESHOLD:
			os.system("spd-say 'System is running slow, close all applications'")

if __name__ == "__main__":
	main()
