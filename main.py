def task1():
    """
    Inputs:
        IP Address
        Prefix

    Outputs:
        Binary IP Address
        Subnet mask (Binary)
        Subnet mask (Decimal)
        Network address
        Broadcast address
        First address
        Last address (Default Gateway)

    """

    ip_address = input("IP Address: ")
    prefix = int(input("Prefix: "))

    def BinaryIPAddress():
        ip_split_dec=ip_address.strip().split(".")
        # print(ip_split_dec) # length 4

        ip_split_bin = []

        for a in ip_split_dec:
            bin_a = bin(int(a))
            bin_a = bin_a[2:]
            if len(bin_a) < 8:
                for a in range(8-len(bin_a)):
                    bin_a="0"+bin_a
            # print(bin_a)
            ip_split_bin.append(bin_a)


        return ip_split_bin

    ip_bin = BinaryIPAddress()
    print("IP Binary:",ip_bin)

    def SubnetMask():
        host_bytes = 32-prefix
        sub_mask =""

        for a in range(32-host_bytes):
            sub_mask+="1"
            if (a+1)%8==0:
                sub_mask+="."
        for a in range(host_bytes):
            sub_mask+="0"
        # return sub_mask
        sub_mask_split_bin = sub_mask.split(".")
        sub_mask_split_dec = []

        for a in sub_mask_split_bin:
            decimalint = int(a,2)
            sub_mask_split_dec.append(str(decimalint))

        print("Subnet mask BINARY:",sub_mask_split_bin)

        sub_mask_dec = ".".join(sub_mask_split_dec)
        return sub_mask_dec

    subnet_mask = SubnetMask()
    print("Subnet mask DECIMAL:",subnet_mask)

    def NetworkAddress():
        lastoctet = ip_bin[-1]
        host_bytes = 32-prefix
        # print("Last octet:",lastoctet)
        newoctet = lastoctet[:8-host_bytes]

        for a in range(host_bytes):
            newoctet+="0"

        network_address_bin = ip_bin
        del network_address_bin[-1]
        network_address_bin.append(newoctet)

        network_address_dec = []

        for a in network_address_bin:
            decimalint = int(a,2)
            network_address_dec.append(decimalint)

        return network_address_dec

    network_address = NetworkAddress()
    print("Network address:", network_address)


    def BroadcastAddress(): #same as in Network Address but last host bytes of the last octet are replaced with 1s
        #Should've used a decorator probably
        lastoctet = ip_bin[-1]
        host_bytes = 32 - prefix
        # print("Last octet:",lastoctet)
        newoctet = lastoctet[:8 - host_bytes]

        for a in range(host_bytes):
            newoctet+="1"

        broadcast_address_bin = ip_bin
        del broadcast_address_bin[-1]
        broadcast_address_bin.append(newoctet)

        broadcast_address_dec = []

        for a in broadcast_address_bin:
            decimalint = int(a, 2)
            broadcast_address_dec.append(decimalint)

        return broadcast_address_dec

    broadcast_address = BroadcastAddress()
    print("Broadcast address:", broadcast_address)

    def FirstAddress():
        first_address = network_address
        first_address[-1] = first_address[-1]+1
        return first_address

    first_address = FirstAddress()
    print("First Address:",first_address)

    def LastAddress():
        last_address = broadcast_address
        last_address[-1] = broadcast_address[-1]-1
        return last_address

    last_address = LastAddress()
    print("Last Address (Default gateway):",last_address)

task1()
