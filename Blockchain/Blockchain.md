A blockchain is a chain of records , called blocks: each block is linked and secured by using cryptography.
A record/block is composed by:
![[Screenshot 2026-04-22 at 10.40.13.png|241]]
1. Data $\rightarrow$ data contained into the block
2. Previous Hash $\rightarrow$ link/pointer to the previous block
3. Hash $\rightarrow$ its fingerprint
![[Screenshot 2026-04-22 at 10.42.05.png|401]]

**SHA256 Hash Algorithm**
It was developed by NSA.
This algorithm is used to create a fingerprint of documents/entities
![[Screenshot 2026-04-22 at 10.44.58.png]]
SHA stands for Secure Hash Algorithm and 256 is the number of bits it takes up in memory ( 64 characters each one composed by 4 bit ).
*Explanation*
The hash produced is always formed by 64 characters which are taken from the set: 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F. Each of this character takes 4 bit, multiplying 64 by 4 produces 256 bit.

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


Next episode is:
10 how mining works 