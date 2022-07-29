sozluk = {
    "a":15,
    "b":9,
    "c":56,
    "ç":45,
    "d":58,
    "e":89,
    "f":78,
    "g":87,
    "ğ":11,
    "h":55,
    "ı":78,
    "i":83,
    "j":12,
    "k":41,
    "l":40,
    "m":36,
    "n":50,
    "o":16,
    "ö":12,
    "p":88,
    "r":65,
    "s":70,
    "ş":60,
    "t":20,
    "u":59,
    "ü":69,
    "v":19,
    "y":18,
    "z":17,
    ".":22,
    ",":27,
    " ":28,
    "1":24,
    "2":39,
    "3":31,
    "4":35,
    "5":32,
    "6":30,
    "7":46,
    "8":48,
    "9":72,
    "/":73,
    "'":62,
    "-":59,
    "_":53,
    "x":10,
    "0":99,
    "w":90
    }

sec = input("Şifrelemek için = 1 -- Çözmek için -- 2 yaz.")

cozum = []
cozumsayilar = ()
sifrelist = []
sonhali = []

def get_key(val):
    for key, value in sozluk.items():
        if val == value:
            return key


if sec == "1":
    yazi = input("Şifrelenecek metini Gir: ")
    yazi = yazi.lower()
    harfler = list(yazi)
    for i in harfler:
        try:
            sonhali.append(sozluk[i])
        except:
            continue
    print(sonhali)
elif sec == "2":
    son = "-"
    while True:
        sifre = input("Şifreyi Gir : ")
        sifre = sifre.replace(" ", "")
        sifrelist = sifre.split(",")
        for i in sifrelist:
            i = int(i)
            son = son + get_key(i)

        else:
            break
    print(son)

    
    
    
    
