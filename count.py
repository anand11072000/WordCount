def word(text):
    words=text.split()
    try:
        if len(words)==0:
            print("You have entered no Setence/Paragraph")
    except:
        print("You have entered no Setence/Paragraph")
    finally:
        return len(words)
def user():
    user_input=input("Enter the Sentence/Paragraph:")
    count=word(user_input)
    print(f"No of words in Sentence/Paragraph:{count}")

user()   
        
