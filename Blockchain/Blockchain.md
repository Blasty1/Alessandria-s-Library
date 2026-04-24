A blockchain is a chain of records , called blocks: each block is linked and secured by using cryptography.
A record/block is composed by:
![[Screenshot 2026-04-22 at 10.40.13.png|241]]
1. Data $\rightarrow$ data contained into the block
	1. It can contain multiple transactions
2. Previous Hash $\rightarrow$ link/pointer to the previous block
3. Hash $\rightarrow$ its fingerprint
4. Nonce $\rightarrow$ number used only once ( it is a big number )
	1. We can vary the hash of the block by changing the nonce ( block number and the prev. hash can note be changed )
![[Screenshot 2026-04-24 alle 15.36.29.png|403]]
We take the first 4 components ( Block number, Nonce, Data and pointer to the previous hash )and we hash them to produce the fingerprint of the block.
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

The blockchain establishes a target ( a specific hash, target is expressed by leading 0 ), the hashes higher did not count and they can not be accepted in the blockchain.
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



Next episode is:
20
