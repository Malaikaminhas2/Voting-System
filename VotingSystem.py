
import csv

def calculate_percentage(votes, total_votes):
  return (votes/total_votes)*100

# Welcome massage.
print("Welcome To The Voting Center")

# Nominee info. You can also add more than 2 nominee.
nominee1 = input("Enter the nominee 1 name : ")
nominee2 = input("Enter the nominee 2 name : ")
nominee3 = input("Enter the nominee 3 name : ")

# Initial value of there vote must be 0 for both.
nominee1Votes = 0
nominee2Votes = 0
nominee3Votes = 0

# Voter id to detect fake voters.
voterId = [1,2,3,4,5]
numberOfVoters = len(voterId)

# Open a file for writing the voting data.
with open('voting_data.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object.
    writer = csv.writer(csvfile)
    # Write the header row.
    writer.writerow(['Voter ID', 'Nominee1','Votes', 'Nominee2', 'Votes', 'Nominee3', 'Votes'])

    
    # main loop( we are using while loop).
    while True:

        # To check voter list is completed or become empty.
        if voterId == []:
            print("Voting session is over !!!")
            if nominee1Votes > nominee2Votes and nominee1Votes > nominee3Votes:
                # To calculate the percentage.
                percent = calculate_percentage(nominee1Votes, numberOfVoters)
                print("{} has won the election with {} %.".format(nominee1, percent))
                print('You win Election with', nominee1Votes, "Votes")
                # to break the loop and exit the program.
                break

            elif nominee2Votes > nominee1Votes and nominee2Votes > nominee3Votes:
                # To calculate the percentage.
                percent = calculate_percentage(nominee2Votes, numberOfVoters)
                print("{} has won the election with {} %.".format(nominee2, percent))
                print('You win Election with', nominee2Votes, "Votes")
               
                # to break the loop and exit the program.
                break

            elif nominee3Votes > nominee1Votes and nominee3Votes > nominee2Votes:
                # To calculate the percentage.
                percent = calculate_percentage(nominee3Votes, numberOfVoters)
                print("{} has won the election with {} %.".format(nominee3, percent))
                print('You win Election with', nominee3Votes, "Votes")
                
                # to break the loop and exit the program.
                break

            # if they got equal votes.
            else:
                print("Both have got equal number of votes !! Heigher authority will decide the final result, Thankyou !!")
                # to break the loop and exit the program.
                break
        
        # For taking voter id
        voterIdDetection = int(input("Enter your voter id : "))
        # for detecting fake voters vs real voters.
        if voterIdDetection in voterId:
            print("You are a genuine voter ")
            # we will remove voterId so that same voter can't vote again.
            voterId.remove(voterIdDetection)
        
            print("********************************************")

            print(f"To give a vote to {nominee1} Press 1 : ")
            print(f"To give a vote to {nominee2} Press 2 : ")
            print(f"To give a vote to {nominee3} Press 3 : ")

            print("********************************************")
            # checking voter votes whom.
            vote = int(input("Enter 'your PRECIOUS VOTE' : "))
            if vote == 1:
                nominee1Votes += 1
                print(f"{nominee1}, Thanks you to give me your important vote !! ")
            elif vote == 2:
              nominee2Votes += 1
              print(f"{nominee2}, Thanks you to give me your important vote !! ")
            elif vote == 3:
              nominee3Votes += 1
              print(f"{nominee3}, Thanks you to give me your important vote !! ")
            else:
              print("No nominee Data Found")  


                # Write the voting data to the CSV file.
            writer.writerow([voterIdDetection, nominee1, nominee1Votes,nominee2, nominee2Votes, nominee3, nominee3Votes])
        else:
          print('you Are Not a genuine voter')     

          
           
