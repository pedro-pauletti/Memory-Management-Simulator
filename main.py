import PySimpleGUI as sg
import visual as vs
import datetime
import random
import math

# Create the window
window = sg.Window('Memory Management Simulator', vs.layout, default_element_size=(15, 1), auto_size_text=False, finalize=True, icon = 'assets\logo.ico')
data_pages = [['', '']]
headings_pages = ["Physical Memory"]
data_pageTable = [['', '', '', '', '', '']]
numpages = 0
data_hd = []
hd = []
page_list = []
page_list_hd = []
count = 0
reset = 0

 
def resetR():
    for i in range(len(data_pageTable)):
      if data_pageTable[i][3] != '':
        data_pageTable[i][3] = 0
        page_list[data_pageTable[i][0]].reference = 0

    window['page-table'].update(values = data_pageTable)

 

class Page:
    def __init__(self):
        self.id = ''
        self.data = []
        self.time = 0
        self.reference = 0
        self.modified = 0
        self.lastAcess = 0


def SetLED(window, key, color):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 17, fill_color=color, line_color=color)

def delLED(window, key):
    graph = window[key]
    graph.erase()

def fifo(page_list):
    smallerTime = page_list[0].time
    pageToRemove = 0

    for i in range(len(page_list)):
        
        if(page_list[i].time < smallerTime):
            smallerTime = page_list[i].time
            pageToRemove = i
    
    return pageToRemove

def lru(page_list):
    smallerTime = page_list[0].lastAcess
    pageToRemove = 0
    print(smallerTime)

    for i in range(len(page_list)):
        if(page_list[i].lastAcess < smallerTime):
            smallerTime = page_list[i].lastAcess
            pageToRemove = i
    
    #print(smallerTime)
    return pageToRemove

def secondChance(page_list):
    smallerTime = page_list[0].time
    pageToRemove = 0

    while True:
        for i in range(len(page_list)):
            
            if(page_list[i].time < smallerTime):
                smallerTime = page_list[i].time
                pageToRemove = i
        
        if page_list[pageToRemove].reference == 0:
            break
        else:
            page_list[pageToRemove].reference = 0
            page_list[pageToRemove].time = datetime.datetime.now().time()
        

    return pageToRemove

def clock(page_list):
    smallerTime = -1

    for i in range(len(page_list)):
        print(page_list[i].reference)
        if(page_list[i].reference == 0):
            smallerTime = page_list[i].time
            pageToRemove = i
            break

    if smallerTime == -1:
        smallerTime = page_list[0].time
        pageToRemove = -1

    
    while True:
        for i in range(len(page_list)):
            
            if(page_list[i].time < smallerTime and page_list[i].reference == 0):
                smallerTime = page_list[i].time
                pageToRemove = i

        if (pageToRemove != -1):
            for i in range(len(page_list)):
                if page_list[i].time < page_list[pageToRemove].time:
                    page_list[i].reference = 0

            break
        else:
            resetR()
    
    return pageToRemove


def nru(page_list):
    lowerClass = 3
    pagesClasses = []

    for i in range(len(page_list)):
        if (page_list[i].modified == 0 and page_list[i].reference == 0):
            pagesClasses.append([i, 0])
        elif (page_list[i].modified == 1 and page_list[i].reference == 0):
            pagesClasses.append([i, 1])
        elif (page_list[i].modified == 0 and page_list[i].reference == 1):
            pagesClasses.append([i, 2])
        else:
            pagesClasses.append([i, 3])


    for i in range(len(pagesClasses)):
        if pagesClasses[i][1] <= lowerClass:
            lowerClass = pagesClasses[i][1]

    print('lower class:', lowerClass)

    
    for i in range(len(pagesClasses)):
        if i == len(pagesClasses):
            break
        if pagesClasses[i][1] != lowerClass:
            del(pagesClasses[i])
            print(pagesClasses)


    print(pagesClasses)
    return random.choice(pagesClasses)[0]


