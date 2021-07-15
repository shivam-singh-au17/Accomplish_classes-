
"""
(Maximum marks -15)
Q-1 ) Briefly describe CAP theorem (5 marks)
(Easy)

"""





"""
The CAP theorem is a belief from theoretical computer science about distributed data stores that claims, in the event of 
a network failure on a distributed database, it is possible to provide either consistency or availability—but not both.


The CAP Theorem is comprised of three components (hence its name) as they relate to distributed data stores:

Consistency. All reads receive the most recent write or an error.
Availability. All reads contain data, but it might not be the most recent.
Partition tolerance. The system continues to operate despite network failures (ie; dropped partitions, slow network 
connections, or unavailable network connections between nodes.)
In normal operations, your data store provides all three functions. But the CAP theorem maintains that when a
 distributed database experiences a network failure, you can provide either consistency or availability.

"""







"""
Q-2) Explain DHCP, ARP and NAT. (5 marks)
(Easy)

"""



"""

DHCP
But how exactly a network interface is assigned an IP-address? One of the options – manually. The disadvantage: 
handwork. If you're no good with your hands, you can configure duplicate addresses and get a conflict :)

Another option: Dynamic Host Configuration Protocol (DHCP), a protocol used for setting different configuration, 
including IP-addresses, automatically.

Refer to RFC documentation for more details on DHCP: https://www.ietf.org/rfc/rfc2131.txt

For DHCP to work, you need a DHCP-server, which will assign IP-addresses, and a DHCP-client on your device,
 which will request for an address. At home, the DHCP-server is usually located in router.

In order to understand how exactly DHCP works, you need to focus on "broadcasting". This is a process, 
in which our server transfers a message to all servers in the network, as it doesn't know where exactly the 
information it needs is located. Such a broadcast communication is close to a radio broadcasting.

In case of DHCP, it happens like this:

A DHCP-client sends a broadcast message with a request "I need an IP-address"
A DHCP-server catches it and sends back also a broadcast message "I have an IP-address x.x.x.x, do you want it?"
The DHCP-client receives the message and sends another one: "Yes, I want the address x.x.x.x"
The DHCP-server answers "Ok, then x.x.x.x belongs to you"


NAT
When you were reading about CIDR, there was something that might get your attention: even if we divide the network into many blocks, the total
 amount of IP-addresses isn't going to increase. Actually, a combination of private and public addresses is always used.
  Usually, one public address hides a lot of machines, each one having its own private address.

This is also true for our VMs. Each one has the private IP-address from the block 192.168.122.0/24, and all of 
them are hidden behind the public address of the host machine.

The host machine, if we continue to use our private laptop at home as it, is hidden behind our Wi-Fi router and
 also doesn't have a public address.


"""










"""
Q-3) Longest Palindrome (5 marks)
https://leetcode.com/problems/longest-palindrome/
(Easy)
Given a string s which consists of lowercase or uppercase letters, return the
length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome
here.
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7

"""



class Solution:
    def longestPalindrome(self, s: str) -> int:
    	D = {}
    	for c in s:
    		if c in D:
    			D[c] += 1
    		else:
    			D[c] = 1
    	L = D.values()
    	E = len([i for i in L if i % 2 == 1])
    	return sum(L) - E + (E > 0)





