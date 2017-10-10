import requests
import xmltodict
import datetime
import dateutil.parser
import tkinter

nsApiAuth = ('noahlvb@gmail.com', 'vgP9zOsCz1088_c-aQtaIv9BZG0aQ8ftcz9JvA_bxLnnoDSxo2OwmQ')
nsApiURL = 'http://webservices.ns.nl/ns-api-avt?station='

departureLabels = list()

def renderDepartureTimes():
    for label in departureLabels: label.destroy()

    response = requests.get(nsApiURL + stationInput.get(), auth=nsApiAuth)
    response = xmltodict.parse(response.text)
    for index, trein in enumerate(response['ActueleVertrekTijden']['VertrekkendeTrein']):
        if index <= 10:
            time = dateutil.parser.parse(trein['VertrekTijd']).strftime('%H:%M')
            departureText = 'De {} naar {} van {}({}) vertrekt vanaf spoor {}'.format(trein['TreinSoort'], trein['EindBestemming'], time, trein['RitNummer'], trein['VertrekSpoor']['#text'])
            departureLabel = tkinter.Label(master=root, text=departureText)
            departureLabel.grid(row=2+index, column=0, sticky=tkinter.W)
            departureLabels.append(departureLabel)

root = tkinter.Tk()
tkinter.Label(master=root, text='Voer een stations afkorting in voor de vertrektijden', background='yellow').grid(row=0, column=0)
stationInput = tkinter.Entry(master=root)
stationInput.grid(row=1, column=0)
tkinter.Button(master=root, text='Vetrektijden ophalen', command=renderDepartureTimes).grid(row=1, column=1)

root.mainloop()
