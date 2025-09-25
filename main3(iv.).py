#new_file = open ("MYFILE.txt", "x") 
#print("File created successfully!")
#new_file.close ()

with open ("MYFILE.txt","w") as file:
    file.write (" Hello. I am living in KSK HOMES right now. I have been meeting different people from different cultural backgrounds. The place is quite boring sometimes however I have loved playing the game room:Playing PS4. But, I haven't been playing as I have been busy with myself.I dearly miss my family and friends a lot back in Mombasa.")
with open ("MYFILE.txt", "r") as file:
    print (file.read())

