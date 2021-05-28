<p align="center">
    <img src="https://img.shields.io/github/repo-size/pedro-pauletti/Simulador-Escalonamento-de-Processos">
    <img src="https://img.shields.io/github/downloads/pedro-pauletti/Simulador-Escalonamento-de-Processos/total">
    <img src="https://img.shields.io/github/contributors/pedro-pauletti/Simulador-Escalonamento-de-Processos">
</p>

<p>
<h1 align="center">
    <img title="Memory-Management-Simulator" src="https://user-images.githubusercontent.com/57163905/119591368-d7f34100-bdac-11eb-9857-0e8c066ad841.png" width = "250px"/>
    <h1 align="center">Memory-Management-Simulator</h1>
</h1>
</p>


## 🇺🇸 Memory Management Simulator for educational and didactic purposes, developed for the discipline: Operating Systems l
## 🇧🇷 Simulador de Gerenciamento de Memória com propósito educacional e didático, desenvolvido para a disciplina de Sistemas Operacionais l

<p>
<h1 align="center">
    <img title="Tela Inicial" src="https://user-images.githubusercontent.com/57163905/119929701-635b0680-bf54-11eb-8731-59e9f9bce457.png" width = "900px"/>
</h1>
</p>

<a align="center" href="https://drive.google.com/file/d/1js3r10AU76a8tUtQP33NyzXg8NnIObOg/view?usp=sharing"><img src="https://user-images.githubusercontent.com/57163905/119594233-c496a480-bdb1-11eb-938e-ab395e855c1f.png" width = "400px"></a>


