from treys import Card
from treys import Evaluator

card = Card.new('Qh')
board = [Card.new('Ah'),Card.new('Kd'),Card.new('Jc')]
hand = [Card.new('Qs'),Card.new('Th')]
evaluator = Evaluator()
hand_score = evaluator.evaluate(board, hand)
hand_class = evaluator.get_rank_class(hand_score)
print(hand_score,hand_class ,evaluator.class_to_string(hand_class))

string = '0.01'
zahl = float(string)
print(zahl)