# blackjack/report.py
import json
import os
import statistics
from game_stats import GameStats
from simulation import SimConfig

THICK = '═' * 70
THIN  = '─' * 70

def fc(v):  return f'${v:>9,.2f}'
def fp(v):  return f'{v*100:>5.1f}%'
def fi(v):  return f'{v:>8,}'


def _aggregate(games: list[GameStats], cfg: SimConfig) -> dict:
    """Aggregate list of GameStats into summary numbers"""
    n               = len(games)
    finals          = [g.end_bankroll    for g in games]
    peaks           = [g.peak_bankroll   for g in games]
    profits         = [g.net_profit      for g in games]
    hands_per_game  = [g.total_hands     for g in games]

    return {
        'n':               n,
        'avg_final':       statistics.mean(finals),
        'med_final':       statistics.median(finals),
        'std_final':       statistics.stdev(finals) if n > 1 else 0,
        'best':            max(finals),
        'worst':           min(finals),
        'avg_peak':        statistics.mean(peaks),

        'profitable':      sum(1 for f in finals if f > cfg.starting_bankroll),
        'broke':           sum(1 for f in finals if f <= 0),
        'hit_1k':          sum(1 for p in peaks if p >= 1000),
        'hit_2k':          sum(1 for p in peaks if p >= 2000),
        'hit_4k':          sum(1 for p in peaks if p >= 4000),

        'avg_hands':       statistics.mean(hands_per_game),
        'total_hands':     sum(g.total_hands    for g in games),
        'total_wins':      sum(g.wins           for g in games),
        'total_losses':    sum(g.losses         for g in games),
        'total_pushes':    sum(g.pushes         for g in games),
        'total_busts':     sum(g.busts          for g in games),
        'total_bjs':       sum(g.blackjacks     for g in games),

        'total_soft':      sum(g.soft_hands     for g in games),
        'total_hard':      sum(g.hard_hands     for g in games),
        'total_pairs':     sum(g.pairs_dealt    for g in games),
        'total_doubles':   sum(g.doubles_taken  for g in games),
        'total_i18':       sum(g.i18_deviations for g in games),

        'avg_accuracy':    statistics.mean(g.accuracy  for g in games),
        'avg_win_rate':    statistics.mean(g.win_rate  for g in games),

        'hands_neg':       sum(g.hands_negative  for g in games),
        'hands_p1':        sum(g.hands_at_plus1  for g in games),
        'hands_p2':        sum(g.hands_at_plus2  for g in games),
        'hands_p3':        sum(g.hands_at_plus3  for g in games),

        'avg_max_bet':     statistics.mean(g.max_bet for g in games),
        'avg_wagered':     statistics.mean(g.total_wagered for g in games),
    }


def print_strategy_block(label:  str,
                         a:      dict,
                         cfg:    SimConfig):
    n = a['n']
    print(f'\n  ▶  {label}')
    print(THIN)

    print(f'\n  BANKROLL  ({n} games)')
    print(f'  {"Avg final:":<28} {fc(a["avg_final"])}  '
          f'({(a["avg_final"]-cfg.starting_bankroll)/cfg.starting_bankroll*100:+.1f}%)')
    print(f'  {"Median final:":<28} {fc(a["med_final"])}')
    print(f'  {"Std deviation:":<28} {fc(a["std_final"])}')
    print(f'  {"Best game:":<28} {fc(a["best"])}')
    print(f'  {"Worst game:":<28} {fc(a["worst"])}')
    print(f'  {"Avg peak reached:":<28} {fc(a["avg_peak"])}')

    print(f'\n  SESSION OUTCOMES')
    print(f'  {"Profitable games:":<28} {a["profitable"]:>5} / {n}  '
          f'({a["profitable"]/n*100:.1f}%)')
    print(f'  {"Went broke:":<28} {a["broke"]:>5} / {n}  '
          f'({a["broke"]/n*100:.1f}%)')
    print(f'  {"Reached $1,000+:":<28} {a["hit_1k"]:>5} / {n}  '
          f'({a["hit_1k"]/n*100:.1f}%)')
    print(f'  {"Reached $2,000+:":<28} {a["hit_2k"]:>5} / {n}  '
          f'({a["hit_2k"]/n*100:.1f}%)')
    print(f'  {"Reached $4,000+:":<28} {a["hit_4k"]:>5} / {n}  '
          f'({a["hit_4k"]/n*100:.1f}%)')

    th = a['total_hands']
    print(f'\n  HAND BREAKDOWN  ({th:,} total  |  avg {a["avg_hands"]:.1f}/game)')
    print(f'  {"Wins:":<28} {fi(a["total_wins"])}  {fp(a["total_wins"]/th)}')
    print(f'  {"Losses:":<28} {fi(a["total_losses"])}  {fp(a["total_losses"]/th)}')
    print(f'  {"Pushes:":<28} {fi(a["total_pushes"])}  {fp(a["total_pushes"]/th)}')
    print(f'  {"Busts:":<28} {fi(a["total_busts"])}  {fp(a["total_busts"]/th)}')
    print(f'  {"Blackjacks:":<28} {fi(a["total_bjs"])}  {fp(a["total_bjs"]/th)}')

    print(f'\n  HAND COMPOSITION')
    print(f'  {"Hard hands:":<28} {fi(a["total_hard"])}  {fp(a["total_hard"]/th)}')
    print(f'  {"Soft hands:":<28} {fi(a["total_soft"])}  {fp(a["total_soft"]/th)}')
    print(f'  {"Pairs dealt:":<28} {fi(a["total_pairs"])}  {fp(a["total_pairs"]/th)}')
    print(f'  {"Doubles taken:":<28} {fi(a["total_doubles"])}  {fp(a["total_doubles"]/th)}')
    if label.startswith('AGGRESSIVE'):
        print(f'  {"I18 deviations:":<28} {fi(a["total_i18"])}  {fp(a["total_i18"]/th)}')

    print(f'\n  COUNT DISTRIBUTION  (when bet was placed)')
    total_counted = a["hands_neg"]+a["hands_p1"]+a["hands_p2"]+a["hands_p3"]
    print(f'  {"TC negative:":<28} {fi(a["hands_neg"])}  {fp(a["hands_neg"]/total_counted)}')
    print(f'  {"TC +1:":<28} {fi(a["hands_p1"])}  {fp(a["hands_p1"]/total_counted)}')
    print(f'  {"TC +2:":<28} {fi(a["hands_p2"])}  {fp(a["hands_p2"]/total_counted)}')
    print(f'  {"TC +3+:":<28} {fi(a["hands_p3"])}  {fp(a["hands_p3"]/total_counted)}')

    print(f'\n  BETTING')
    print(f'  {"Avg max bet/game:":<28} {fc(a["avg_max_bet"])}')
    print(f'  {"Avg total wagered/game:":<28} {fc(a["avg_wagered"])}')
    print(f'  {"Strategy accuracy:":<28} {fp(a["avg_accuracy"])}')
    print(f'  {"Win rate:":<28} {fp(a["avg_win_rate"])}')
    print(THIN)