def swapping(vpn, displacement, page_list):
    SetLED(window, 'led-swap', 'green')

    hd = False
    for i in range(len(data_hd)):
        if data_hd[i][0] == vpn:
            hd = True
            hdIndex = i

    if values['algorithms'] == 'FIFO':
        pageToRemove = fifo(page_list)
    if values['algorithms'] == 'NRU':
        pageToRemove = nru(page_list)
    if values['algorithms'] == 'Second-chance':
        pageToRemove = secondChance(page_list)
    if values['algorithms'] == 'LRU':
        pageToRemove = lru(page_list)
    if values['algorithms'] == 'Clock':
        pageToRemove = clock(page_list)

    print('pageToRemove:', pageToRemove)    

    page_list_hd.append(page_list[pageToRemove])
    data_hd.append([page_list[pageToRemove].id, page_list[pageToRemove].data])
    window['table-hd'].update(values = data_hd)

    data_pageTable[page_list[pageToRemove].id][1] = 0
    data_pageTable[page_list[pageToRemove].id][3] = 0
    data_pageTable[page_list[pageToRemove].id][4] = 0

    if(hd == True):
        print('SWAPPING HD->RAM')
        page_list[pageToRemove].data = data_hd[hdIndex][1] 
        print(page_list[pageToRemove].data)
        page_list[pageToRemove].data[displacement] = ['■■■■■■■■■■■']
        page_list[pageToRemove].time = datetime.datetime.now().time()
        page_list[pageToRemove].lastAcess = datetime.datetime.now().time()
        del(data_hd[hdIndex])
    else:
        newPage = Page()
        newPage.id = vpn
        for _ in range((2 ** values['input-offset'])):
            newPage.data.append([''])
        newPage.data[displacement] = ['■■■■■■■■■■■']
        newPage.time = datetime.datetime.now().time() 
        newPage.modified = 1
        newPage.reference = 1
        newPage.lastAcess = datetime.datetime.now().time() 
        page_list[pageToRemove] = newPage
   

    window['table-hd'].update(values = data_hd)
    window[f'table-pages-{pageToRemove}'].update(values = page_list[pageToRemove].data)
    data_pageTable[vpn] = [pageToRemove, 1, page_list[pageToRemove].time, page_list[pageToRemove].reference, page_list[pageToRemove].modified, page_list[pageToRemove].lastAcess]
    window['page-table'].update(values = data_pageTable)


def fillTable(address, offset, page_list, data_pageTable):


    vpn = int(address[0:(len(address)-offset)], 2)
    displacement = int(address[(len(address)-offset):], 2)

   
    for i in range(len(page_list)):
        if page_list[i].id == vpn: #se vpn ja foi alocado
            if page_list[i].data[displacement] == ['■■■■■■■■■■■']:
                page_list[i].reference = 1
                page_list[i].lastAcess = datetime.datetime.now().time()
                data_pageTable[vpn] = [i, 1, page_list[i].time, page_list[i].reference, page_list[i].modified, datetime.datetime.now().time()]
            else:
                page_list[i].id = vpn
                page_list[i].data[displacement] = ['■■■■■■■■■■■']
                page_list[i].modified = 1
                page_list[i].reference = 1
                page_list[i].lastAcess = datetime.datetime.now().time()
                window[f'table-pages-{i}'].update(values = page_list[i].data)
                data_pageTable[vpn] = [i, 1, page_list[i].time, page_list[i].reference, page_list[i].modified, datetime.datetime.now().time()]
            window['page-table'].update(values = data_pageTable)
            break
        else:
            if page_list[i].id == '': #se o vpn ainda nao foi alocado
            
                page_list[i].id = vpn
                page_list[i].time = datetime.datetime.now().time() 
                page_list[i].lastAcess = datetime.datetime.now().time() 
                page_list[i].data[displacement] = ['■■■■■■■■■■■']
                page_list[i].modified = 1
                page_list[i].reference = 1
                window[f'table-pages-{i}'].update(values = page_list[i].data)
                data_pageTable[vpn] = [i, 1, page_list[i].time, page_list[i].reference, page_list[i].modified, page_list[i].lastAcess]
                window['page-table'].update(values = data_pageTable)
                break
            else:
                if i == (len(page_list)-1):
                    print('SWAPPING RAM->HD')
                    swapping(vpn,displacement,page_list)
       



