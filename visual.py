import PySimpleGUI as sg
sg.theme('Dark Grey 1')

def LEDIndicator(key=None, metadata = None, radius=30):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key, metadata = metadata)



numProcesso = 1
data1 = []
data2 = []
data3 = []
filas = [['', '', '']]
headings1 = ["Page", "Active", "Time", "R", "M", "Last Acess"]
headings2 = ["Physical Memory"]
headings3 = ["VPN (Decimal)"]

menu = [['&Application', ['&Restart','&Quit']],
        ['&Help', ['&About']] ]

left_col = [
            [sg.Text('Page Replacement Algorithm:', size=(25,1)), sg.Combo(values=('FIFO', 'NRU', 'Second-chance', 'Clock', 'LRU'), default_value='FIFO', key = 'algorithms'), sg.Button('❓', key = 'help')],
            [sg.Text('Address size (bits):', size=(20,1), key='sizeAddress'), sg.Spin([i for i in range(0,999)], initial_value=1, size=(5, 5), key = 'input-sizeAddress')],
            [sg.Text('Offset size:', size=(20,1), key='offset'), sg.Spin([i for i in range(0,999)], initial_value=1, size=(5, 5), key = 'input-offset')],
            [sg.Text('Number of pages:', size=(20,1), key='num-pages'), sg.Spin([i for i in range(0,999)], initial_value=1, size=(5, 5), key = 'input-pages')],
            [sg.Button('Refresh', key='refresh')],
            [sg.HorizontalSeparator()],
            [sg.Text('Address: (Binary)', size=(20,1), key='address'), sg.Input(key='input-address'), sg.Button('ADD', key='add')],
            [sg.HorizontalSeparator()],
            [sg.Text('PAGE TABLE', font=("Helvetica", 11))],
            [sg.Table(values=data1, headings=headings1,
                                auto_size_columns=False,
                                display_row_numbers=True,
                                justification='center',
                                num_rows= 6,
                                key='page-table',
                                row_height=25)],
            ]
mid_col = [
            [sg.Text('Swapping:', font=("Helvetica", 11)), LEDIndicator('led-swap'), sg.Button('❓', key = 'help-swapping') ],

            [sg.HorizontalSeparator()],
            [sg.Text('HD', font=("Helvetica", 11))],
            [sg.Table(values=data3, headings=headings3,
                                auto_size_columns=False,
                                display_row_numbers=False,
                                justification='center',
                                num_rows= 6,
                                key='table-hd',
                                row_height=25)],
]

right_col =[[sg.Frame('PAGES',[[]], key='pages', font=("Helvetica", 13),)],
            ]


# Define the window's contents
layout = [
        [sg.Menu(menu, key='-MENU-')],
        [sg.Column(left_col, element_justification='c'), sg.VSeperator(),sg.Column(mid_col, element_justification='c'), sg.VSeperator(),sg.Column(right_col, element_justification='c')]
            ]

