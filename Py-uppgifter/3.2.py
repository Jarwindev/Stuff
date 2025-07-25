# Program som jämför biljettpris och årskortspris.

# Användaren anger biljettpris, årskortspris och uppskattad mängd besök per år.

biljett_pris=int(input("Ange biljettpris: "))
årskort_pris=int(input("Ange årskortspris: "))
besök_frekvens=int(input("Ange besök per år: "))

# Jämför kostnaden för att köpa biljetter mot att köpa ett årskort.
# Om kostnaden för biljetter är mindre än den för årskort, skrivs ut att årskort lönar sig.
# Annars skrivs det ut att biljetter lönar sig.

if(besök_frekvens*biljett_pris<årskort_pris):
    print("Årskort lönar sig")
else:
    print("Biljett lönar sig")