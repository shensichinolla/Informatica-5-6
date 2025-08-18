def main():
    emoji = input("Write a message with an emoji:")
    convert(emoji)

def convert(message):
    message = message.replace(":)", "😊").replace(":(", "☹️")
    print(message)
    
main()
