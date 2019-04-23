#!/usr/bin/env python3

import argparse
import json
import sys


def init_default_argument_parser(prog_desc, default_chain_id, default_start_time):
    parser = argparse.ArgumentParser(description=prog_desc)
    parser.add_argument(
        'exported_genesis',
        help='exported genesis.json file',
        type=argparse.FileType('r'), default=sys.stdin,
    )
    parser.add_argument('--chain-id', type=str, default=default_chain_id)
    parser.add_argument('--start-time', type=str, default=default_start_time)
    return parser


def main(argument_parser, process_genesis_func):
    args = argument_parser.parse_args()
    if args.chain_id.strip() == '':
        sys.exit('chain-id required')

    genesis = json.loads(args.exported_genesis.read())

    print(json.dumps(process_genesis_func(
        genesis=genesis, parsed_args=args,), indent=4))



def process_raw_genesis(genesis, parsed_args):
    # Update block size
    genesis['consensus_params']['block']['max_bytes'] = '20000000'
    genesis['consensus_params']['block']['max_gas'] = '-1'

    # Crisis Module
    genesis['app_state']['crisis'] = {
        'constant_fee': {
            'amount': '10000000000',
            'denom': 'uluna',
        },
    }

    # Set new chain ID and genesis start time
    genesis['chain_id'] = parsed_args.chain_id.strip()
    genesis['genesis_time'] = parsed_args.start_time

    # Enable transfers
    genesis['app_state']['bank']['send_enabled'] = True
    genesis['app_state']['distr']['withdraw_addr_enabled'] = True

    # Auth Module
    # number of signature limit in a single tx
    genesis['app_state']['auth']['params']['tx_sig_limit'] = "100"

    # Staking Module
    genesis['app_state']['staking']['params']['unbonding_time'] = "1814400000000000"
    genesis['app_state']['staking']['params']['max_validators'] = 100

    # Distribution Module
    genesis['app_state']['distr']['community_tax'] = "0.000000000000000000"
    genesis['app_state']['distr']['base_proposer_reward'] = "0.010000000000000000"
    genesis['app_state']['distr']['base_bonus_proposer_reward'] = "0.040000000000000000"

    # Treasury Module
    genesis['app_state']['treasury']['params']['tax_policy']['rate_min'] = "0.000500000000000000"
    genesis['app_state']['treasury']['params']['tax_policy']['rate_max'] = "0.010000000000000000"
    genesis['app_state']['treasury']['params']['tax_policy']['change_max'] = "0.000250000000000000"
    genesis['app_state']['treasury']['params']['tax_policy']['cap']['denom'] = "msdr"
    genesis['app_state']['treasury']['params']['tax_policy']['cap']['amount'] = "1000000"

    genesis['app_state']['treasury']['params']['reward_policy']['rate_min'] = "0.050000000000000000"
    genesis['app_state']['treasury']['params']['reward_policy']['rate_max'] = "0.200000000000000000"
    genesis['app_state']['treasury']['params']['reward_policy']['change_max'] = "0.025000000000000000"
    genesis['app_state']['treasury']['params']['reward_policy']['cap']['denom'] = "unused"
    genesis['app_state']['treasury']['params']['reward_policy']['cap']['amount'] = "0"

    genesis['app_state']['treasury']['params']['seigniorage_burden_target'] = "0.670000000000000000"
    genesis['app_state']['treasury']['params']['mining_increment'] = "1.070000000000000000"
    genesis['app_state']['treasury']['params']['window_short'] = "4"
    genesis['app_state']['treasury']['params']['window_long'] = "52"
    genesis['app_state']['treasury']['params']['window_probation'] = "12"
    genesis['app_state']['treasury']['params']['oracle_share'] = "0.100000000000000000"
    genesis['app_state']['treasury']['params']['budget_share'] = "0.900000000000000000"

    # Budget Module
    genesis['app_state']['budget']['params']['active_threshold'] = "0.100000000000000000"
    genesis['app_state']['budget']['params']['legacy_threshold'] = "0.000000000000000000"
    genesis['app_state']['budget']['params']['vote_peroid'] = "518400"
    genesis['app_state']['budget']['params']['deposit']['denom'] = "msdr"
    genesis['app_state']['budget']['params']['deposit']['amount'] = "100000000"

    # Oracle Module
    genesis['app_state']['oracle']['params']['vote_period'] = "180"
    genesis['app_state']['oracle']['params']['vote_threshold'] = "0.500000000000000000"
    genesis['app_state']['oracle']['params']['drop_threshold'] = "10"
    genesis['app_state']['oracle']['params']['oracle_reward_band'] = "0.010000000000000000"

    # Slashing Module
    genesis['app_state']['slashing']['params']['max_evidence_age'] = "1814400000000000"
    genesis['app_state']['slashing']['params']['signed_blocks_window'] = "10000"
    genesis['app_state']['slashing']['params']['min_signed_per_window'] = "0.050000000000000000"
    genesis['app_state']['slashing']['params']['downtime_jail_duration'] = "600000000000"
    genesis['app_state']['slashing']['params']['slash_fraction_double_sign'] = "0.010000000000000000"
    genesis['app_state']['slashing']['params']['slash_fraction_downtime'] = "0.000100000000000000"

    # Market Module
    genesis['app_state']['market']['params']['daily_swap_limit'] = "0.010000000000000000"

    return genesis

if __name__ == '__main__':
    parser = init_default_argument_parser(
        prog_desc='Convert genesis.json for columbus-drill',
        default_chain_id='columbus-drill',
        default_start_time='2019-04-18T19:00:00Z',
    )
    main(parser, process_raw_genesis)
