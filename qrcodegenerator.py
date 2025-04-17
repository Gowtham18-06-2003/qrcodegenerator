import qrcode
'''qr=qrcode.make("please subscribe the python-life channel")
data="https://www.linkedin.com/in/abhiram-kothuri-140817250/"
qr=qrcode.make(data)
qr.save("docpy.png")
qr.show()'''








qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2

)

name=input("enter your name:")
age=int(input("enter your age:"))
email=input("enter your email:")
mobile=int(input("enter your mobile:"))
data={"name":name,"age":age,"email":email,"mobile":mobile}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("mydetails_in_qr.png")
img.show()

