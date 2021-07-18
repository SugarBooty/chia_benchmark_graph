## Simple graph utility for chia benchmarks

It takes in CSV files and spits out a matplotlib graph of the results  
You must edit the code to use your files for now, but argument processing wouldnt be that hard to implement

CSV format: THREADS, BUCKETS, DURATION

Example of my rigs benchmark:

![Figure_2.png](https://raw.githubusercontent.com/SugarBooty/chia_benchmark_graph/main/Figure_2.png)

Example of the difference between a single disk and an LVM RAID0:  
(Top is single disk, bottom is RAID0 of 2 disks)

![Figure_2.png](https://raw.githubusercontent.com/SugarBooty/chia_benchmark_graph/main/Figure_1.png)