while True:

    event, values = window.read()

    if count == 3:
        resetR()
        count = 0

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'Restart':
  
        import os 
        os.startfile("main.py")

        SetLED(window, 'led-swap', 'red')
        data_pages = []
        for i in range(numpages):
           window[f'table-pages-{i}'].update(values = data_pages) 

        data_pageTable = []
        numpages = 0
        data_hd = []
        hd = []
        page_list = []
        page_list_hd = []
        window['page-table'].update(values = data_pageTable)
        window['table-hd'].update(values = data_hd)



    if event == 'add':
        SetLED(window, 'led-swap', 'red')
        fillTable(values['input-address'], values['input-offset'], page_list, data_pageTable)
        count += 1

    
    
    if event == 'refresh':

        window['page-table'].update(num_rows = 2 ** (values['input-sizeAddress'] - values['input-offset']))
        for _ in range((2 ** (values['input-sizeAddress'] - values['input-offset'])-1)):
            data_pageTable.append(['', '', '', '', '', ''])
        window['page-table'].update(values = data_pageTable)

        
        for i in range(values['input-pages']):
            page_list.append(Page())

            for _ in range((2 ** values['input-offset'])):
                page_list[i].data.append([''])

            window.extend_layout(window['pages'], [[sg.Text(f'Page {numpages}'), sg.Table(values=page_list[i].data, headings=headings_pages,
                                    auto_size_columns=False,
                                    display_row_numbers=True,
                                    justification='center',
                                    def_col_width = 12,
                                    num_rows= 2 ** values['input-offset'],
                                    key=f'table-pages-{numpages}',
                                    row_height=25) ],
                        ])
            
            numpages += 1
            
   

    if event == 'help':
        if values['algorithms'] == 'FIFO':
            sg.popup('Algorithm FIFO (First-in, First-out)',      
                'The first-in, first-out (FIFO) page replacement algorithm is a low-overhead algorithm that requires little bookkeeping on the part of the operating system.', 
                'The idea is obvious from the name – the operating system keeps track of all the pages in memory in a queue, with the most recent arrival at the back, and the oldest arrival in front.', 
                'When a page needs to be replaced, the page at the front of the queue (the oldest page) is selected.',
                ) 
        
        if values['algorithms'] == 'NRU':
            sg.popup('Algorithm NRU (Not Recently Used)',      
                    'The not recently used (NRU) page replacement algorithm is an algorithm that favours keeping pages in memory that have been recently used.', 
                    'This algorithm works on the following principle: when a page is referenced, a referenced bit is set for that page, marking it as referenced.',  
                ) 

        if values['algorithms'] == 'Second-chance':
           sg.popup('Algorithm Second-chance',      
                    'A modified form of the FIFO page replacement algorithm, known as the Second-chance page replacement algorithm, fares relatively better than FIFO at little cost for the improvement.', 
                    'It works by looking at the front of the queue as FIFO does, but instead of immediately paging out that page, it checks to see if its referenced bit is set. If it is not set, the page is swapped out.',
                ) 

        if values['algorithms'] == 'Clock':
            sg.popup('Algorithm Clock',      
                'Clock is a more efficient version of FIFO than Second-chance because pages don''t have to be constantly pushed to the back of the list, but it performs the same general function as Second-Chance.',
                'The clock algorithm keeps a circular list of pages in memory, with the "hand" (iterator) pointing to the last examined page frame in the list.', 
                ) 

        if values['algorithms'] == 'LRU':
            sg.popup('Algorithm LFU',      
                'The least recently used (LRU) page replacement algorithm, though similar in name to NRU, differs in the fact that LRU keeps track of page usage over a short period of time, while NRU just looks at the usage in the last clock interval.', 
                'LRU works on the idea that pages that have been most heavily used in the past few instructions are most likely to be used heavily in the next few instructions too.',    
                )   
 
    if event == 'help-swapping':
        sg.popup('RED - Swapping Occurred',      
                'GREEN - Swapping Not-Occurred',
                ) 
    

