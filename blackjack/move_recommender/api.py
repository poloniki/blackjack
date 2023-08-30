from fastapi import FastAPI
from blackjack.move_recommender.recommender import Hand, SCORE_TABLE

app = FastAPI()





@app.get("/")
def hello():
    return{"response":"hellow"}


@app.post("/predict_move")
def predict(input_d:dict = {'dealer': [], 'player':[]}):
    # input_d = {'dealer': [7], 'player':[10,'A']}
    player_cards = input_d['player']
    dealer_card = SCORE_TABLE[input_d['dealer'][0]]
    player_hand = Hand(player_cards)
    player_score = player_hand.get_score()
    if player_hand.get_score() > 21:
            rec = 'You busted!'
    elif player_hand.is_blackjack():
            rec = 'Blackjack'
    else:
        rec = player_hand.recommend(dealer_card)
    return {'next_move': rec, 'player_hand': player_score, 'dealer_hand': dealer_card}
