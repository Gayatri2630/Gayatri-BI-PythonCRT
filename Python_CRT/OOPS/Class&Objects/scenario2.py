'''
Scenario:
You had participated in your college-level coding fest which was there for 6 days
Task:
Write a Python Program to give the final report which includes
1.Activites for the day including timeline
2.Number of Teams/participants for the day
3.Project Names
4.Technologies Used
5.PPT Demonstrations Given
6.Winner of Day
7.Runner up of the Day
8.Best Performer of the Day
9.Host of the program for that day
'''
class Fest:
    def __init__(self,day,activities,teams,project,technology,demo,winner,runner,bestperformer,host):
        self.Day=day
        self.Activities=activities
        self.Teams=teams
        self.Project=project
        self.Technology=technology
        self.Demo=demo
        self.Winner=winner
        self.Runner=runner
        self.BestPerformer=bestperformer
        self.Host=host
def Display_details(self):
    print("--------------------------------------------------------------")
    print("College Level Fest")
    print("--------------------------------------------------------------")
    print(f"Day:{self.Day}")
    print(f"Activities for the day including timeline:{self.Activities}")
    print(f"Number of Teams for the Day:{self.Teams}")
    print(f"Project Names:{self.Project}")
    print(f"Technologies:{self.Technology}")
    print(f"Presentations are given:{self.Demo}")
    print(f"Winner of Day:{self.Winner}")
    print(f"Runner up of the Day:{self.Runner}")
    print(f"Best Performer of the Day:{self.BestPerformer}")
    print(f"Host of the Program for the Day:{self.Host}")
D1=Fest(1,"Welcome Ceremony",5,"Project_AI,Project_DS","python","Yes","Team-A","Team-D","Paru","Gagan,Bhoomi")
D2=Fest(2,"Workshops on python and web development",6,"Python using AI","python,HTML,CSS","Yes","Team-C","Team-B","Nelu","Deva,Paravathi")
D3=Fest(3,"Hackathon and Team collaboration",8,"Project-a,Project-b","python.Flask","Yes","Team-Alpha","Team-Delta","Sampadha","Shourya,Kalyani")
D4=Fest(4,"Coding Challange and Team presentations",14,"Project-c,project-d","python,Flask","Yes","Team-Mega","Team-Pro","Srivalli","Dheeraj,Prema")
D5=Fest(5,"Final Coding Sessions and Debugging",16,"Project-e,proect-f","python,Django","Yes","Team-Ultra","Team-Meta","Srivalli","Saagar,Naramada")
D6=Fest(6,"Closing Ceremony and Award Distribution",16,"Project-g,Project-h","python,React","Yes","Team-L","Team-M","Manohari","Amar,Bhagi")
Display_details(D1)
Display_details(D2)
Display_details(D3)
Display_details(D4)
Display_details(D5)
Display_details(D6)

