import  miniupnpc
import socket
def open_upnp(port_no):
    '''this function opens a port using upnp'''
    upnp = miniupnpc.UPnP()

    upnp.discoverdelay = 10
    upnp.discover()

    upnp.selectigd()
    # addportmapping(external-port, protocol, internal-host, internal-port, description, remote-host)
    result=upnp.addportmapping(port_no, 'TCP', socket.gethostbyname(socket.gethostname()), port_no, 'testing', '91.77.244.112')
    #result = upnp.deleteportmapping(5001, 'TCP')
    return result
