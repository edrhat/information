import os

print("-----------------------------------------------------")
print("SCRIPT PARA BUSCAR INFORMAÇÕES PÚBLICAS DE DOMÍNIOS")
print("-----------------------------------------------------")
so = input("Está usando qual sistema operacional ?.\nWindows[1]\nLinux[2]\n")
if (so) == "1":
    d = input("Domínio: ")
    link1 = ("https://www.google.com/search?q=site:{}".format(d))
    link2 = ("https://www.google.com/search?q=site%3Abr.linkedin.com+intext%3A{}".format(d))
    
    os.system("start chrome {}".format(link1))
    os.system("start chrome {}".format(link2))

if (so) == "2":
    d = input("Domínio: ")
    link1 = ("https://www.google.com/search?q=site:{}".format(d))
    link2 = ("https://www.google.com/search?q=site%3Abr.linkedin.com+intext%3A{}".format(d))
    
    os.system("firefox {}".format(link1))
    os.system("firefox {}".format(link2))
    
    




