from __future__ import unicode_literals

from ipaddress import ip_network, ip_address as IP


def is_bogon(ip_address):
    for network in BOGON_NETWORKS:
        if IP(ip_address) in network:
            return True
    return False


BOGON_NETWORKS = [
    ip_network("0.0.0.0/8"),
    ip_network("10.0.0.0/8"),
    ip_network("100.64.0.0/10"),
    ip_network("127.0.0.0/8"),
    ip_network("169.254.0.0/16"),
    ip_network("172.16.0.0/12"),
    ip_network("192.0.0.0/24"),
    ip_network("192.0.2.0/24"),
    ip_network("192.168.0.0/16"),
    ip_network("198.18.0.0/15"),
    ip_network("198.51.100.0/24"),
    ip_network("203.0.113.0/24"),
    ip_network("224.0.0.0/4"),
    ip_network("240.0.0.0/4"),
    ip_network("255.255.255.255/32"),
    ip_network("::/128"),
    ip_network("::1/128"),
    ip_network("::ffff:0:0/96"),
    ip_network("::/96"),
    ip_network("100::/64"),
    ip_network("2001:10::/28"),
    ip_network("2001:db8::/32"),
    ip_network("fc00::/7"),
    ip_network("fe80::/10"),
    ip_network("fec0::/10"),
    ip_network("ff00::/8"),
    ip_network("2002::/24"),
    ip_network("2002:a00::/24"),
    ip_network("2002:7f00::/24"),
    ip_network("2002:a9fe::/32"),
    ip_network("2002:ac10::/28"),
    ip_network("2002:c000::/40"),
    ip_network("2002:c000:200::/40"),
    ip_network("2002:c0a8::/32"),
    ip_network("2002:c612::/31"),
    ip_network("2002:c633:6400::/40"),
    ip_network("2002:cb00:7100::/40"),
    ip_network("2002:e000::/20"),
    ip_network("2002:f000::/20"),
    ip_network("2002:ffff:ffff::/48"),
    ip_network("2001::/40"),
    ip_network("2001:0:a00::/40"),
    ip_network("2001:0:7f00::/40"),
    ip_network("2001:0:a9fe::/48"),
    ip_network("2001:0:ac10::/44"),
    ip_network("2001:0:c000::/56"),
    ip_network("2001:0:c000:200::/56"),
    ip_network("2001:0:c0a8::/48"),
    ip_network("2001:0:c612::/47"),
    ip_network("2001:0:c633:6400::/56"),
    ip_network("2001:0:cb00:7100::/56"),
    ip_network("2001:0:e000::/36"),
    ip_network("2001:0:f000::/36"),
    ip_network("2001:0:ffff:ffff::/64"),
]
