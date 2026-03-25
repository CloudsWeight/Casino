# blackjack/table.py
import os
from card   import Card
from deck   import Shoe
from player import Player, Dealer

SEPARATOR  = '─' * 60
THICK_LINE = '═' * 60

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Table:
    MIN_BET =  5.0
    MAX_BET = 500.0

    def __init__(self, players: list[Player]):
        self.players = players
        self.dealer  = Dealer()
        self.shoe    = Shoe()
        self.round   = 0

        # running count for display (Hi-Lo)
        self.running_count = 0

    # ─────────────────────────────────────────
    # DISPLAY
    # ─────────────────────────────────────────
    def display_table(self, hide_dealer: bool = True):
        clear()
        print(THICK_LINE)
        print('       ♠  BLACKJACK TRAINER  ♠'.center(60))
        print(f'       Round {self.round}  |  '
              f'Shoe: {self.shoe.decks_remaining} decks left  |  '
              f'RC: {self.running_count:+d}')
        print(THICK_LINE)

        # dealer hand
        print(f'\n  🎩  DEALER')
        if hide_dealer:
            visible = self.dealer.hand.cards
            first   = str(visible[0]) if visible else ''
            hidden  = '[??]' if len(visible) > 1 else ''
            print(f'      {first}  {hidden}')
        else:
            print(f'      {self.dealer.hand.display()}')

        print(f'\n{SEPARATOR}')

        # player hands
        for i, player in enumerate(self.players):
            if not player.is_active:
                status = '💤 sitting out'
            elif player.hand.is_bust:
                status = '💥 BUST'
            elif player.hand.is_blackjack:
                status = '🎉 BLACKJACK'
            elif player.standing:
                status = '✋ standing'
            else:
                status = '🎮 playing'

            print(f'\n  P{i+1}  {player.name:<12} '
                  f'${player.bankroll:<8.0f} '
                  f'Bet: ${player.bet:<6.0f} {status}')

            if player.hand.cards:
                print(f'      {player.hand.display()}')

        print(f'\n{THICK_LINE}\n')

    # ─────────────────────────────────────────
    # BETTING
    # ─────────────────────────────────────────
    def betting_round(self):
        print('\n📍  PLACE YOUR BETS\n')
        for player in self.players:
            if player.bankroll < self.MIN_BET:
                print(f'  {player.name} is out of money — sitting out')
                player.is_active = False
                continue

            while True:
                try:
                    prompt = (f'  {player.name} '
                              f'(${player.bankroll:.0f}) '
                              f'— bet $[{self.MIN_BET:.0f}'
                              f'-{min(self.MAX_BET, player.bankroll):.0f}]: $')
                    amount = float(input(prompt))
                    if amount < self.MIN_BET:
                        print(f'  Minimum bet is ${self.MIN_BET:.0f}')
                        continue
                    if player.place_bet(amount):
                        break
                except ValueError:
                    print('  Enter a valid number')

    # ─────────────────────────────────────────
    # DEALING
    # ─────────────────────────────────────────
    def _update_count(self, card: Card):
        """Hi-Lo running count"""
        if card.face_up:
            if card.value <= 6:
                self.running_count += 1
            elif card.value >= 10:
                self.running_count -= 1

    def deal_card(self, recipient, face_up: bool = True) -> Card:
        card         = self.shoe.deal()
        card.face_up = face_up
        recipient.receive_card(card)
        self._update_count(card)
        return card

    def deal_initial(self):
        """Standard deal — two cards each, dealer second card face down"""
        for _ in range(2):
            for player in self.players:
                if player.is_active:
                    self.deal_card(player)
            face_up = len(self.dealer.hand.cards) == 0
            self.deal_card(self.dealer, face_up=face_up)

    # ─────────────────────────────────────────
    # PLAYER TURN
    # ─────────────────────────────────────────
    def player_turn(self, player: Player):
        while not player.standing and not player.hand.is_bust:
            self.display_table(hide_dealer=True)
            print(f'  👤  {player.name}\'s turn\n')

            # build action menu dynamically
            actions = [('h', 'Hit')]
            actions.append(('s', 'Stand'))
            if player.hand.can_double and player.bankroll >= player.bet:
                actions.append(('d', 'Double Down'))
            if player.hand.can_split and player.bankroll >= player.bet:
                actions.append(('sp', 'Split'))

            menu = '  '.join(f'[{k}] {v}' for k, v in actions)
            print(f'  {menu}\n')

            valid = {k for k, _ in actions}
            choice = input('  Your move: ').strip().lower()

            if choice not in valid:
                print('  Invalid choice\n')
                continue

            if choice == 'h':
                card = self.deal_card(player)
                print(f'\n  Drew {card}')
                if player.hand.is_bust:
                    self.display_table(hide_dealer=True)
                    print(f'  💥  {player.name} busts with {player.hand.score}!\n')
                    input('  Press Enter to continue...')
                    break

            elif choice == 's':
                player.standing = True
                print(f'\n  ✋  {player.name} stands on {player.hand.score}')
                input('  Press Enter to continue...')

            elif choice == 'd':
                player.bankroll -= player.bet
                player.bet      *= 2
                card = self.deal_card(player)
                print(f'\n  doubled down — drew {card} '
                      f'— total bet ${player.bet:.0f}')
                player.standing = True
                if player.hand.is_bust:
                    print(f'  💥  {player.name} busts with {player.hand.score}!')
                input('  Press Enter to continue...')
                break

            elif choice == 'sp':
                self._handle_split(player)
                break

    def _handle_split(self, player: Player):
        """Basic split — move second card to new hand, deal one each"""
        print(f'\n  ✂️   {player.name} splits!\n')
        split_card       = player.hand.cards.pop()
        player.bankroll -= player.bet

        # second hand
        second_hand = Player(f'{player.name}-B', player.bankroll)
        second_hand.bet      = player.bet
        second_hand.bankroll = player.bankroll
        second_hand.hand.add_card(split_card)

        # deal one card to each
        self.deal_card(player)
        self.deal_card(second_hand)

        # insert split hand right after current player
        idx = self.players.index(player)
        self.players.insert(idx + 1, second_hand)

        input('  Press Enter to continue...')

    # ─────────────────────────────────────────
    # DEALER TURN
    # ─────────────────────────────────────────
    def dealer_turn(self):
        # reveal hole card
        for card in self.dealer.hand.cards:
            card.face_up = True
            self._update_count(card)

        self.display_table(hide_dealer=False)
        print('  🎩  Dealer reveals hole card...\n')
        input('  Press Enter...')

        while self.dealer.should_hit():
            card = self.deal_card(self.dealer)
            self.display_table(hide_dealer=False)
            print(f'  🎩  Dealer draws {card} — score: {self.dealer.hand.score}\n')
            input('  Press Enter...')

        if self.dealer.hand.is_bust:
            print(f'  💥  Dealer busts with {self.dealer.hand.score}!\n')
        else:
            print(f'  ✋  Dealer stands on {self.dealer.hand.score}\n')
        input('  Press Enter to see results...')

    # ─────────────────────────────────────────
    # RESULTS
    # ─────────────────────────────────────────
    def settle_bets(self):
        self.display_table(hide_dealer=False)
        print('  📊  RESULTS\n')
        print(SEPARATOR)

        d_score    = self.dealer.hand.score
        dealer_bj  = self.dealer.hand.is_blackjack
        dealer_bust = self.dealer.hand.is_bust

        for player in self.players:
            if not player.is_active:
                continue

            p_score    = player.hand.score
            player_bj  = player.hand.is_blackjack

            # determine outcome
            if player.hand.is_bust:
                result  = 'lose'
                payout  = 0

            elif player_bj and not dealer_bj:
                result  = 'blackjack'
                payout  = player.bet * 2.5    # 3:2 payout

            elif dealer_bj and not player_bj:
                result  = 'lose'
                payout  = 0

            elif dealer_bust:
                result  = 'win'
                payout  = player.bet * 2

            elif p_score > d_score:
                result  = 'win'
                payout  = player.bet * 2

            elif p_score < d_score:
                result  = 'lose'
                payout  = 0

            else:
                result  = 'push'
                payout  = player.bet          # return bet

            player.bankroll += payout
            net = payout - player.bet if result != 'push' else 0

            icons = {
                'blackjack': '🎉',
                'win':       '✅',
                'lose':      '❌',
                'push':      '🤝'
            }
            print(f'  {icons[result]}  {player.name:<12} '
                  f'{result.upper():<10} '
                  f'Net: ${net:+.0f}  '
                  f'Bankroll: ${player.bankroll:.0f}')

        print(f'\n{SEPARATOR}\n')
        input('  Press Enter for next round...')

    # ─────────────────────────────────────────
    # RESET
    # ─────────────────────────────────────────
    def reset_round(self):
        self.dealer.reset()
        for player in self.players:
            # remove split hands, keep originals
            player.reset()
        # clean up any split players that were inserted
        self.players = [p for p in self.players
                        if not p.name.endswith('-B')]

    # ─────────────────────────────────────────
    # MAIN GAME LOOP
    # ─────────────────────────────────────────
    def play(self):
        while True:
            self.round += 1
            self.reset_round()

            # check anyone can still play
            active = [p for p in self.players
                      if p.bankroll >= self.MIN_BET]
            if not active:
                print('\n  💸  All players are broke. Game over!\n')
                break

            self.betting_round()
            self.deal_initial()

            # each player takes their turn
            for player in self.players:
                if player.is_active and not player.hand.is_blackjack:
                    self.player_turn(player)

            self.dealer_turn()
            self.settle_bets()

            # play again?
            again = input('  Play another round? [y/n]: ').strip().lower()
            if again != 'y':
                self._final_standings()
                break

    def _final_standings(self):
        print(f'\n{THICK_LINE}')
        print('  FINAL STANDINGS'.center(60))
        print(THICK_LINE)
        sorted_players = sorted(self.players,
                                key=lambda p: p.bankroll,
                                reverse=True)
        for i, p in enumerate(sorted_players, 1):
            print(f'  {i}. {p.name:<15} ${p.bankroll:.0f}')
        print(f'\n{THICK_LINE}\n')