Get to know the project:
=================
<!--ts-->
   * [About](#About)
   * [Interface](#Interface)
   * [How to use?](#How-to-Use)
   * [Algorithms](#Algorithms)
   * [Tools Used](#Tools-Used)
   * [References](#References)
   * [Author](#Author)
<!--te-->

## About 💬
In a computer operating system that uses paging for virtual memory management, page replacement algorithms decide which memory pages to page out, sometimes called swap out, or write to disk, when a page of memory needs to be allocated. Page replacement happens when a requested page is not in memory (page fault) and a free page cannot be used to satisfy the allocation, either because there are none, or because the number of free pages is lower than some threshold.

The idea of creating a simulator is so that students and interested parties can understand and analyze the functioning of the page replacement algorithms and the functioning of the memory management process in a simple, visual and didactic way. All algorithms were developed in Python. The interface was designed using the PySimpleGUI graphic library. To improve the visualization of the simulation the unit of execution time of each process is in seconds. 

## Interface 💻

### Botões:
- ***?*** –> Information about the respective algorithms and the swapping states.
- ***Refresh*** –> Update application with user-defined pages.
- ***ADD*** –> Add the logical address in memory.
- ***Application***:<br>
	– ***Restart***: Restart the application, resetting all values and pages.<br>
	– ***Quit***: Close the application.<br>


## How to use?💡

For the correct functioning of the simulator, the user must fill in the fields *Page Replacement Algorithm*, *Address size*, *Offset size*, *Number of pages* and after that is, click *Refresh* create all pages.
After filling in the fields and updating, the page table and pages will be generated so the user can type N entries in the *Address* field and add them to the memory by clicking on *ADD* and analyzing the behavior of the memory management and page replacement algorithms.

The simulator has an indication of when *Swapping* occurs, the red sphere turns green when this process occurs.
- 🔴 Swapping Occurred     
- 🟢 Swapping Not-Occurred

## Algorithms📝

## FIFO (First-in, First-out)   
The first-in, first-out (FIFO) page replacement algorithm is a low-overhead algorithm that requires little bookkeeping on the part of the operating system. The idea is obvious from the name – the operating system keeps track of all the pages in memory in a queue, with the most recent arrival at the back, and the oldest arrival in front. 
When a page needs to be replaced, the page at the front of the queue (the oldest page) is selected.

* Demonstration:
Sequence of logical addresses added to memory:<br>
00111 -> VPN = 0 / Offset = 7<br>
00010 -> VPN = 0 / Offset = 2<br>
10100 -> VPN = 2 / Offset = 4<br>
11001 -> VPN = 3 / Offset = 1<br>
01110 -> VPN = 1 / Offset = 6<br>
00000 -> VPN = 0 / Offset = 0<br>
<br>
Simulation:<br>

## NRU (Not Recently Used)     
The not recently used (NRU) page replacement algorithm is an algorithm that favours keeping pages in memory that have been recently used. 
This algorithm works on the following principle: when a page is referenced, a referenced bit is set for that page, marking it as referenced. 
At a certain fixed time interval, a timer interrupt triggers and clears the referenced bit of all the pages, so only pages referenced within the current timer interval are marked with a referenced bit. When a page needs to be replaced, the operating system divides the pages into four classes:<br>

3 = referenced, modified<br>
2 = referenced, not modified<br>
1 = not referenced, modified<br>
0 = not referenced, not modified<br>
<br>
* Demonstration:
Sequence of logical addresses added to memory:<br>
00111 -> VPN = 0 / Offset = 7<br>
00010 -> VPN = 0 / Offset = 2<br>
10100 -> VPN = 2 / Offset = 4<br>
00011 -> VPN = 0 / Offset = 3<br>
11001 -> VPN = 3 / Offset = 1<br>
01110 -> VPN = 1 / Offset = 6<br>
01000 -> VPN = 1 / Offset = 0<br>
00000 -> VPN = 0 / Offset = 0<br>
<br>
Simulation:<br>

## Second-chance    
A modified form of the FIFO page replacement algorithm, known as the Second-chance page replacement algorithm, fares relatively better than FIFO at little cost for the improvement.
It works by looking at the front of the queue as FIFO does, but instead of immediately paging out that page, it checks to see if its referenced bit is set. If it is not set, the page is swapped out.

* Demonstration:
Sequence of logical addresses added to memory:<br>
00111 -> VPN = 0 / Offset = 7<br>
10011 -> VPN = 2 / Offset = 3<br>
10100 -> VPN = 2 / Offset = 4<br>
00010 -> VPN = 0 / Offset = 7<br>
11001 -> VPN = 3 / Offset = 1<br>
01110 -> VPN = 1 / Offset = 6<br>
<br>
Simulation:<br>

## Clock    
Clock is a more efficient version of FIFO than Second-chance because pages don''t have to be constantly pushed to the back of the list, but it performs the same general function as Second-Chance.
The clock algorithm keeps a circular list of pages in memory, with the "hand" (iterator) pointing to the last examined page frame in the list.

* Demonstration:
Sequence of logical addresses added to memory:<br>
00111 -> VPN = 0 / Offset = 7<br>
10011 -> VPN = 2 / Offset = 3<br>
10100 -> VPN = 2 / Offset = 4<br>
00010 -> VPN = 0 / Offset = 7<br>
11001 -> VPN = 3 / Offset = 1<br>
01110 -> VPN = 1 / Offset = 6<br>
<br>
Simulation:<br>

## LFU     
The least recently used (LRU) page replacement algorithm, though similar in name to NRU, differs in the fact that LRU keeps track of page usage over a short period of time, while NRU just looks at the usage in the last clock interval.
LRU works on the idea that pages that have been most heavily used in the past few instructions are most likely to be used heavily in the next few instructions too.   
    
* Demonstration:
Sequence of logical addresses added to memory:<br>
00111 -> VPN = 0 / Offset = 7<br>
10100 -> VPN = 2 / Offset = 4<br>
00010 -> VPN = 0 / Offset = 2<br>
11001 -> VPN = 3 / Offset = 1<br>
00000 -> VPN = 0 / Offset = 0<br>
01110 -> VPN = 1 / Offset = 6<br>
<br>
Simulation:<br>
                
## 🛠 Tools Used

- 🔗[Python](https://www.python.org/)
- 🔗[PySimpleGUI](https://pypi.org/project/PySimpleGUI/)

## References ✔

- 🔗[Page replacement algorithm](https://en.wikipedia.org/wiki/Page_replacement_algorithm)
- 🔗[Memória Virtual: Paginação por demanda e Algoritmos de Substituição de páginas](http://escalonamentoprocessos.blogspot.com/2010/12/memoria-virtual-paginacao-por-demanda-e.html#:~:text=O%20algoritmo%20NRU%20(Not%20Recently,durante%20sua%20perman%C3%AAncia%20em%20mem%C3%B3ria)

## Author👨🏼‍💻

<p align="center">
    <a align="center" href="https://pedro-pauletti.github.io/pedropauletti.github.io/"><img src="https://user-images.githubusercontent.com/57163905/116717987-e0c04500-a9af-11eb-835f-81939e7c8bf1.jpeg" width = "150px"></a>
    <h3 align="center">Pedro Pauletti</h3>
</p>
