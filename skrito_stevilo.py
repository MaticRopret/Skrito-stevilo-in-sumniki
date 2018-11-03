# -*- encoding: utf-8 -*- #

secret_number = 8


print "Pred vami je igra ugibanja skritega števila. Na voljo imate 5 poizkusov."
for x in range(1, 6 ):
    guess = int ( raw_input ("""POIZKUS """ + str(x) + """/5. 
Vnesite število med 5 in 10: """) )

    if guess == secret_number:
        print "Čestitamo, uganili ste skrito število!"
        break
    elif guess > secret_number:
        print "Število " + str(guess) + " je napačno. Ponovno poizkusite z MANJŠIM številom."
    elif guess < secret_number:
        print "Število " + str(guess) + " je napačno. Ponovno poizkusite z VEČJIM številom."
