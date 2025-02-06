from timeit import timeit
import pandas as pd
class Song:
    def __init__(self, id, playtime, artist, name):
        self.id = id
        self.playtime = playtime
        self.artist = artist
        self.name = name
    def __lt__(self, other):
        if isinstance(other, Song):
            return self.artist<other.artist
        else:
            return self.artist<other
    def __str__(self):
        return f'låt-id:{self.id}, speltid:{self.playtime}, artistnamn:{self.artist}, låtnamn:{self.name}'
def readfile(filename:str):
    songs = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if "<SEP>" not in line:
                continue
            count = 0
            trackid = ""
            playtime = ""
            artist_name = ""
            song_name = ""
            for info in line.split('<SEP>'):
                info = info.strip()
                match count:
                    case 0:
                        trackid = info
                    case 1:
                        playtime = info
                    case 2:
                        artist_name = info
                    case 3:
                        song_name = info
                count+=1
            if count > 1:
                songs.append(Song(trackid, playtime, artist_name, song_name))
    return songs
def linsok(list, target):
    '''O(n), söker lijärt efter ett värde'''
    for index, element in enumerate(list):
        if element.artist == target:
            return index
        
    return -1

def binary_search(numbers_list, number_to_find):
    '''O(log(n)), söker genom en sorterad lista'''
    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = (left_index + right_index) // 2

    while left_index <= right_index:
        mid_number = numbers_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        elif mid_number < number_to_find:
            left_index = mid_index+1
        else:
            right_index = mid_index-1
        mid_index = (left_index + right_index) // 2
    return -1
def bubble_sort(elements):
    '''O(n^2), sorterar från minst till störst (Space O(1))'''
    for k in range(len(elements)-1):
        swapped = False
        for i in range(len(elements)-1-k):
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                swapped = True
        if not swapped:
            break
    return elements

def merge_sort(elements):
    '''O(logn * n), space O(n)'''
    n = len(elements)
    if n == 1:
        return elements
    m = n//2
    L = elements[:m]
    R = elements[m:]

    L = merge_sort(L)
    R = merge_sort(R)
    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)
    sorted_elements = [0] * n
    i = 0
    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_elements[i] = L[l]
            l+=1
        else:
            sorted_elements[i] = R[r]
            r+=1
        i+=1
    while l < L_len:
        sorted_elements[i] = L[l]
        l += 1
        i += 1
    while r < R_len:
        sorted_elements[i] = R[r]
        r += 1
        i += 1
    return sorted_elements
def test_bubblesort(lista):
    '''Testar bubblesort metoden'''
    n = len(lista)
    print(f'Antal element: {n}')
    linjtid = timeit(stmt = lambda: bubble_sort(lista), number = 1)
    return round(linjtid, 4)
def test_mergesort(lista):
    '''Testar mergesort metoden'''
    n = len(lista)
    print(f'Antal element: {n}')
    linjtid = timeit(stmt = lambda: merge_sort(lista), number = 1)
    return round(linjtid, 4)
def test_linsok(lista):
    '''Testar linsok metoden'''
    n = len(lista)
    print(f'Antal element: {n}')
    sista = lista[n-1]
    testartist = sista.artist
    testartist = ""
    linjtid = timeit(stmt = lambda: linsok(lista, testartist), number = 100)
    return round(linjtid, 4)
def test_binary_search(lista):
    '''Testar binärsökmetoden'''
    n = len(lista)
    print(f'Antal element: {n}')
    linjtid = timeit(stmt = lambda: binary_search(lista, ""), number = 100)
    return round(linjtid, 4)
def test_hash_search(lista):
    '''Testar att kolla upp värdet i en hashtabell'''
    n = len(lista)
    print(f'Antal element: {n}')
    artist = lista[-1].artist
    hash_map = {song.artist:song for song in lista}
    linjtid = timeit(stmt = lambda: hash_map[artist], number = 100)
    return round(linjtid, 4)
if __name__ == '__main__':
    whole = readfile("unique_tracks.txt")
    sorted_whole = merge_sort(whole)
    intervals_search = [250000, 500000, 1000000]
    timetable_search = {"Linjärsökning":{},"Binärsökning":{},"Sökning i hashtabell":{}}
    for interval in intervals_search:
        for key, value in timetable_search.items():
            match key:
                case "Linjärsökning":
                    value[f'n = {str(interval)}'] = test_linsok(whole[:interval])
                case "Binärsökning":
                    value[f'n = {str(interval)}'] = test_binary_search(whole[:interval])
                case "Sökning i hashtabell":
                    value[f'n = {str(interval)}'] = test_hash_search(whole[:interval])
    
    intervals_sort = [100, 1000, 10000]
    timetable_sort = { "Långsam sorteringsmetod:":{},"Snabbare sorteringsmetod:":{}}
    for interval in intervals_sort:
        for key, value in timetable_sort.items():
            match key:
                case "Långsam sorteringsmetod:":
                    value[f'n = {str(interval)}'] = test_bubblesort(whole[:interval])
                case "Snabbare sorteringsmetod:":
                    value[f'n = {str(interval)}'] = test_mergesort(whole[:interval])
    print(timetable_search)
    print(timetable_sort)
    df_search = pd.DataFrame(timetable_search)
    df_sort = pd.DataFrame(timetable_sort)
    with pd.ExcelWriter("tidtabeller.xlsx") as writer:
        df_search.to_excel(writer, sheet_name="Sökning")
        df_sort.to_excel(writer, sheet_name="Sortering")
    
    
    
            
                    