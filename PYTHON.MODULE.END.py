feedback_data={
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
     ], 'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]}

print(feedback_data)

n=int(input("enter how many more feedbacks wanted"))
sno=11
for i in range(n):
    name=input("Enter a name")
    feedback=input("Enter a feedback")
    rating=int(input("Enter a rating in between(1-5)"))

    feedback_data["S_No"].append(sno)
    feedback_data["Name"].append(name)
    feedback_data["Feedback"].append(feedback)
    feedback_data["Rating"].append(rating)
    sno +=1
    
print(feedback_data)


for i in range(len(feedback_data["Feedback"])):
    Feedback=feedback_data["Feedback"][i]
    Feedback=Feedback.replace(".","")
    Feedback=Feedback.replace(",","")
    Feedback=Feedback.replace("!","")
    Feedback=Feedback.replace("?","")
    Feedback=" ".join(Feedback.split())
    Feedback=Feedback.strip()
    Feedback=Feedback.lower()

    feedback_data["Feedback"][i] = Feedback
              
print(feedback_data)



word=input("Enter a word")
def count_word_in_feedbacks(word):
    count=0
    for i in feedback_data["Feedback"]:
        if word.lower() in i.lower().split():
            count +=1
    return count
    
res=count_word_in_feedbacks(word)
print(word,res)

res=count_word_in_feedbacks("good")
print("good",res)
res=count_word_in_feedbacks("poor")
print("poor",res)
res=count_word_in_feedbacks("excellent")
print("excellent",res)


print(feedback_data)
    
print("Final Cleaned Feedback Data:",feedback_data)

totalrating=sum(feedback_data["Rating"])
print(totalrating)
no=len(feedback_data["Rating"])
print(no)
average=totalrating/no
print("average rating",round(average,2))


wordcount=0
longestcomment=""
for i in  feedback_data["Feedback"]:
    ogwordcount=len(i.split())
    if ogwordcount>wordcount:
        wordcount=ogwordcount
        longestcomment=i
        

print("longestcomment:",longestcomment)
print("wordcount:", wordcount)


uniqueset = set()

for i in feedback_data["Feedback"]:
    words = i.split()
    uniqueset.update(words)

print("Unique words:", sorted(uniqueset)) 

feedback_entries = zip(
    feedback_data["Rating"],
    feedback_data["S_No"],
    feedback_data["Name"],
    feedback_data["Feedback"]
)
sorted_feedbacks = sorted(feedback_entries, reverse=True)
print("Feedbacks sorted by rating:")
for Rating, S_No, Name, Feedback in sorted_feedbacks:
    print(Rating,S_No,Name,Feedback)




    
    

   
                 
      


