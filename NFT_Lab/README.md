# NFT-Lab

Here are the steps that I followed in order to complete this laboratory work.

## Getting started

First things first, I followed the requirements:

1. Installed code editor (Visual Studio Code or an alternative one)

2. Installed [node js](https://nodejs.org/en)

3. Checked the installation by running the command `npm -v`

4. Installed the Metamask browser extension.

### Interacting with Q testnet

5. Connected Metamask to the Q testnet
   1. Network name: Q Testnet
   2. RPC URL: https://rpc.qtestnet.org
   3. Chain ID: 35443
   4. Currency symbol (with space): "Q "
   5. Block explorer URL: https://explorer.qtestnet.org

6. Created a new Metamask address (in order not to compromise the data)

7. Got test tokens to the created address using [Q faucet](https://faucet.qtestnet.org/)

8. Copied the preparatory code of the lab work from [GitHub](https://github.com/Q-Laboratory/nft-lab).

## Preparing contracts and front end parts

1. Opened the folder with the lab from the previous step in the code editor

2. Created a copy of the `.env.example` file and name it `.env`

3. Got the private key of the account (that has test tokens on) in the Metamask
This can be done as follows: 
    * in the browser extension go to _Account details_
    * click on _Export private key_ and enter your Metamask password
    * copy the uncovered private key

4. Inserted the copied private key into the `.env` file you created as the `PRIVATE_KEY` variable

5. Opened a terminal in the code editor and entered the command: 
    ```bash
    npm install
    ``` 
    This command installed the necessary dependencies for the contract deployment and local operation of the frontend

6. After running the command above, entered the next command:
    ```bash
    npm run deploy-contracts
    ```
    This command deployed the contract that is in the lab work. After the command was complete, the terminal displayed the address of the contract. This address was copied.

7. In the `.env` file replaced the value of the variable `VITE_ERC721_ADDRESS` with the copied address

    :warning: Before proceeding, since I use **Windows OS**, I replaced **line 14** in `package.json` file with following command:

    ```
    "start-web-client": "npm run copy-file-win && npm --prefix ./web-client run start"
    ```

8. In the terminal, entered the command:
    ```bash
    npm run start-web-client
    ```
    After its completion, there was a link in the terminal to the front end application that had been set up locally.

9. Clicked on the link to open the front end application that works with the contracts you deployed.

:warning: **Saved files after making changes to them**

## Tasks

**After successfully completing the preparation part, the following tasks were completed:**

1. Checked the basic flow operation:
    * Mint an NFT with image links (you can upload the desired image to ipfs yourself or get the link to the image on Google :warning: please make sure that you have copied the link to the actual image :warning:)
    * Transfer an NFT to another address (this can be your second Metamask account)
    * Switch to that address to see the differences that will be in the interface
    * Use the address search. Take a look at your main and secondary accounts

After completing steps above, I located to the code editor and executed the following command `control + C`. After that the frontend was halted

2. Transformed an existing NFT contract into an [SBT](https://vitalik.ca/general/2022/01/26/soulbound.html) contract. To achieve that, add some necessary code in the `SimpleNFT.sol` file. The file location is here: `NFT-LAB/core-contracts/contracts/SimpleNFT.sol`
 
   There was provided a solution that makes the issued tokens non-transferable. As a hint, you can look up for already existing SBT contracts to take away what can be used to complete the task

3. After making changes to the `SimpleNFT.sol` file I redeployed the contract and restarted the frontend part. The deployment instructions can be found in the steps 6-9 in the _Preparation part_ of the lab

4. After making required changes to make the contract an SBT, the transfer function on the front end throws an error

5. Additionally, I've done an optional task by taking the address of the contract my friend and followed the steps 7-9 in the _Preparation part_. It allowed seeing the NFTs my friend has minted.

