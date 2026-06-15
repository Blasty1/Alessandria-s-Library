*What is Ethereum?*
It is designed as a platform for others to build on top of it using smart contracts while bitcoin was created mainly for developing a cryptocurrency
Ethereum core idea is to build digital assets and decentralized applications ( dapps ) that run 24/7.
Ether ( ETH ) is the native cryptocurrency of Ethereum.
Ethereum used *proof of work* but in 2002 it upgraded to a new system called *proof of stake*: it is 100% energy efficient.
1. If you want to help run the network, you stake your coins which means you lock up your coins in a digital vault as a deposit
2. The network randomly picks a Validator to check the next batch of transactions: more coins you have stacked and higher chances are of being picked
3. The chosen Validator checks the transactions to make sure they are real
4. If everything looks good , the Validator gets a small reward
5. If a Validator tries to cheat (e.g. approve fake transactions ), they lose some or all of thei staked coins as penalty.
![[Screenshot 2026-05-06 alle 19.19.03.png|385]]

*Smart Contracts*
They are programs running on the blockchain.
In ethereum the programming language for smart contracts is Solidity while for Bitcoin is called Bitcoin Script.
Solidity is **Turing-Complete** ( which means that Solidity can be used to implement any logic into code ) while Bitcoin Script is not ( it does not include loops ).
Each node has a copy of all smart chain and theirs current state.
![[Screenshot 2026-05-10 alle 17.25.29.png|489]]
*Decentralized Applications Dapps*
A Dapp is a digital application that run on a blockchain or peer-to-peer network , rather than centralized servers.
They operate using smart contracts to automate functions, ensuring transparency, censorships resistance and autonomy with no single entity controlling the network.

Running a smart contract on the blockchain requires gas ( each operation/command as jump/pop/create has a fixed cost ). The fact that you pay for iterating code means that people are incentivized to write quality good ( Infinite loops aren't a problem; the code will simply run out of gas and terminate ). Prices are decided by community consensus.

*Decentralized Autonomous Organizations ( DAOs )*
An organization that operates without centralized leadership using smart contracts to automate decisions and enforce rules.

After the DAO attack ( crowdfund operation of 150,000,000 $ hacked for 50,000,000 because a bug was found in the smart contract code ) Ethereum split in 2016 into **ETH** ( Ethereum Difference , The community decided to "rewrite" history via a hard fork to return stolen funds to users) and **ETC** ( Ethereum classic , A minority refused to change the ledger, arguing that "Code is Law." They believe that even if a hack occurs, the blockchain must remain untouched ).
![[Screenshot 2026-05-10 alle 17.57.10.png|441]]
There are two types of forks:
- Hard fork $\rightarrow$ A hard fork is a permanent divergence from the previous version of the blockchain.
	- Nodes that don't upgrade cannot validate new block (e.g. the maximum block size increases, old nodes can not allow for block with higher dimension )
	- If a part of the community refuses to upgrade, the chain splits into two (e.g., **ETH vs. ETC**).
- Soft fork $\rightarrow$ it is a backward compatible upgrade
	- Introduces a stricter rule that still follows the old rules ( e.g. the maximum block size decreases, old nodes can allow for block with lower dimension, it is not a problem )
	- ld nodes still see new blocks as valid, even if they don't understand the new features.
	- It does not result in a split because the chain remains a single ledger.

*Initial Coin Offerings ( ICOs )* 
IPO is a way for companies to raise money for the public trade market. 
ICO is when a company creates its own token ( which are not related to the equity , they are utility token usually means they are designed to be used in the application/idea founders are building ) and sell it through the blockchain to people to raise money.
![[Screenshot 2026-05-10 alle 18.22.36.png]]