def print_comparison(agg: dict, basic: dict, cfg: SimConfig):
    print(f'\n  HEAD TO HEAD COMPARISON')
    print(THIN)
    print(f'  {"Metric":<28} {"Aggressive":>14} {"Basic":>14}')
    print(THIN)

    rows = [
        ('Avg final bankroll',
         fc(agg["avg_final"]),          fc(basic["avg_final"])),
        ('Profitable games',
         f'{agg["profitable"]/agg["n"]*100:.1f}%',
         f'{basic["profitable"]/basic["n"]*100:.1f}%'),
        ('Went broke',
         f'{agg["broke"]/agg["n"]*100:.1f}%',
         f'{basic["broke"]/basic["n"]*100:.1f}%'),
        ('Reached $1,000+',
         f'{agg["hit_1k"]/agg["n"]*100:.1f}%',
         f'{basic["hit_1k"]/basic["n"]*100:.1f}%'),
        ('Reached $4,000+',
         f'{agg["hit_4k"]/agg["n"]*100:.1f}%',
         f'{basic["hit_4k"]/basic["n"]*100:.1f}%'),
        ('Avg peak bankroll',
         fc(agg["avg_peak"]),           fc(basic["avg_peak"])),
        ('Win rate',
         fp(agg["avg_win_rate"]),       fp(basic["avg_win_rate"])),
        ('Pairs dealt/game',
         f'{agg["total_pairs"]/agg["n"]:.1f}',
         f'{basic["total_pairs"]/basic["n"]:.1f}'),
        ('Soft hands/game',
         f'{agg["total_soft"]/agg["n"]:.1f}',
         f'{basic["total_soft"]/basic["n"]:.1f}'),
        ('Doubles/game',
         f'{agg["total_doubles"]/agg["n"]:.1f}',
         f'{basic["total_doubles"]/basic["n"]:.1f}'),
        ('Avg wagered/game',
         fc(agg["avg_wagered"]),        fc(basic["avg_wagered"])),
    ]

    for label, av, bv in rows:
        print(f'  {label:<28} {av:>14} {bv:>14}')

    print(THIN)


def export_json(results: dict):
    os.makedirs('chart_data', exist_ok=True)

    agg_games   = results['aggressive']
    basic_games = results['basic']

    # per-game summary for charting
    game_summary = {
        'aggressive': [g.to_dict() for g in agg_games],
        'basic':      [g.to_dict() for g in basic_games],
    }

    # per-hand records for detailed charts
    agg_hands   = []
    basic_hands = []
    for g in agg_games:
        agg_hands.extend([h.to_dict() for h in g.hand_records])
    for g in basic_games:
        basic_hands.extend([h.to_dict() for h in g.hand_records])

    with open('chart_data/game_summary.json', 'w') as f:
        json.dump(game_summary, f, indent=2)

    with open('chart_data/hand_records_aggressive.json', 'w') as f:
        json.dump(agg_hands, f, indent=2)

    with open('chart_data/hand_records_basic.json', 'w') as f:
        json.dump(basic_hands, f, indent=2)

    print(f'  📊  chart_data/game_summary.json')
    print(f'  📊  chart_data/hand_records_aggressive.json')
    print(f'  📊  chart_data/hand_records_basic.json\n')


def print_report(results: dict):
    cfg  = results['config']
    agg  = _aggregate(results['aggressive'], cfg)
    bas  = _aggregate(results['basic'],      cfg)

    print(f'\n{THICK}')
    print('  BLACKJACK SIMULATION REPORT'.center(70))
    print(THICK)
    print(f'  Games:           {cfg.num_games:,}')
    print(f'  Decks:           {cfg.num_decks}')
    print(f'  Starting stack:  {fc(cfg.starting_bankroll)}')
    print(f'  Base bet:        {fc(cfg.base_bet)}')
    print(f'  Max bet:         {fc(cfg.max_bet)}')
    print(f'  Penetration:     {cfg.penetration*100:.0f}%')
    print(f'  Table players:   {cfg.num_other_players} random + 2 tracked')
    print(THICK)

    print_strategy_block('AGGRESSIVE COUNTER', agg, cfg)
    print_strategy_block('BASIC STRATEGY',     bas, cfg)
    print_comparison(agg, bas, cfg)

    print(f'\n  EXPORTING CHART DATA...')
    export_json(results)

    print(f'{THICK}\n')