# Packet-Visualizer

### Overview
It is a Python-based network diagnostic tool that recreates the tracert utility. It takes domain as input and outputs a table to help visualize the path of the data packets.

### Features
- Command Line Interface (CLI) tool
- Uses TCP Port 443 (HTTPS) to bypass firewalls that typically block standard ICMP "Ping" requests
- Uses ipinfo.io API to fetch physical location of IP Address
- DNS Lookup
- Calculates Round Trip Time (RTT) for every hop
- Easy visualiztion due to the use of table

### Tech Stack
| Purpose | Technology | Version |
| ------------- | ------------- | ------------- | 
| Language | Python | 3.14.0 |
| DNS Lookup | Socket | --- |
| Transfer Data Packet | Scapy | 2.7.0 |
| Geolocation | Ipinfo.io | --- |
| Visualization | Rich | 14.3.3 |

### User Interface
![b972f6c4-0803-41c1-a12c-d28a47645e78](https://github.com/user-attachments/assets/4c9f79fd-e144-45f8-bc40-90c9ab666446)
