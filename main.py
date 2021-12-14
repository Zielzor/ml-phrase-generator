import random 

LIST_1=["Dear colleagues,","At the same time,","However,","Nevertheless,","Hence,","On the other hand,",
"Even so,","Moreover,"]
LIST_2=["the paradigm of ","context of ","business integration of ","a pragmatic approach to ",
"the commutative effect of ","the expotentnial growth of ","funding of ","the hype around "]
LIST_3=["machine learning ","AI revolution ","deep learning ","ML solutions ","AI pipelines ",
"data labeling ","AI research ","MLOps "]
LIST_4=["opens new possibilites for ","challenges us for ","gains the risks of ","widens the horizons of ",
"forces us to search for" ,"escalates the problem of" ,"gives no chance to" ,"leads the community to "]
LIST_5=["the deeper development of ","more expensive research in ","unpredictable bias in ",
"computational stability of ","generalized weight in ","practical usage of ","customized layers in ",
"the pruned "]
LIST_6=["neural machine translators.","teinforcement learning research.","feature map extractors.",
"deep fakes.","super-resolution models.","multi-task classification.","real-time detection.", "generative models."]


phrase_list = []

def random_ml_related_phrase():
    phrase = (random.choice(LIST_1) + random.choice(LIST_2) + random.choice(LIST_3) + random.choice(LIST_4) +
    random.choice(LIST_5) + random.choice(LIST_6))
    return phrase 

def writing_phrases(list,filename):
    try:
        with open(f"{filename}.txt","a") as f:
            f.write('\n'.join(list))
    except FileNotFoundError:
        with open(f"{filename}.txt","w") as f:
            f.write('\n'.join(list))
    print("Text file generated.")

def unique_phrases_generated():
    try:
        unique_phrases = set(open("generated_phrases.txt").readlines())
        if len(unique_phrases) == 0:
            print("File is empty")
        else:
            print(f"File contains {len(unique_phrases)} unique phrases")
    except FileNotFoundError:
        print("No file found")

def phrase_generating():
    while True:
        welcome_message=str(input("Would you like to generate a phrase for incoming meeting?:> y/n? "))
        if welcome_message == "y":
            meeting_phrase = random_ml_related_phrase()
            if meeting_phrase not in phrase_list:
                phrase_list.append(meeting_phrase)
                print(meeting_phrase)
            else:
                print("Phrase already used")     
        else:
            writing_phrases(phrase_list,"generated_phrases")
            break

def remove_duplicate_phrases_from_file():
    with open ("generated_phrases.txt", "r+") as f:
        unique_phrases = set(open("generated_phrases.txt").readlines())
        unique_phrases = list(unique_phrases)
        data = f.read()
        f.seek(0)
        f.writelines(unique_phrases)
        f.truncate()
        print("Duplicates removed from file.")


phrase_generating()
unique_phrases_generated()
remove_duplicate_phrases_from_file()


