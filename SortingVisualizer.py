import pygame
import random
import time

SCREENWIDTH = 1800
SCREENHEIGHT = 1000
DELAY = 0.05

# Pygame Initialization
pygame.init()
pygame.display.init()
w = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
w.fill((0, 0, 0))

# Font Setup
font = pygame.font.SysFont("Arial", 22, True)
padding = 20

# Options Setup
selection = font.render("SelectionSort", True, (255, 0, 0))
quick = font.render("QuickSort", True, (255, 0, 0))
merge_font = font.render("MergeSort", True, (255, 0, 0))
insertion = font.render("InsertionSort", True, (255, 0, 0))
bubble = font.render("BubbleSort", True, (255, 0, 0))
radix = font.render("RadixSort", True, (255, 0, 0))
heap = font.render("HeapSort", True, (255, 0, 0))
selection_text = selection.get_rect()
selection_text.center = (padding // 2 + font.size("SelectionSort")[0] // 2, SCREENHEIGHT - font.size("SelectionSort")[1] // 2)
quick_text = quick.get_rect()
quick_text.center = (padding + selection_text.center[0] + font.size("SelectionSort")[0] // 2 + font.size("QuickSort")[0] // 2, SCREENHEIGHT - font.size("QuickSort")[1] // 2)
merge_text = merge_font.get_rect()
merge_text.center = (padding + quick_text.center[0] + font.size("QuickSort")[0] // 2 + font.size("MergeSort")[0] // 2, SCREENHEIGHT - font.size("MergeSort")[1] // 2)
insertion_text = insertion.get_rect()
insertion_text.center = (padding + merge_text.center[0] + font.size("MergeSort")[0] // 2 + font.size("InsertionSort")[0] // 2, SCREENHEIGHT - font.size("InsertionSort")[1] // 2)
bubble_text = bubble.get_rect()
bubble_text.center = (padding + insertion_text.center[0] + font.size("InsertionSort")[0] // 2 + font.size("BubbleSort")[0] // 2, SCREENHEIGHT - font.size("BubbleSort")[1] // 2)
radix_text = radix.get_rect()
radix_text.center = (padding + bubble_text.center[0] + font.size("BubbleSort")[0] // 2 + font.size("RadixSort")[0] // 2, SCREENHEIGHT - font.size("RadicSort")[1] // 2)
heap_text = heap.get_rect()
heap_text.center = (padding + radix_text.center[0] + font.size("RadixSort")[0] // 2 + font.size("HeapSort")[0] // 2, SCREENHEIGHT - font.size("HeapSort")[1] // 2)
user_range = font.render("Enter range and list size separated by commas (min, max, size) :", True, (255, 0, 0))
user_range_text = user_range.get_rect()
user_range_text.center = (padding + heap_text.center[0] + font.size("HeapSort")[0] // 2 + font.size("Enter range and list size separated by commas (min, max, size) :")[0] // 2, SCREENHEIGHT - font.size("Enter range and list size separated by commas (min, max, size) :")[1] // 2)
user_input = ''
input_box = pygame.Rect(padding + user_range_text.center[0] + font.size("Enter range and list size separated by commas (min, max, size) :")[0] // 2, SCREENHEIGHT - font.size("HeapSort")[1], padding, font.size("HeapSort")[1])
color_active = pygame.Color("green")
color_inactive = pygame.Color("red")
color = color_inactive
active = False
time_font = font.render("Time:", True, (255, 0, 0))
time_text = time_font.get_rect()
time_text.center = (selection_text.center[0], selection_text.center[1] - font.size("SelectionSort")[1] - padding)


# List Utility Functions
def draw_list(w, l):
    largest = max(l)
    mult = (SCREENHEIGHT - font.size("SelectionSort")[1] - padding) / largest
    width = SCREENWIDTH // (len(l) + 1)

    w.fill((0, 0, 0))
    draw_options()

    for i in range(len(l)):
        pygame.draw.line(w, (255, 255, 255), (width * (i+1), 0), (width * (i+1), mult * l[i]), width // 2)

    pygame.display.update()


def generate_list(start, end, n):
    result = []

    for i in range(n):
        result.append(random.randint(start, end))

    return result


# Sorting Algorithms
def selection_sort(l, s):
    time.sleep(DELAY)
    if s == len(l):
        return

    min_index = s

    for i in range(s, len(l)):
        if l[i] < l[min_index]:
            min_index = i

    swap(l, s, min_index)
    draw_list(w, l)
    selection_sort(l, s+1)


def quick_sort(l, s, e):
    time.sleep(DELAY / 2)
    if s < e:
        p = partition(l, s, e)
        quick_sort(l, s, p-1)
        quick_sort(l, p+1, e)


def merge_sort(l, s, e):
    mid = (s+e) // 2
    if s < e:
        merge_sort(l, s, mid)
        merge_sort(l, mid+1, e)
        merge(l, s, mid, mid+1, e)


def insertion_sort(l):
    for i in range(1, len(l)):
        curr = l[i]
        j = i-1
        while j >= 0 and curr < l[j]:
            l[j+1] = l[j]
            draw_list(w, l)
            j -= 1

        l[j+1] = curr
        draw_list(w, l)


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                swap(l, j, j+1)
                draw_list(w, l)


def radix_sort(l):
    largest = max(l)
    num = 1

    while largest // num > 0:
        counting_sort(l, num)
        num *= 10


def counting_sort(l, num):
    result = [0] * len(l)
    count = [0] * 10

    for i in range(len(l)):
        index = l[i] // num
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = len(l) - 1
    while i >= 0:
        index = l[i] // num
        result[count[index % 10] - 1] = l[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(l)):
        time.sleep(DELAY / 6)
        l[i] = result[i]
        draw_list(w, l)


def heap_sort(l):
    for i in range(len(l)//2, -1, -1):
        heapify(l, len(l), i)

    for i in range(len(l) - 1, 0, -1):
        swap(l, 0, i)
        draw_list(w, l)
        heapify(l, i, 0)


# Sorting Helper Functions
def swap(l, a, b):
    tmp = l[a]
    l[a] = l[b]
    l[b] = tmp


def partition(l, s, e):
    i = s
    j = e - 1

    while True:
        while l[i] <= l[e] and i < j:
            i += 1

        while l[j] >= l[e] and i < j:
            j -= 1

        if i == j:
            if l[i] <= l[e]:
                i += 1

            swap(l, i, e)
            draw_list(w, l)
            return i
        else:
            swap(l, i, j)
            draw_list(w, l)


def merge(l, a, b, c, d):
    i = a
    j = c
    tmp = []

    while i <= b and j <= d:
        if l[i] < l[j]:
            tmp.append(l[i])
            i += 1
        else:
            tmp.append(l[j])
            j += 1

    tmp.extend(l[i:c])
    tmp.extend(l[j:d+1])

    for i in range(len(tmp)):
        l[a+i] = tmp[i]
        draw_list(w, l)


def heapify(l, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and l[largest] < l[left]:
        largest = left

    if right < n and l[largest] < l[right]:
        largest = right

    if largest != i:
        swap(l, i, largest)
        draw_list(w, l)
        heapify(l, n, largest)


# Pygame window drawing functions
def draw_options():
    w.blit(selection, selection_text)
    w.blit(quick, quick_text)
    w.blit(merge_font, merge_text)
    w.blit(insertion, insertion_text)
    w.blit(bubble, bubble_text)
    w.blit(radix, radix_text)
    w.blit(heap, heap_text)
    w.blit(user_range, user_range_text)
    height = SCREENHEIGHT - font.size("SelectionSort")[1]
    selection_size = font.size("SelectionSort")
    quick_size = font.size("QuickSort")
    merge_size = font.size("MergeSort")
    insertion_size = font.size("InsertionSort")
    bubble_size = font.size("BubbleSort")
    radix_size = font.size("RadixSort")
    heap_size = font.size("HeapSort")
    pygame.draw.line(w, (255, 0, 0), (0, SCREENHEIGHT - selection_size[1]), (SCREENWIDTH, height))
    pygame.draw.line(w, (255, 0, 0), (1, height), (1, SCREENHEIGHT))
    pygame.draw.line(w, (255, 0, 0), (selection_text.center[0] + selection_size[0] // 2 + padding // 2, height), (selection_text.center[0] + selection_size[0] // 2 + padding // 2, SCREENHEIGHT))
    pygame.draw.line(w, (255, 0, 0), (quick_text.center[0] + quick_size[0] // 2 + padding // 2, height), (quick_text.center[0] + quick_size[0] // 2 + padding // 2, SCREENHEIGHT))
    pygame.draw.line(w, (255, 0, 0), (merge_text.center[0] + merge_size[0] // 2 + padding // 2, height), (merge_text.center[0] + merge_size[0] // 2 + padding // 2, SCREENHEIGHT))
    pygame.draw.line(w, (255, 0, 0), (insertion_text.center[0] + insertion_size[0] // 2 + padding // 2, height), (insertion_text.center[0] + insertion_size[0] // 2 + padding // 2, SCREENHEIGHT))
    pygame.draw.line(w, (255, 0, 0), (bubble_text.center[0] + bubble_size[0] // 2 + padding // 2, height),(bubble_text.center[0] + bubble_size[0] // 2 + padding // 2, SCREENHEIGHT))
    pygame.draw.line(w, (255, 0, 0), (radix_text.center[0] + radix_size[0] // 2 + padding // 2, height), (radix_text.center[0] + radix_size[0] // 2 + padding // 2, SCREENHEIGHT))
    pygame.draw.line(w, (255, 0, 0), (heap_text.center[0] + heap_size[0] // 2 + padding // 2, height), (heap_text.center[0] + heap_size[0] // 2 + padding // 2, SCREENHEIGHT))
    pygame.draw.line(w, (255, 0, 0), (SCREENWIDTH-1, height), (SCREENWIDTH-1, SCREENHEIGHT))
    pygame.display.update()


def draw_textbox():
    w.fill((0, 0, 0))
    pygame.draw.rect(w, color, input_box, 2)
    text_font = font.render(user_input, True, (255, 0, 0))
    w.blit(text_font, (input_box.x + 5, input_box.y))
    input_box.w = max(padding, text_font.get_width() + 10)


def draw_time():
    time_font = font.render("Time:" + str(end - start), True, (255, 0, 0))
    w.blit(time_font, time_text)
    pygame.display.update()


run = True
lmin = 1
lmax = 10000
lnum = 200

while run:
    draw_options()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if selection_text.collidepoint(mouse_pos):
                l = generate_list(lmin, lmax, lnum)
                draw_list(w, l)
                time.sleep(2)
                selection = font.render("SelectionSort", True, (0, 255, 0))
                start = time.time()
                selection_sort(l, 0)
                end = time.time()
                draw_time()
                selection = font.render("SelectionSort", True, (255, 0, 0))
                time.sleep(2)
            elif quick_text.collidepoint(mouse_pos):
                l = generate_list(lmin, lmax, lnum)
                draw_list(w, l)
                time.sleep(2)
                quick = font.render("QuickSort", True, (0, 255, 0))
                start = time.time()
                quick_sort(l, 0, len(l)-1)
                end = time.time()
                draw_time()
                quick = font.render("QuickSort", True, (255, 0, 0))
                time.sleep(2)
            elif merge_text.collidepoint(mouse_pos):
                l = generate_list(lmin, lmax, lnum)
                draw_list(w, l)
                time.sleep(2)
                merge_font = font.render("MergeSort", True, (0, 255, 0))
                start = time.time()
                merge_sort(l, 0, len(l)-1)
                end = time.time()
                draw_time()
                merge_font = font.render("MergeSort", True, (255, 0, 0))
                time.sleep(2)
            elif insertion_text.collidepoint(mouse_pos):
                l = generate_list(lmin, lmax, lnum)
                draw_list(w, l)
                time.sleep(2)
                insertion = font.render("InsertionSort", True, (0, 255, 0))
                start = time.time()
                insertion_sort(l)
                end = time.time()
                draw_time()
                insertion = font.render("InsertionSort", True, (255, 0, 0))
                time.sleep(2)
            elif bubble_text.collidepoint(mouse_pos):
                l = generate_list(lmin, lmax, lnum)
                draw_list(w, l)
                time.sleep(2)
                bubble = font.render("BubbleSort", True, (0, 255, 0))
                start = time.time()
                bubble_sort(l)
                end = time.time()
                draw_time()
                bubble = font.render("BubbleSort", True, (255, 0, 0))
                time.sleep(2)
            elif radix_text.collidepoint(mouse_pos):
                l = generate_list(lmin, lmax, lnum)
                draw_list(w, l)
                time.sleep(2)
                radix = font.render("RadixSort", True, (0, 255, 0))
                start = time.time()
                radix_sort(l)
                end = time.time()
                draw_time()
                radix = font.render("RadixSort", True, (255, 0, 0))
                time.sleep(2)
            elif heap_text.collidepoint(mouse_pos):
                l = generate_list(lmin, lmax, lnum)
                draw_list(w, l)
                time.sleep(2)
                heap = font.render("HeapSort", True, (0, 255, 0))
                start = time.time()
                heap_sort(l)
                end = time.time()
                draw_time()
                heap = font.render("HeapSort", True, (255, 0, 0))
                time.sleep(2)
            elif input_box.collidepoint(mouse_pos):
                active = not active
                if active:
                    color = color_active
                else:
                    color = color_inactive
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    var = user_input.split(",")
                    lmin = int(var[0])
                    lmax = int(var[1])
                    lnum = int(var[2])
                    user_input = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

    draw_textbox()

pygame.quit()
