# Här skriver du ditt textäventyr
import random
print("Du vaknar i sängen en vacker morgon när ditt larm ringer. Så trött som du är tänker du på att somna om, gör du det? (Ja/Nej)")
svar = input().lower()
if svar == "ja":
    print("Du somnar om och sover resten av dagen. Slut 1/4")

elif svar == "nej":
    print("Du kliver upp och inser att du har glömt ditt namn. Vad heter du? ")
    spelare = input()
    print(f"Godmorgon {spelare}")
    print(f"\nFör eller senare tar du dig in till byn där du behöver handla matvaror.\nPå vägen dit ser du en affisch med en någon som håller i ett svärd och slåss med en drake.\nDu läser vad det står. 'En räddare i nöden, Drakdräpren {spelare}.' Du har aldrig dräpt en drake, och du vill inte heller det. ")
    print("\nVad gör du? Svara med A, B eller C \n \nA, Konfronterar byborna och säger att du inte vill dräpa någon drake. \nB, Accepterar ödet.\nC, flyr från byn")

Abc = input().lower()
if Abc == "a":
    print(f"Byborna blir ledsna och börjar gråta. 'Snälla {spelare} du måste hjälpa oss' ber dem. De tror verkligen att draken kommer förstöra byn\n\nVad tänker du nu? Svara mad A eller B")
    print("\nA, Synd för dem, inte mitt problem. \nB, Jag måste nog hjälpa dem.")
tanke = input().lower()
if tanke == "a":
        print("Du fortsätter med din dag så gott som möjligt fast byborna blev besvikna.\nSlut 2/4")

elif tanke == "b":
        print("Motiverad av byborna fortsätter du med din resa\n   Du går mot vapenaffären för att skaffa vapen och skaffar ett svärd och en karta.\n  Du vandrar länge innan du hittar draken. Draken är betydligt större än vad du hade förväntat dig och mitt i striden inser du att den kan spruta eld.")
        print("Våger du fortsätta?\n'Ja/Nej")
fortsättning = input().lower()
if fortsättning == "ja":
    Fighten = random.randint(1,5)
    if random == 1:
         print("På något sätt lyckades du slå ner draken och släpade med huvudet tillbaka som en trofé.\n Folket jublade när du kom tillbaka och nu hoppas du bara att du får leva vidare med ditt vanliga normala liv.Du stred med allt du hade men tyvärr var det inte tillräckligt.\nSlut 3/4")
    else:
         print("Du stred med allt du hade men tyvärr var det inte tillräckligt.\n Slut 4/4")
#fghjklö Nej
elif Abc == "b":
    print("Du accepterar ditt öde att besegra denna drake. En lång stund tänker du på hur du ska göra det och till slut kommer du på att du kan fråga den tidigare drakdräparen\n När du kommer fram till huset han bor i blir du välkomnad av honom")
    print(f"Välkommen {spelare}, jag har väntat på dig.\n Den gamla drakdräparen är gammal och ser inte ut som han ska springa runt och dräpa drakar längre, kanske därför han slutade.\n  Hur visste han att du skulle komma? Aja hursomehelst, du ber honom lära dig hur man besegrar en drake")
    print("Det tar lång tid att lära sig, men jag ska göra mitt bästa för att lära dig. Berättar gamlingen. Och du, som inte vill mista livet till draken, gör som han säger.\n\n Efter 2 veckor känner du dig redo att slå ner draken en gång för alla. Under natten tar du några vapen du lärt dig använda innan du smyger ut, gamlingen tyckte inte att du är redo än men vem bryr sig.")
    print("När du väl är framme inser du att draken är betydligt större än du förväntat dig.\n  Vågar du slå ner den? Ja/Nej")
fighten2 = input().lower()
if fighten2 == "ja":
     slaget = random.randint(1,2)
     if slaget == 1:
          print("Med alla träning och kunskap lyckas du slå ner draken och rädda byn. Du tar med dig drakhuvudet som en trofé och när du väl kommer tillbaka till byn är det gryning och folket jublar.\n slut 3/4")
     else:
          print("Trots all träning är draken för stark och du dör istället.\n slut 4/4")