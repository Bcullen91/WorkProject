def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0
# test call
# print(ping("192.168.5.139"))
isonline == 1
while isonline == 1:
    ping("192.168.5.40")
    print(ping("192.168.5.40")
    if ping == "True":
        print("its working")
    else:
        isonline == 0
    print("The pi is still online")

