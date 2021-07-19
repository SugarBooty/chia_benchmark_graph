import subprocess

POOL_CON_KEY = {INSERT_HERE}
FARM_PUB_KEY = {INSERT_HERE}

# Edit these to fit your setup
buckets = [128, 256, 512]
threads = [40, 36, 32, 28, 24]
# paths for Chia
processingDrive = "/mnt/{WORKING DIRECTORY}"
archicalDrive = "/mnt/{ARCHIVE DIRECTORY}"

def run_command(command: str) -> list:
    # runs the command and keeps the output, element 0 is STDIO, element 1 is STDERR
    # formats the output and splits it into a list by line
    # if theres any errors it prints them out
    # returns the list of output lines

    commandOutput = subprocess.Popen(
    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    commandOutputFormatted = commandOutput[0].decode('utf-8').split('\n')
    if commandOutput[1]:
        errorFormatted = commandOutput[1].decode('utf-8')
        print(f'ERROR: {errorFormatted}')
    return commandOutputFormatted

def log_to_file(line: str):
    f = open("Benchmark_output", "a")
    f.write(line + "\n")
    f.close

# reads through all the output lines and finds the one that has the duration
# returns the amount of seconds it took to complete the plot
def parse_output(output: list) -> str:
    for line in output:
        if (line.find("Total plot creation time") != -1):
            splitLine = line.split(" ")
            duration = splitLine[5]
            return duration

def start_benchmark():
    for bucket in buckets:
        for thread in threads:
            command = f"chia_plot -n 1 -r {thread} -u {bucket} -t {processingDrive} -d {archicalDrive} -c {POOL_CON_KEY} -f {FARM_PUB_KEY}"
            print(f"Starting madmax | Threads: {thread} Buckets: {bucket}")
            output = run_command(command)
            duration = parse_output(output)
            print(f"Plot Time: {duration}")
            log_to_file(f"{thread},{bucket},{duration}")

start_benchmark()
