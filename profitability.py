#! /bin/python3
import requests
from diff_to_work import target_from_nbits, work

url = 'https://explorer.ergon.network/api/'
def block_count():
    r = requests.get(url+'getblockcount')
    return r.json()

def block_hash(height):
    r = requests.get(url+'getblockhash?index='+str(height))
    return r.json()

def block(block_hash):
    r = requests.get(url+'getblock?hash='+block_hash)
    block = r.json()
    return block

def block_diff(block):
    return block['difficulty']

def block_reward(block):
    tx_hash = block['tx'][0]
    r = requests.get(url+'getrawtransaction?txid='+tx_hash+'&decrypt=1')
    tx = r.json()
    total_value=0
    for v in tx['vout']:
        total_value+=v['value']
    return total_value*10**8

def parse_bits_string(bits):
    exp = int('0x'+bits[0:2],16)
    sigd = int('0x'+bits[2:],16)
    return exp, sigd

height = block_count()
current_block = block(block_hash(height))
exp, sigd = parse_bits_string(current_block['bits'])
current_target = target_from_nbits(exp, sigd)
current_work = work(current_target)
current_reward = block_reward(current_block)
# work done by 1 ths per day:
ths_work = 10**12*3600*24
blocks_a_day = ths_work/current_work
reward_per_day = blocks_a_day*current_reward
xrg_per_day=reward_per_day/10**5

print("we are at the height of: ", height,'<BR>')
print("difficulty is: ", block_diff(current_block),'<BR>')
print("# of hashes to find a block: ", current_work,'<BR>')
print("the reward is: ", current_reward, 'fix','<BR>')
print(f"1Ths would find {blocks_a_day:.0f} block a day earning {reward_per_day:.0f}fix" ,'<BR>')
print(f"{reward_per_day:.0f}fix is {xrg_per_day:.5f}mXRG",'<BR>')


