import os 
os.system("cd /Users/elizbr/Documents/NLP/TheBachelor")
 
directory = r'/Users/elizbr/Documents/NLP/TheBachelor/srt' 
for filename in os.listdir(directory):
    print(os.path.join(directory, filename))
    try:
        os.system(f"python3 process.py '{filename}'")
    except: 
        print('nope') 
