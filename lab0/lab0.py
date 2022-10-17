def main_func(filename):
    with open(filename, "r") as f:
        def ip2network_ip(ip):
            list_of_bytes = list(ip.split())
            network_ip = [list_of_bytes[0], list_of_bytes[1], list_of_bytes[2], str(int(list_of_bytes[3]) & 192)]
            return (' ').join(network_ip)

        ip_s = f.readlines()
        list_of_networks = list(map(ip2network_ip, ip_s))

        casual_dict = {k: 0 for k in list_of_networks}
        ip_s = set(ip_s)
        for ip in ip_s:
            if not ip == ip2network_ip(ip) and not bin(int(ip.split()[-1]))[-6:] == "1" * 6:
                casual_dict[ip2network_ip(ip)] += 1
        network_with_max_agents = max(casual_dict, key=casual_dict.get)
        print("answers for file " + filename + " is", len(set(list_of_networks)), max(casual_dict.values()),"(second answer for network "+network_with_max_agents+")")


main_func("log1.txt")
main_func("log2.txt")
