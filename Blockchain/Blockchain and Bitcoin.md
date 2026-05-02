A blockchain is a chain of records , called blocks: each block is linked and secured by using cryptography.
A record/block is composed by:
![[Screenshot 2026-04-22 at 10.40.13.png|241]]
1. Data $\rightarrow$ data contained into the block
	1. It can contain multiple transactions
2. Previous Hash $\rightarrow$ link/pointer to the previous block
3. Hash $\rightarrow$ its fingerprint
4. Nonce $\rightarrow$ number used only once ( it is a big number )
	1. We can vary the hash of the block by changing the nonce ( block number and the prev. hash can note be changed )
	2. It is an unsigned 32-bit number which means it has a cap( between 0 and 4 billion = $4 \cdot 10^9$)
5. Timestamp who gets updated every single second
![[Screenshot 2026-05-02 alle 12.24.04.png]]
We take all the components and we hash them to produce the fingerprint of the block.
![[Screenshot 2026-04-24 alle 15.37.45.png|404]]
![[Screenshot 2026-04-22 at 10.42.05.png|401]]

**SHA256 Hash Algorithm**
It was developed by NSA.
This algorithm is used to create a fingerprint of documents/entities
![[Screenshot 2026-04-22 at 10.44.58.png]]
SHA stands for Secure Hash Algorithm and 256 is the number of bits it takes up in memory ( 64 characters each one composed by 4 bit ).
*Explanation*
The hash produced is always formed by 64 characters which are taken from the set: 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F. Each of this character takes 4 bit, multiplying 64 by 4 produces 256 bit.
**The hash is a hexadecimal number** ( digits from 0 to 15 where 10 is represented by A ).
![[Screenshot 2026-04-24 alle 15.43.32.png]]


Some practical hints of how it works:
- If we put always the same data, we will get always the same hash
- If we slightly change our data , its hash changes entirely

There are different types of hash algorithms, each one must satisfy the following 5 requirements:
1. One-way $\rightarrow$ you can not restore the data from its hash
![[Screenshot 2026-04-22 at 10.55.33.png]]
2. Deterministic $\rightarrow$ same data hashed multiple times gives always the same result
3. Fast computation
4. Avalanche Effect $\rightarrow$ a tiny change in the data must produce a very different hash.
5. Must withstand collisions $\rightarrow$ the algorithm must tollerate collisions , it does not affect badly it. 
	1. It must prevent artificial collisions ( to avoid attacks )

**Immutable Ledger**
Immutable Ledger can be translated as Registro Immutabile.
Blockchain can serve as immutable ledger because when we change a specific block in the chain (e.g. we want to chaneg to owner/buyer of an house ), its next block will not point to that anymore( the hash/fingerprint is different now )
![[Screenshot 2026-04-22 at 11.09.11.png|363]]
You need to change all the blocks forward the victim.

**Distributed P2P Network**
Blockchain is actually copied/distributed into multiple servers which are interconnected.
![[Screenshot 2026-04-22 at 11.19.57.png|376]]
When a new block is added to a server, the blockchain is then updated to the other servers ( it can take some times ).
Each server is constantly checking its version with the peers´ versions in order to avoid inconsistency due some external attacks ( it uses a majority voting system ).
![[Screenshot 2026-04-22 at 11.25.18.png|397]]
*Difference between distributed and decentralized*
Distributed means not all the processes are executed in the same places whereas decentralized means that not one single entity has control over all the processing.

There are 3 types of decentralization:
1. Architectural decentralization: how many physical computers is a system made up of?
2. Political decentralization: how many individuals/organizations control the computers of the system?
3. Logical decentralization: does the system ( in terms of data structures and interfaces ) look like as a monolithic object or an amorphous swarm?
![[Screenshot 2026-04-22 at 11.35.43.png]]
- Languages are logically decentralized; the English spoken between Alice and Bob and the English spoken between Charlie and David do not need to agree at all. There is no centralized infrastructure required for a language to exist, and the rules of English grammar are not created or controlled by any one single person
- Blockchains are politically decentralized(no one controls them) and architecturally decentralized (no infrastructural central point of failure) but they are logically centralized (there is one commonly agreed state and the system behaves like a single computer)
- Traditional corporations are politically centralized (one CEO), architecturally centralized (one head office) and logically centralized (can’t really split them in half)

