def list_to_dict(lista,listb):
    if len(lista) == len(listb):
        Warna =zip(lista, listb)
        print(dict(Warna))
    else:
        return print("kedua list tidak dalam jumlah yang sama")
    
list_to_dict(['red', 'green', 'blue',],['#FF0000','#008000', '#0000FF'])
list_to_dict(['red', 'green', 'blue','Merah'],['#FF0000','#008000', '#0000FF'])