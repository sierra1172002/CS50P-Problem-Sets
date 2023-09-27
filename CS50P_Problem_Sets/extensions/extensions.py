usinp=input('File name: ',).strip().lower().split('.')

image= ["gif","png"]
application=["pdf","zip"]

if usinp[-1] in image:
    print("image/"+usinp[-1])
elif usinp[-1] in application:
    print("application/"+usinp[-1])
elif usinp[-1]=='jpeg' or usinp[-1]=='jpg':
    print("image/jpeg")
elif usinp[-1]=='txt':
    print('text/plain')
else:
    print('application/octet-stream')