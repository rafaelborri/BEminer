import hashlib

#Nonce limit must starts with 0
NONCE_LIMIT = 10

#How many zeros must be in final hash (usualy 18 zeros)
zeroes = 1


def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f"Found hash with nonce: {nonce}")
            return hash_try

    print("ERROR code: 4")
    input("Bminer > ")
    quit()

#Number of block you want to mine
block_number = 0
#Transactions
transactions = ""
#Previous hash (hash of previous block)
previous_hash = ""

if bool(block_number) == False:
    print("ERROR code: 1")
    input("Bminer > ")
    quit()
if bool(transactions) == False:
    print("ERROR code: 2")
    input("Bminer > ")
    quit()
if bool(previous_hash) == False:
    print("ERROR code: 3")
    input("Bminer > ")
    quit()



if __name__ == "__main__":
    mine(block_number, transactions, previous_hash)