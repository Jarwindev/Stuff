biljett_pris=int(input("Ange biljettpris: "))
årskort_pris=int(input("Ange årskortspris: "))
besök_frekvens=int(input("Ange besök per år: "))
if(besök_frekvens*biljett_pris<årskort_pris):
    print("Årskort lönar sig")
else:
    print("Biljett lönar sig")