#Sortowanie bąbelkowe:
def bubble_sort(arr):
    n = len(arr)

    #Przejście przez wszystkie elementy.
    for i in range(n-1):
    #range od n tez działa, ale wykona się jeszcze raz niz trzeba

        #Ostatni i jest juz na miejscu
        for j in range(0, n-i-1):
            
            #Przejdz przez tablice od 0 do n-i-1
            #Zamień jezeli znaleziony element jest większy niz nastepny element
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [24,260,12,34,21,56,89,54,32,1,2]


bubble_sort(arr)

print("Sorted array is: ")
for i in range(len(arr)):
    print("%d"% arr[i])

