gigs_used_input = int(input("How much data did you use last month in gigs? "))

def gigs_used(gigs_used):
    if  gigs_used <= 12:
        tax = 50 * .06625
        gigs12 = 50 + tax
        print("You will pay " + str(gigs12) + ", which includes tax.")
    elif gigs_used > 12 and gigs_used <= 30:
        tax2 = 60 * .06625
        gigs30 = 60 + tax2
        print("You will pay " + str(gigs30) + ", which includes tax.")
    elif gigs_used > 30 and gigs_used <= 50:
        tax3 = 80 *.06625
        gigs50 = 80 + tax3
        print("You will pay " + str(gigs50) + ", which includes tax.")
    else:
        print("Invalid Input")
        print("If you put over 50, then there is no cell phone plan for you.")

gigs_used(gigs_used_input)

