import tkinter
import random


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:
        for card in range(1, 11):
            name = '{}/{}_{}.{}'.format(extension, str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        for face_card in face_cards:
            name = '{}/{}_{}.{}'.format(extension, face_card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    has_ace = False

    for card in hand:
        card_value = card[0]
        if card_value == 1 and not has_ace:
            has_ace = True
            card_value = 11

        score += card_value

        if score > 21 and has_ace:
            score -= 10

    return score


def deal_card_to_dealer():
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)
    if dealer_score > 21:
        result_text.set('Player wins!')


def deal_card_to_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set('Dealer wins!')


mainWindow = tkinter.Tk()

mainWindow.title("Blackjack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

# frame for cards
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# another frame for cards
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_card_to_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_card_to_player)
player_button.grid(row=0, column=1)

cards = []
load_images(cards)

print(cards)

# create deck and shuffle
deck = list(cards)

random.shuffle(deck)

# dealer and player hands

dealer_hand = []
player_hand = []

mainWindow.mainloop()
