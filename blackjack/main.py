# main.py
from simulation import SimConfig, run_simulation
from report     import print_report

def main():
    print('\n  🃏  BLACKJACK SIMULATOR\n')

    cfg = SimConfig(
        num_games          = 200,
        num_decks          = 2,
        starting_bankroll  = 500.0,
        base_bet           = 10.0,
        min_bet            = 10.0,
        max_bet            = 2000.0,
        penetration        = 0.75,
        num_other_players  = 5,
    )

    results = run_simulation(cfg)
    print_report(results)

if __name__ == '__main__':
    main()