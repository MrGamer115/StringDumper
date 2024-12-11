import sys

def logo():
    print(r"""
   _____ _        _             _____                                  
  / ____| |      (_)           |  __ \                                 
 | (___ | |_ _ __ _ _ __   __ _| |  | |_   _ _ __ ___  _ __   ___ _ __ 
  \___ \| __| '__| | '_ \ / _` | |  | | | | | '_ ` _ \| '_ \ / _ \ '__|
  ____) | |_| |  | | | | | (_| | |__| | |_| | | | | | | |_) |  __/ |   
 |_____/ \__|_|  |_|_| |_|\__, |_____/ \__,_|_| |_| |_| .__/ \___|_|   
                           __/ |                      | |              
                          |___/                       |_|                    
    """)

def getContent():
    file_path = str(input("Path: "))
    global char_min_length
    try:
        char_min_length = int(input("Length of Chars: "))
        print("")
    except ValueError:
        print("Type a valid number!")
        sys.exit()

    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print("File not found")
        sys.exit()


def analyzeFile():
    index = 0
    hex_values = []
    cur_text = []

    for line in getContent():
        if (line >= 33 and line <= 126):
            index +=1 
            hex_values.append(hex(line))
            cur_text.append(chr(line))
            if (index == char_min_length):
                print(f"{' '.join(hex_values)} : {''.join(cur_text)}")
                
                index = 0
                hex_values.clear()
                cur_text.clear()
    print("\nEnd")
    
    

def main():
    logo()
    analyzeFile()

if __name__ == "__main__":
    main()
