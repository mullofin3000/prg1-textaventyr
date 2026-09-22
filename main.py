# Här skriver du ditt textäventyr
print("Du vaknar i sängen en vacker morgon när ditt larm ringer. Så trött som du är tänker du på att somna om, gör du det? (Ja/Nej)")
svar = input().lower 
if svar == "ja":
    print("Du somnar om och sover resten av dagen. Slut 1/4")
elif svar == "nej":
    print("Du kliver upp och inser att du har glömt ditt namn. Vad heter du? ")
    spelare = input()
    print(f"Godmorgon {spelare}")
    print(f"\nFör eller senare tar du dig in till byn där du behöver handla matvaror.\nPå vägen dit ser du en affisch med en man som håller i ett svärd och slåss med en drake.\n Du löser vad det står. En räddare i nöden, Drakdräpren {spelare}. Du har aldrig dräpt en drake, och du vill inte heller det. ")
    print("Vad gör du? Svara med A, B eller C \nA, Konfronterar byborna och säger att du inte vill dräpa någon drake. \nB, Accepterar ödet.\nC, flyr från byn")
Abc = input().lower
if Abc == "a":
    print("Byborna blir ledsna och börjar gråta för att dem tror att byn kommer gå under samtidigt som dem försöker övertyga dig att dräpa den.\nVad tänker du nu?")
    print("A, Synd för dem, inte mitt problem. \nB, Jag måste nog hjälpa dem.")
    tanke = input().lower
    if tanke == "a":
        print("Du fortsätter med din dag så gott som möjligt fast byborna blev besvikna.\nSlut 2/4")

        