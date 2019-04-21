import argparse
import json
import sys
import time


def init_default_argument_parser(prog_desc):
    parser = argparse.ArgumentParser(description=prog_desc)
    parser.add_argument(
        'exported_genesis',
        help='exported genesis.json file',
        type=argparse.FileType('r'), default=sys.stdin,
    )
    parser.add_argument(
        'address_book',
        help='address list address.json file',
        type=argparse.FileType('r'), default=sys.stdin,
    )

    return parser


def main(argument_parser, process_genesis_func):
    args = argument_parser.parse_args()
    
    genesis = json.loads(args.exported_genesis.read())
    addressBook = json.loads(args.address_book.read())

    print(json.dumps(process_genesis_func(genesis, addressBook), indent=4))



def process_raw_genesis(genesis, addressBook):
    initialAmount = "10000000000"
    initialDenom = "uluna"

    timeForTenMinutes = 60 * 10

    i = 0
    accounts = []
    while i < len(addressBook):

        # t = 0
        # schedules = {}
        # baseTime = int(time.time())
        # while t < 10:
        #     schedules[baseTime + t * timeForTenMinutes] = 0.1
        #     t+=1
        

        accounts.append(
            {
                'address': addressBook[i],
                'coins': [
                    {
                        'denom': initialDenom,
                        'amount': initialAmount
                    }
                ],
                'sequence_number': str(0),
                'account_number': str(i),
                'original_vesting': None,
                'delegated_free': None,
                'delegated_vesting': None,
                'start_time': str(0),
                'end_time': str(1),
                'vesting_schedules': None
            }        
        )

        i+=1

    genesis['app_state']['accounts'] = accounts

    return genesis

if __name__ == '__main__':
    parser = init_default_argument_parser(prog_desc='Convert genesis.json for columbus-drill')

    main(parser, process_raw_genesis)
