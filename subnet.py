import tkinter as tk
import re  

win = tk.Tk()
win.title("Subnet")
win.geometry("600x400")

left_fr = tk.Frame(win)
left_fr.grid(row=0,column=0)


in_ip = tk.StringVar(left_fr)
sub_mask = tk.StringVar(left_fr)
network_addr = tk.StringVar(left_fr)
ip_data = tk.StringVar(left_fr)
ip_data_bin = tk.StringVar(left_fr)
net_data = tk.StringVar(left_fr)
sub_data = tk.StringVar(left_fr)
sub_bin =  tk.StringVar(left_fr)
def display():
	ip_data.set(in_ip.get())
	binary_ip='.'.join([bin(int(x)+256)[3:]for x in in_ip.get().split('.')]) #converting in to binary
	lst=[]


	print(f"ip address in  binary:{binary_ip}")
	ip_data_bin.set(binary_ip)
	 #taking subnet mask input

#covert subnet mask to binary num
	j=str(1)
	sub_data.set(sub_mask.get())
	for i in range(int(sub_mask.get())):
		lst.append(j)

	b=str(0)  #after 1s zeros
	z=32-int(sub_mask.get())

	for j in range(z):
		lst.append(b)

	sm_str="".join(lst) 


	print(sm_str)  

#moving for spliting 
	sbd=re.findall('........',sm_str)  #spliting each 8 bit
	final_sm_b=".".join(sbd)

	print(f" Subnet mask in binary :{final_sm_b}")  # here we can find 8 bit splited binary number

	sm_lst=final_sm_b.split(".")
	print(sm_lst)  #it print in []
	sub_bin.set(final_sm_b)

# convert binary subnet mask to octformat
	count=0
	ijk=[]
	for i in sm_lst:
		binary_num=list(sm_lst[count])
		value=0
		for i in range(len(binary_num)):
			digit=binary_num.pop()
			if digit =='1':
				value=value + pow(2,i)
		count +=1
		ijk.append(value)
	subnet_mask=".".join(map(str,ijk))
	print(f"subnet mask :{subnet_mask}")


#finding network address


	n_lst=[]  #creating empty list for n/w add
	new=list(in_ip.get().split("."))  #ip addressing []

	for i in range(len(new)):
		n_lst.append(int(new[i]) & ijk[i])  #AND operation
	network_add=".".join(map(str,n_lst))
	print(network_add)
	net_data.set(network_add)

#finding Broadcast addres

	network_add_b ='.'.join([bin(int(x)+256)[3:]for x in network_add.split('.')])

	print(network_add_b)
	string_sm="".join(final_sm_b.split("."))


tk.Label(left_fr,text = "IP Address").grid(row=0,column=0)
ip_addr = tk.Entry(left_fr,textvariable=in_ip)
ip_addr.grid(row=0,column=1)

tk.Label(left_fr,text = "Subnet Mask").grid(row=1,column=0)
sub_mask = tk.Entry(left_fr,textvariable=sub_mask)
sub_mask.grid(row=1,column=1)

tk.Button(left_fr,text="Display",command = display).grid(row=2,column=1)

tk.Label(left_fr,text = "IP Address:").grid(row=3,column=0)
ip_box = tk.Label(left_fr,textvariable=ip_data)
ip_box.grid(row=3,column=1)

tk.Label(left_fr,text = "IP Address Binary:").grid(row=4,column=0)
ip_box_bin = tk.Label(left_fr,textvariable=ip_data_bin)
ip_box_bin.grid(row=4,column=1)

tk.Label(left_fr,text = "Subnet Mask :").grid(row=5,column=0)
sub_box = tk.Label(left_fr,textvariable=sub_data)
sub_box.grid(row=5,column=1)


tk.Label(left_fr,text = "Subnet Mask Binary:").grid(row=6,column=0)
sub_box_bin = tk.Label(left_fr,textvariable=sub_bin)
sub_box_bin.grid(row=6,column=1)
tk.Label(left_fr,text = "Network Address:").grid(row=7,column=0)
net_box = tk.Label(left_fr,textvariable=net_data)
net_box.grid(row=7,column=1)

win.mainloop()
