import matplotlib.pyplot as plt


p_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
throughput = [0.8, 1.25, 1.5, 1.75, 2.0, 2.1, 2.0, 1.6, 1.2]  
delay = [1200, 1000, 850, 700, 600, 500, 550, 700, 950]       # (Average delay for each p)Higher p causes increasing delay due to collisions


# Plotting throughput
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(p_values, throughput, marker='o')
plt.title('Throughput vs Probability p')
plt.xlabel('Probability p')
plt.ylabel('Throughput (frames/sec)')

# Plotting average delay
plt.subplot(1, 2, 2)
plt.plot(p_values, delay, marker='o', color='red')
plt.title('Average Delay vs Probability p')
plt.xlabel('Probability p')
plt.ylabel('Average Delay (ms)')
plt.tight_layout()
plt.show()




# For a 
# 𝑝
# p-persistent CSMA protocol, the relationship between the probability 
# 𝑝
# p, throughput, and delay typically depends on the network conditions. A higher 
# 𝑝
# p often increases the likelihood of a device transmitting, leading to higher throughput but possibly increasing collisions, which in turn can increase delay.

# To provide accurate values of throughput and delay for each 
# 𝑝
# p, we would need to model the behavior of the system or have empirical data. However, I can suggest a pattern that would make the data more realistic:

# Throughput:

# Initially increases with increasing 
# 𝑝
# p as more frames are transmitted successfully.
# Peaks when 
# 𝑝
# p is in an optimal range (typically around 0.5 to 0.7).
# Starts to drop as collisions become more frequent for larger 
# 𝑝
# p.
# Delay:

# Initially decreases as 
# 𝑝
# p increases because fewer idle times are spent waiting to transmit.
# Increases at high p due to more collisions and subsequent retransmissions.


# Explanation:
# Throughput: Increases until 𝑝 = 0.6
# p≈0.6, after which it begins to drop as collisions increase.
# Delay: Decreases as p increases initially, but for higher 𝑝 , delay increases again due to network congestion and more frequent collisions.