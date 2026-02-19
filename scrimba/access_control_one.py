# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.



badgeno={101,102,103,104,105} #revoked badges
approved=[]
denied=[]

while True:
  name=input("Enter name : (or 'done' to exit ) ")
  if(name.lower()=="done"):
    break
  else:
    bno=int(input("Enter your badge number : "))
    if bno in badgeno:
      print("access denied !")
      denied.append(name) 
    else:
      print("access Granted !")
      approved.append(name) 
      
print("===== Access Summary =====")
print("\nApproved Visitors : ")
for i,person in enumerate(sorted(approved)):
  print(f"{i+1} - {person} ")
print("\nDenied Visitors : ")
for i,person in enumerate(sorted(denied)):
  print(f"{i+1} - {person} ")


print("\n")
print(f"Total Apporved visitors: {len(approved)}")
print(f"Total Denied visitors: {len(denied)}")





