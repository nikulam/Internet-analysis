import statistics

with open('results.txt') as file:
    measures = 0
    transmitted = 0
    received = 0
    rtts = [0]

    for line in file:
        if 'packets transmitted' in line:
            transmitted += float(line.split('received')[0].split(' ')[0])
            received += float(line.split('received')[0].split(' ')[3])
            measures += 1
    
        elif 'rtt' in line:
            rtt = float(line.split('/')[4])
            rtts.append(rtt)

    lost = (transmitted - received) / transmitted
    average = sum(rtts) / measures
    median = statistics.median(rtts)

    print(lost)
    print(average)
    print(median)