Decentralization is useful for 3 reasons:
1. Fault Tolerance: decentralized systems rely on separate components
2. Attack resistance:  decentralized systems are more expensive to attack and destroy or manipulate because they lack sensitive central points
3. Collusion resistance: partecipants of decentralized systems can not easily collude to act in a way that benefit them at expense of other participants.

**How mining works**
By changing the Nonce we can vary the hash of the block![[Screenshot 2026-04-24 alle 15.39.53.png|293]]
![[Screenshot 2026-04-24 alle 15.39.41.png|288]]
We can see the avalanche effect in action.

The blockchain establishes a target ( a specific hash, target is expressed by leading 0, more leading zero leads to a more difficult problem to solve ), the hashes higher did not count and they can not be accepted in the blockchain.
![[Screenshot 2026-04-24 alle 15.48.37.png]]
The miners vary the nonce In order to have the hash below the target and the block can be accepted by the blockchain.
The avalanche effect avoids cheating ( the system is completely unpredictable ).
The first person who discovers the block can add it to the blockchain and then the whole system starts again.
Every block has one special transaction at the very top. This is the **Block Reward**. The protocol says: _"The person who finds this block is allowed to write one transaction giving themselves X amount of new coins."_ We can not change the other transactions otherwise the hash will change completely.

**Consensus Protocol**
It is the strategy on how the blockchain agrees on what happened ( without needing a central authority ): it helps to define the truth when no one can trust each other.
It has to solve the following challenges:
1. Defend the network from attackers ( if someone tries to add a malicious block )
![[Screenshot 2026-04-24 alle 16.07.50.png|392]]
2. Two Far away nodes could successfully mine a block at the same time 
![[Screenshot 2026-04-24 alle 16.19.42.png|396]]

There are different types of consensus protocol:
- Proof-Of-Work ( PoW ) $\rightarrow$ used by Bitcoin 
	- it takes time and energy to validate a block, which makes it hard to cheat.  
	- **Downside:** It’s slow and consumes a lot of energy.
- Proof-Of-Stake ( PoS ) $\rightarrow$ used by Ethereum / Solana
	- Validators are chosen based on how much crypto they lock in ( it reduces the energy usage and allows for long-term scalability )

- Others.

Each consensus mechanism is a trade off between scalability , security and decentralization ( called **Blockchain Trilemma**)


**Proof-Of-Work ( PoW )**
Before a block is added and propagated from one node to others , the system applies tons of checks. After a block has been mined, the miner gets a reward ( coinbase ) for that ( if the block is secure and not malicious ).
While finding the solution took trillions of attempts, **verifying it takes only one**. Other nodes just run the data through the hash function once. If the result is below the target, the block is "proven" and added to the ledger.

The high consuming of electricity works as deterrent against potential attacks.

