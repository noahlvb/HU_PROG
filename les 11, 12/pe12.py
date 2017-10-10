import requests
import xmltodict
import datetime
import dateutil.parser
import tkinter
import time
import sys

nsApiAuth = ('noahlvb@gmail.com', 'vgP9zOsCz1088_c-aQtaIv9BZG0aQ8ftcz9JvA_bxLnnoDSxo2OwmQ')
nsApiURL = 'http://webservices.ns.nl/ns-api-avt?station='

stationCode = str(sys.argv[1])
stationSpoor = int(sys.argv[2])

# Defining the root window
root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()

def renderMain():
    for child in root.winfo_children():
        child.destroy()

    # Defining the Frames
    topFrame = tkinter.Frame(master=root)
    topFrame.configure(background='white')
    topFrame.grid(row=0, sticky='nsew')
    midFrame = tkinter.Frame(master=root)
    midFrame.configure(background='white')
    midFrame.grid(row=1, sticky='nsew')
    bottomFrame = tkinter.Frame(master=root)
    bottomFrame.configure(background='blue')
    bottomFrame.grid(row=2, sticky='nsew')

    # configure row sizes of root window
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=2)
    root.rowconfigure(1, weight=10)
    root.rowconfigure(2, weight=3)

    topFrameTime = tkinter.Label(master=topFrame)
    topFrameTime.configure(foreground='blue', background='white', font=("Helvetica", 82))
    topFrameTime.grid(row=0, column=0, sticky='w')
    topFrameTimeDelay = tkinter.Label(master=topFrame)
    topFrameTimeDelay.configure(foreground='red', background='white', font=("Helvetica", 72))
    topFrameTimeDelay.grid(row=0, column=1, sticky='w')
    topFrameType = tkinter.Label(master=topFrame)
    topFrameType.configure(foreground='blue', background='white', font=("Helvetica", 82))
    topFrameType.grid(row=0, column=2, sticky='e')

    topFrame.columnconfigure(0, weight=1)
    topFrame.columnconfigure(1, weight=1)
    topFrame.columnconfigure(2, weight=1)

    midFrameDestination = tkinter.Label(master=midFrame)
    midFrameDestination.configure(foreground='blue', background='white', font=('Helvetica', 64))
    midFrameDestination.grid(sticky='w')
    midFrameDestinationSecond = tkinter.Label(master=midFrame)
    midFrameDestinationSecond.configure(foreground='blue', background='white', font=('Helvetica', 32))
    midFrameDestinationSecond.grid(sticky='w')

    bottomFrame.columnconfigure(0, weight=1)
    bottomFrame.rowconfigure(0, weight=1)
    bottomFrame.rowconfigure(1, weight=1)

    globals().update(locals())

def renderNoBording():
    for child in root.winfo_children():
        child.destroy()

    root.rowconfigure(0, weight=1)
    root.configure(background='white')

    noBordingFrame = tkinter.Frame(master=root)
    noBordingFrame.configure(background='white')
    noBordingFrame.grid(row=0, column=0)

    noBordingLabel = tkinter.Label(master=noBordingFrame, text='Niet instappen!')
    noBordingLabel.configure(background='white', foreground='blue', font=('Helvetica', 64))
    noBordingLabel.grid(row=0, column=0, sticky='w')
    noBordingLabelEnglish = tkinter.Label(master=noBordingFrame, text='Do not board!')
    noBordingLabelEnglish.configure(background='white', foreground='blue', font=('Helvetica', 32))
    noBordingLabelEnglish.grid(row=1, column=0, sticky='w')

    noBordingFrame.rowconfigure(0, weight=1)

    globals().update(locals())

def renderNext(index, trein):
    bottomFrameNext = tkinter.Label(master=bottomFrame)
    bottomFrameNext.configure(foreground='white', background='blue', font=('Helvetica', 32))
    bottomFrameNext.grid(row=index-1, sticky='w')

    departureTime = dateutil.parser.parse(trein['VertrekTijd']).strftime('%H:%M')
    vetragingstijd = ''
    try:
        if trein['VertrekVertraging']:
            vetragingstijd = ' +' + trein['VertrekVertraging'][2:-1]
    except:
        pass
    bottomFrameNext['text'] = departureTime + ' ' + trein['TreinSoort'] + ' ' + trein['EindBestemming'] + vetragingstijd

def render():
    response = requests.get(nsApiURL + stationCode, auth=nsApiAuth)
    response = xmltodict.parse(response.text)

    trainsOnThisTrack = list()
    for index, trein in enumerate(response['ActueleVertrekTijden']['VertrekkendeTrein']):
        try:
            if trein['VertrekSpoor']['#text'] == str(stationSpoor):
                trainsOnThisTrack.append(trein)
        except:
            pass

    if len(trainsOnThisTrack) > 0:
        renderMain()
    else:
        renderNoBording()

    for index, trein in enumerate(trainsOnThisTrack):
        if index == 0:
            departureTime = dateutil.parser.parse(trein['VertrekTijd']).strftime('%H:%M')

            try:
                topFrameTime['text'] = departureTime
                topFrameType['text'] = trein['TreinSoort']
                midFrameDestination["text"] = trein['EindBestemming']
                midFrameDestinationSecond['text'] = 'Via ' + trein['RouteTekst']
                if trein['VertrekVertraging']:
                    topFrameTimeDelay['text'] = '+' + trein['VertrekVertraging'][2:-1] + ' Vertraging'
            except:
                pass
        elif index > 0 and index <= 2:
            renderNext(index, trein)

    root.after(15000, render)

root.after(100, render)
root.mainloop()
