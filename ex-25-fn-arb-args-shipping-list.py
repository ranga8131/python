# This program prints shipping list using arbitrary arguments


def shipping_list(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()    
    print(f"#{kwargs.get('flat')} {kwargs.get('street')},")
    print(f"{kwargs.get('city')}-{kwargs.get('pin')}")    

shipping_list("Mr.", "Rangaraj", "Nandhagopal", flat= "02", street= "Lingappan Street", city="Kanchipuram", pin="631502")