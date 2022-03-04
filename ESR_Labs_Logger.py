logstr='''2017-11-20 00:02:17.216   143   143 I DeveloperMode: Enabling developer mode
2017-11-20 00:02:17.488   149   149 I redundantboot: The device was booted from bootloader1
2017-11-20 00:02:17.652   145   145 I Netd    : Successfully created NetworkController
2017-11-20 00:02:17.677   145   145 I Netd    : Successfully created ExtendedInterfaceController
2017-11-20 00:02:21.688   145   160 D Netd    : Setting iface cfg
2017-11-20 00:02:21.688   145   160 D Netd    : Trying to bring down eth0
2017-11-20 00:02:31.443   155 34102 D ServiceManager: Service vehicleDiagnosticMiddleware has been started in process vdm
2017-11-20 00:02:31.474   155 31794 W VAL     : Steering side unknown, cannot map left/right passenger signals
2017-11-20 00:02:32.390   155 36203 D SmartCard: Releasing smart card from session 0x2d5c05d
2017-11-20 00:02:32.412   155  5549 W VDM     : Cannot read DoIP message, closing connection
2017-11-20 00:02:32.412   155  5549 W VDM     : java.net.SocketException: Connection reset
2017-11-20 00:02:32.412   155  5549 W VDM     :      at java.net.SocketInputStream.read(SocketInputStream.java:209)
2017-11-20 00:02:32.412   155  5549 W VDM     :      at java.net.SocketInputStream.read(SocketInputStream.java:141)
2017-11-20 00:03:12.168   155 34102 D Process : Starting process diagnostics
2017-11-20 00:03:12.282   155 34102 D Process : Starting process diagnostics.obdc
2017-11-20 00:04:05.378   155 27549 D rheating_v1:   state=invalid
2017-11-20 00:04:05.378   155 27549 D rheating_v1:
2017-11-20 00:04:05.378  1155 27549 D rheating_v1:   state=invalid '''

log_str= logstr.splitlines()
Key_a= ('TimeStamp', 'Process ID', 'ThreadID', 'LogLevel','ProcessName','ProcessMsg')
Dict_a={}
Dict_a=Dict_a.fromkeys(Key_a)
for key in Key_a:
    Dict_a.setdefault(key,None)

print('The Dict_a is ',Dict_a)
Dict_a['TimeStamp']=[]
Dict_a['Process ID']=[]
Dict_a['ThreadID']=[]
Dict_a['LogLevel']=[]
Dict_a['ProcessName']=[]
Dict_a['ProcessMsg']=[]

for Temp_str in log_str:
    Temp_a=Temp_str.split(' ')
    while '' in Temp_a:
        Temp_a.remove('')
    Dict_a['TimeStamp'].append(Temp_a[0] + ' ' + Temp_a[1])
    Dict_a['Process ID'].append(Temp_a[2])
    Dict_a['ThreadID'].append(Temp_a[3])
    Dict_a['LogLevel'].append(Temp_a[4])
    Dict_a['ProcessName'].append(Temp_a[5])
    Dict_a['ProcessMsg'].append( ''.join(Temp_a[6:len(Temp_a)]))
    print('\n')

print(Dict_a)