**Longest Chain Rule**
In a decentralized network, it’s common for two miners to find a block at almost the exact same time.
![[Screenshot 2026-04-24 alle 17.07.28.png|429]]
![[Screenshot 2026-04-24 alle 17.08.22.png|434]]
Some conflicts happen between nodes: there are two versions of the chains and this phenomena is called **Competing Chains**. The protocol makes the two chains wait for a new block ( both versions are valid for a moment ): the first one to mint a new block will be the global and new blockchain ( =the longest chain is the winner of the conflict ).
The orange chain has much more hash computation power ( assuming each node has the same computation power in this chart ) and what happens is that the orange chain will probabily win the competition.
![[Screenshot 2026-04-24 alle 17.14.59.png|441]]
![[Screenshot 2026-04-24 alle 17.15.21.png|443]]
The blocks aside are called orphaned blocks and their miners have received their reward which is in the block outside the blockchain ( reward is not payment in cash but it is the special space to add a transaction ): the reward is not valid anymore.
The reward is given only after 6 confirmation usually ( they don't want to double the payment ).

# Cryptocurrency
Each cryptocurrency is defined by 3 aspects:
1. Technology $\rightarrow$ blockchain
2. Protocol/Coin $\rightarrow$ a set of rules for participants of the bitcoin network.
	1. Each protocol has its own coin (e.g. bitcoin has its coin called bitcoin, same for ethereum )
	2. The coin is the native asset of that specific blockchain. It is usually used to pay for the "work" done by the network (transaction fees or mining rewards).
3. Tokens $\rightarrow$ they rely on smart contracts which are builts on top of protocols..
	1. Bitcoins has not token because it does not allow for smart contracts
	2. Tokens are like "guest" currencies. They don’t have their own blockchain; instead, they live inside another protocol's ecosystem using **Smart Contracts**
![[Screenshot 2026-04-26 alle 19.09.57.png|389]]

*Bitcoin's Monetary Policy*
The monetary policy of bitcoin is entirely controlled by software: no one can change it.
It consist into two parts:
1. The Halving $\rightarrow$ the number of bitcoins per block released is halved every single 4 years
![[Screenshot 2026-04-26 alle 19.20.13.png|377]]
 ![[Screenshot 2026-04-26 alle 19.24.26.png]]
2. Block Frequency $\rightarrow$ how often the blocks come in 
	1. Bitcoin is programmed to add a new block to the chain approximately every **10 minutes**.
	2. This is managed by the **Difficulty Adjustment**. As more miners join (increasing total computing power), the "puzzle" becomes harder to solve. If miners leave, the puzzle becomes easier.
![[Screenshot 2026-04-26 alle 19.28.27.png|386]]

*Mining Difficulty*
Increasing the number of leading zeros means decreasing the pool of correct address for the block. Each time we introduce a new leading 0, we are decreasing the pool by 16 times ( 2^4 , because each digit is represented by 4 bits ).
The difficulty can be seens as below:
![[Screenshot 2026-05-02 alle 11.48.43.png|457]]
The green one is our valid pool while the total pool is orange in the image.
However the nonce is capped to 4 billion which means the probability is higher that what we have computed:
![[Screenshot 2026-05-02 alle 12.20.10.png|396]]
To increase the difficulty we know that each second the timestamp is changed and it forces to solve the hash problem with that data in 1 second otherwise the problem starts again from 0 ( the already tried nonce should be tried again ).


Mining Difficulty is computed by
$$
\text{Difficulty} = \frac{\text{Current Target}}{\text{Max Target}}
$$
In our case:
![[Screenshot 2026-05-02 alle 11.51.14.png|433]]
Difficulty is adjusted almost every 2 weeks ( every 2016 blocks, knowing that each block is minted each 10 minute ) through the number of leading zeros.

It says how much harder is to mine a bitcoin now than it was at the beginning.
The current target is stored in the block meta data in the field called **bits**:
![[Screenshot 2026-05-02 alle 15.45.51.png|298]]
We just take the code in bits and we convert it to hexadecimal. 
We take the first two digits and we convert them to decimal system. We get the number of bytes , if we multiply it per 8 we get the total number of bits which can be divided by 4 to get the total of digits in hexadecimal
![[Screenshot 2026-05-02 alle 15.59.35.png|408]]
![[Screenshot 2026-05-02 alle 16.00.19.png|410]]

*Mining Pools*
A mining pool distributes the work ( challenge/puzzle) for attempting the same problem in order that multiple people do not work at the same time at the same problem without collaboration.

When one of the node of the mining pool finds the solution, the reward is then split about the nodes inside the mining pool weighted on the basis of the computing power introduced in the pool.

*Where do transactions in the data field come from in reality?*
All the transactions that happens in between the mining of a new block are stored into a **mempool** ( attached to each node ) which is a staging area for transactions.
![[Screenshot 2026-05-02 alle 12.33.37.png|334]]
For each transaction we have its fee ( how much the miner is earning ) and its identifier.
The miner has to include some of this transactions ( of the mempool ) in the data field of the just mined block.
The miner has to choose which transactions should be included ( each block has a maximum dimension around 1MB in Bitcoin , which is 200k transactions ) and it chooses the transactions with the highest fee ( these fees will be its reward )
![[Screenshot 2026-05-02 alle 12.37.16.png|390]]
The hash rate is very high and usually it allows for being faster then 1 second to try the whole 4 billion range of number of the nonce. If at the end of the search no hash has been found , the miner changes the data: it chooses different configuration of the transactions until it finds the hash.

*How do Mempools work?*
There is one mempools for each node of the blockchain.
![[Screenshot 2026-05-02 alle 12.56.35.png|423]]
It is a staging area for transactions.
Practical example: one person does a transaction and it is added to her mempool. The update is then broadcasted to her neighbours ( closer nodes of the blockchain network ).
![[Screenshot 2026-05-02 alle 13.00.13.png|400]]
When a node/miner finds a new block, it already knows in advanced which transactions to add and these are deleted from the mempools ( they are updated ).
![[Screenshot 2026-05-02 alle 13.02.33.png|413]]

*51% Attack*
It happens when malicious entities control 51% of the hash rate / power of the blockchain and they start to manipulate transaction histories ( .e.g reversing old transaction and spending again ).
![[Screenshot 2026-05-02 alle 15.36.18.png]]
Having much more power , they can double the length of the blockchain and they are controlling it (remember the longest chain wins rule when there is a merge).

# Cryptocurrency Transactions
A **UTXO** represents a certain amount of cryptocurrency that has been authorized by a sender and is available to be spent by a recipient.
When someone wants spent money , he wants to make a new transaction. Each transaction requires:
- Input ( a link to an UTXO )
	- The UTXO is not an UTXO anymore, it is done ( it is not considered as UTXO anymore )
- Output ( the owner of the money transferred)
	- It is allowed to have multiple outputs to a transaction.
![[Screenshot 2026-05-02 alle 16.17.51.png|414]]
![[Screenshot 2026-05-02 alle 16.18.38.png|416]]

*Where do transactions fees come from?*
Any acceptable transaction needs to have a fee ( something that we pay in order that the transaction is inserted into a block ): bigger is the fee , faster it would be inserted into a block.
The fee is originated from the change of input w.r.t. the output of a transaction.
![[Screenshot 2026-05-02 alle 16.39.12.png]]
Here the output sum up to 0.98 and to 0.1, the change represents the fee of the transaction.

*How wallets work?*
The wallet calculates remaining UTXO ( transaction not already used/linked by another )going through the whole blockchain in order to show us our balance ( how many bitcoins do we have? ).
![[Screenshot 2026-05-02 alle 16.50.08.png|419]]
The problem of this image is the privacy: everyone can see people's money and they can also add/remove money of others.

*Signatures*
When someone starts into cryptocurrency, he gets a private key ( unique identifier ) and then he can generate a public key using the private key ( public keys are available to everyone ).
The link between private key and public key is not reversable. 
The private key is used to sign the message ( transaction  in this case ) in order to create a signature which is paired always with the message.
![[Screenshot 2026-05-02 alle 17.11.46.png|389]]
The verification function is used to asses the signature by using the public key to confirm or deny that the relative message is signed with the relative private key.
![[Screenshot 2026-05-02 alle 17.41.26.png|399]]
The bitcoin address is derived by the public key by applying the sha256 algorithm. It is used for receiving money ( as IBAN we can say but it can not be used to pull money ) so it can be available online.
We should avoid to expose the public key because if someone is able to find a way of reverse engineering the relation between private and public key then he can get our money.

*What is Segregated Witness ( SegWit )?*
It is an upgrade of the bitcoin protocol.
A single transaction is composed by: transactionID  ( unique receipt of the transfer ), sender, receiver, amount of money , the signature and public key ( useful for proof of ownership, they are used for verifying that we own the private key associated with that bitcoin address).
![[Screenshot 2026-05-02 alle 17.29.27.png|392]]
The problem with this structure is that signature and public key are long and heavy numbers ( they take 60% of the space dimension of the whole transaction ).
**SegWit** proposes to remove the **scriptSig** ( signature + public key ) from the transaction inside the block and send it through the network separately in order to save space.

Now we can include a lot of more data but the threshold/maximum size of a block is still 1 Mb.

*Hierarchically deterministic (HD) Wallets*
From and To in the transactions are replaced with the relative public keys but this allows to establish a flow of money ( privacy can be violated or not totally preserved ).
With HD Wallets, the owner has a master private key which is used to generate multiple private keys with new relative addresses
![[Screenshot 2026-05-02 alle 17.51.14.png|384]]
It enforces privacy or it allows for flow money structuring ( each department of a company has a different private key/ address ).
There is also a master public key related to its master private key which is used for checking payment or transactions by an auditor ( it can be used as a global public key ).



Next episode is:
44-
