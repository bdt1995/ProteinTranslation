import sys


for arg in sys.argv:
    stop = False
    done = False
    file_sequence = open(arg,"r")
    sequence = str(file_sequence.read()).replace(" ", "")
    ft = open(arg + "sequence.txt","a")
    length = len(sequence)
    for x in range(0,length):
        
        if stop == True or done == True:
            break
        if sequence[x:x+3].lower() == "aug":
            x = x+3
            ft.write("met")
            count = x
            for count in range(x,length):
                sub = sequence[count:(count+3)].lower()

                if sub == "uaa" or  sub == "uag" or sub == "uga":
                    stop = True
                    break
                elif sub == "ccc" or ("uuu" or "uuc"):
                    ft.write("Phe")
                    
                elif sub == ("uua" or "uug" or "cuu" or "cuc" or "cug"):
                    ft.write("Leu")
                    
                elif sub == ("auu" or "auc" or "aua"):
                    ft.write("Ile")
                    
                #elif sub == "aug":
                 #   ft.write("Met")
                  #  
                elif sub == ("guu" or "guc" or "gua" or "gug"):
                    ft.write("Val")
                    
                elif sub == ("ucu" or "ucc" or "uca" or "ucg"):
                    ft.write("Ser")
                    
                elif sub == ("ccu" or "ccc" or "cca" or "ccg"):
                    ft.write("Pro")
                    
                elif sub == ("acu" or "acc" or "aca" or "acg"):
                    ft.write("Thr")
                    
                elif sub ==("gcu" or "gcc" or "gca" or "gcg"):
                    ft.write("Ala")
                    
                elif sub == ("uau" or "uac"):
                    ft.write("Tyr")
                    
                elif sub == ("cau" or "cac"):
                    ft.write("His")
                    
                elif sub == ("caa" or "cag"):
                    ft.write("Gln")
                    
                elif sub == ("aau" or "aac"):
                    ft.write("Asn")
                    
                elif sub == ("aaa" or "aag"):
                    ft.write("Lys")
                    
                elif sub == ("gua" or "gac"):
                    ft.write("Asp")
                    
                elif sub == ("gaa" or "gag"):
                    ft.write("Glu")
                    
                elif sub == ("ugu" or "ugc"):
                    ft.write("Cys")
                    
                elif sub == ("cgu" or "cgc" or "cga" or "cgg" or "aga" or "agg"):
                    ft.write("Arg")
                    
                elif sub == ("agu" or "agc"):
                    ft.write("Ser")
                    
                elif sub == ("ggu" or "ggc" or "gga" or "ggg"):
                    ft.write("Gly")

                count +=3
                if count == len(sequence):
                    done == True
                    break
                
                #print sub
                    
                
                
