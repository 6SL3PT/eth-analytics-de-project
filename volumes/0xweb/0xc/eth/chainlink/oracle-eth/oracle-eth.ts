/**
 *  AUTO-Generated Class: 2024-02-06 01:39
 *  Implementation: https://etherscan.io/address/0x5f4ec3df9cbd43714fe2740f5e3616155c5b8419#code
 */
import di from 'a-di';
import { TAddress } from '@dequanto/models/TAddress';
import { TAccount } from '@dequanto/models/TAccount';
import { TBufferLike } from '@dequanto/models/TBufferLike';
import { ClientEventsStream, TClientEventsStreamData } from '@dequanto/clients/ClientEventsStream';
import { ContractBase, ContractBaseHelper } from '@dequanto/contracts/ContractBase';
import { ContractStorageReaderBase } from '@dequanto/contracts/ContractStorageReaderBase';
import { TxWriter } from '@dequanto/txs/TxWriter';
import { ITxLogItem } from '@dequanto/txs/receipt/ITxLogItem';
import { Web3Client } from '@dequanto/clients/Web3Client';
import { IBlockChainExplorer } from '@dequanto/explorer/IBlockChainExplorer';
import { SubjectStream } from '@dequanto/class/SubjectStream';


import type { ContractWriter } from '@dequanto/contracts/ContractWriter';
import type { TAbiItem } from '@dequanto/types/TAbi';
import type { TEth } from '@dequanto/models/TEth';
import type { TOverrideReturns } from '@dequanto/utils/types';


import { Etherscan } from '@dequanto/explorer/Etherscan'
import { EthWeb3Client } from '@dequanto/clients/EthWeb3Client'



export class ChainlinkOracleEth extends ContractBase {
    constructor(
        public address: TEth.Address = '0x5f4ec3df9cbd43714fe2740f5e3616155c5b8419',
        public client: Web3Client = di.resolve(EthWeb3Client, ),
        public explorer: IBlockChainExplorer = di.resolve(Etherscan, ),
    ) {
        super(address, client, explorer)

        this.storage = new ChainlinkOracleEthStorageReader(this.address, this.client, this.explorer);
    }

    

    async $constructor (deployer: TSender, _aggregator: TAddress, _accessController: TAddress): Promise<TxWriter> {
        throw new Error('Not implemented. Use the ContractDeployer class to deploy the contract');
    }

    // 0x79ba5097
    async acceptOwnership (sender: TSender, ): Promise<TxWriter> {
        return this.$write(this.$getAbiItem('function', 'acceptOwnership'), sender);
    }

    // 0xbc43cbaf
    async accessController (): Promise<TAddress> {
        return this.$read(this.$getAbiItem('function', 'accessController'));
    }

    // 0x245a7bfc
    async aggregator (): Promise<TAddress> {
        return this.$read(this.$getAbiItem('function', 'aggregator'));
    }

    // 0xa928c096
    async confirmAggregator (sender: TSender, _aggregator: TAddress): Promise<TxWriter> {
        return this.$write(this.$getAbiItem('function', 'confirmAggregator'), sender, _aggregator);
    }

    // 0x313ce567
    async decimals (): Promise<number> {
        return this.$read(this.$getAbiItem('function', 'decimals'));
    }

    // 0x7284e416
    async description (): Promise<string> {
        return this.$read(this.$getAbiItem('function', 'description'));
    }

    // 0xb5ab58dc
    async getAnswer (_roundId: bigint): Promise<bigint> {
        return this.$read(this.$getAbiItem('function', 'getAnswer'), _roundId);
    }

    // 0x9a6fc8f5
    async getRoundData (_roundId: bigint): Promise<{ roundId: bigint, answer: bigint, startedAt: bigint, updatedAt: bigint, answeredInRound: bigint }> {
        return this.$read(this.$getAbiItem('function', 'getRoundData'), _roundId);
    }

    // 0xb633620c
    async getTimestamp (_roundId: bigint): Promise<bigint> {
        return this.$read(this.$getAbiItem('function', 'getTimestamp'), _roundId);
    }

    // 0x50d25bcd
    async latestAnswer (): Promise<bigint> {
        return this.$read(this.$getAbiItem('function', 'latestAnswer'));
    }

    // 0x668a0f02
    async latestRound (): Promise<bigint> {
        return this.$read(this.$getAbiItem('function', 'latestRound'));
    }

    // 0xfeaf968c
    async latestRoundData (): Promise<{ roundId: bigint, answer: bigint, startedAt: bigint, updatedAt: bigint, answeredInRound: bigint }> {
        return this.$read(this.$getAbiItem('function', 'latestRoundData'));
    }

    // 0x8205bf6a
    async latestTimestamp (): Promise<bigint> {
        return this.$read(this.$getAbiItem('function', 'latestTimestamp'));
    }

    // 0x8da5cb5b
    async owner (): Promise<TAddress> {
        return this.$read(this.$getAbiItem('function', 'owner'));
    }

    // 0xc1597304
    async phaseAggregators (input0: number): Promise<TAddress> {
        return this.$read(this.$getAbiItem('function', 'phaseAggregators'), input0);
    }

    // 0x58303b10
    async phaseId (): Promise<number> {
        return this.$read(this.$getAbiItem('function', 'phaseId'));
    }

    // 0xf8a2abd3
    async proposeAggregator (sender: TSender, _aggregator: TAddress): Promise<TxWriter> {
        return this.$write(this.$getAbiItem('function', 'proposeAggregator'), sender, _aggregator);
    }

    // 0xe8c4be30
    async proposedAggregator (): Promise<TAddress> {
        return this.$read(this.$getAbiItem('function', 'proposedAggregator'));
    }

    // 0x6001ac53
    async proposedGetRoundData (_roundId: bigint): Promise<{ roundId: bigint, answer: bigint, startedAt: bigint, updatedAt: bigint, answeredInRound: bigint }> {
        return this.$read(this.$getAbiItem('function', 'proposedGetRoundData'), _roundId);
    }

    // 0x8f6b4d91
    async proposedLatestRoundData (): Promise<{ roundId: bigint, answer: bigint, startedAt: bigint, updatedAt: bigint, answeredInRound: bigint }> {
        return this.$read(this.$getAbiItem('function', 'proposedLatestRoundData'));
    }

    // 0x92eefe9b
    async setController (sender: TSender, _accessController: TAddress): Promise<TxWriter> {
        return this.$write(this.$getAbiItem('function', 'setController'), sender, _accessController);
    }

    // 0xf2fde38b
    async transferOwnership (sender: TSender, _to: TAddress): Promise<TxWriter> {
        return this.$write(this.$getAbiItem('function', 'transferOwnership'), sender, _to);
    }

    // 0x54fd4d50
    async version (): Promise<bigint> {
        return this.$read(this.$getAbiItem('function', 'version'));
    }

    $call () {
        return super.$call() as IChainlinkOracleEthTxCaller;
    }

    $data (): IChainlinkOracleEthTxData {
        return super.$data() as IChainlinkOracleEthTxData;
    }
    $gas (): TOverrideReturns<IChainlinkOracleEthTxCaller, Promise<{ gas?: bigint, price?: bigint, error?: Error & { data?: { type: string, params } } }>> {
        return super.$gas() as any;
    }

    onTransaction <TMethod extends keyof IMethods> (method: TMethod, options: Parameters<ContractBase['$onTransaction']>[0]): SubjectStream<{
        tx: TEth.Tx
        block: TEth.Block<TEth.Hex>
        calldata: IMethods[TMethod]
    }> {
        options ??= {};
        options.filter ??= {};
        options.filter.method = method;
        return <any> this.$onTransaction(options);
    }

    onLog (event: keyof IEvents, cb?: (event: TClientEventsStreamData) => void): ClientEventsStream<TClientEventsStreamData> {
        return this.$onLog(event, cb);
    }

    onAnswerUpdated (fn?: (event: TClientEventsStreamData<TLogAnswerUpdatedParameters>) => void): ClientEventsStream<TClientEventsStreamData<TLogAnswerUpdatedParameters>> {
        return this.$onLog('AnswerUpdated', fn);
    }

    onNewRound (fn?: (event: TClientEventsStreamData<TLogNewRoundParameters>) => void): ClientEventsStream<TClientEventsStreamData<TLogNewRoundParameters>> {
        return this.$onLog('NewRound', fn);
    }

    onOwnershipTransferRequested (fn?: (event: TClientEventsStreamData<TLogOwnershipTransferRequestedParameters>) => void): ClientEventsStream<TClientEventsStreamData<TLogOwnershipTransferRequestedParameters>> {
        return this.$onLog('OwnershipTransferRequested', fn);
    }

    onOwnershipTransferred (fn?: (event: TClientEventsStreamData<TLogOwnershipTransferredParameters>) => void): ClientEventsStream<TClientEventsStreamData<TLogOwnershipTransferredParameters>> {
        return this.$onLog('OwnershipTransferred', fn);
    }

    extractLogsAnswerUpdated (tx: TEth.TxReceipt): ITxLogItem<TLogAnswerUpdated>[] {
        let abi = this.$getAbiItem('event', 'AnswerUpdated');
        return this.$extractLogs(tx, abi) as any as ITxLogItem<TLogAnswerUpdated>[];
    }

    extractLogsNewRound (tx: TEth.TxReceipt): ITxLogItem<TLogNewRound>[] {
        let abi = this.$getAbiItem('event', 'NewRound');
        return this.$extractLogs(tx, abi) as any as ITxLogItem<TLogNewRound>[];
    }

    extractLogsOwnershipTransferRequested (tx: TEth.TxReceipt): ITxLogItem<TLogOwnershipTransferRequested>[] {
        let abi = this.$getAbiItem('event', 'OwnershipTransferRequested');
        return this.$extractLogs(tx, abi) as any as ITxLogItem<TLogOwnershipTransferRequested>[];
    }

    extractLogsOwnershipTransferred (tx: TEth.TxReceipt): ITxLogItem<TLogOwnershipTransferred>[] {
        let abi = this.$getAbiItem('event', 'OwnershipTransferred');
        return this.$extractLogs(tx, abi) as any as ITxLogItem<TLogOwnershipTransferred>[];
    }

    async getPastLogsAnswerUpdated (options?: {
        fromBlock?: number | Date
        toBlock?: number | Date
        params?: { current?: bigint,roundId?: bigint }
    }): Promise<ITxLogItem<TLogAnswerUpdated>[]> {
        return await this.$getPastLogsParsed('AnswerUpdated', options) as any;
    }

    async getPastLogsNewRound (options?: {
        fromBlock?: number | Date
        toBlock?: number | Date
        params?: { roundId?: bigint,startedBy?: TAddress }
    }): Promise<ITxLogItem<TLogNewRound>[]> {
        return await this.$getPastLogsParsed('NewRound', options) as any;
    }

    async getPastLogsOwnershipTransferRequested (options?: {
        fromBlock?: number | Date
        toBlock?: number | Date
        params?: { from?: TAddress,to?: TAddress }
    }): Promise<ITxLogItem<TLogOwnershipTransferRequested>[]> {
        return await this.$getPastLogsParsed('OwnershipTransferRequested', options) as any;
    }

    async getPastLogsOwnershipTransferred (options?: {
        fromBlock?: number | Date
        toBlock?: number | Date
        params?: { from?: TAddress,to?: TAddress }
    }): Promise<ITxLogItem<TLogOwnershipTransferred>[]> {
        return await this.$getPastLogsParsed('OwnershipTransferred', options) as any;
    }

    abi: TAbiItem[] = [{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"},{"internalType":"address","name":"_accessController","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"int256","name":"current","type":"int256"},{"indexed":true,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"updatedAt","type":"uint256"}],"name":"AnswerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":true,"internalType":"address","name":"startedBy","type":"address"},{"indexed":false,"internalType":"uint256","name":"startedAt","type":"uint256"}],"name":"NewRound","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"OwnershipTransferRequested","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"accessController","outputs":[{"internalType":"contract AccessControllerInterface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"aggregator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"}],"name":"confirmAggregator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"}],"name":"getAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"}],"name":"getTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRound","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"phaseAggregators","outputs":[{"internalType":"contract AggregatorV2V3Interface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phaseId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"}],"name":"proposeAggregator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposedAggregator","outputs":[{"internalType":"contract AggregatorV2V3Interface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"proposedGetRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposedLatestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_accessController","type":"address"}],"name":"setController","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]

    storage: ChainlinkOracleEthStorageReader
}

type TSender = TAccount & {
    value?: string | number | bigint
}

    type TLogAnswerUpdated = {
        current: bigint, roundId: bigint, updatedAt: bigint
    };
    type TLogAnswerUpdatedParameters = [ current: bigint, roundId: bigint, updatedAt: bigint ];
    type TLogNewRound = {
        roundId: bigint, startedBy: TAddress, startedAt: bigint
    };
    type TLogNewRoundParameters = [ roundId: bigint, startedBy: TAddress, startedAt: bigint ];
    type TLogOwnershipTransferRequested = {
        from: TAddress, to: TAddress
    };
    type TLogOwnershipTransferRequestedParameters = [ from: TAddress, to: TAddress ];
    type TLogOwnershipTransferred = {
        from: TAddress, to: TAddress
    };
    type TLogOwnershipTransferredParameters = [ from: TAddress, to: TAddress ];

interface IEvents {
  AnswerUpdated: TLogAnswerUpdatedParameters
  NewRound: TLogNewRoundParameters
  OwnershipTransferRequested: TLogOwnershipTransferRequestedParameters
  OwnershipTransferred: TLogOwnershipTransferredParameters
  '*': any[] 
}



interface IMethodAcceptOwnership {
  method: "acceptOwnership"
  arguments: [  ]
}

interface IMethodAccessController {
  method: "accessController"
  arguments: [  ]
}

interface IMethodAggregator {
  method: "aggregator"
  arguments: [  ]
}

interface IMethodConfirmAggregator {
  method: "confirmAggregator"
  arguments: [ _aggregator: TAddress ]
}

interface IMethodDecimals {
  method: "decimals"
  arguments: [  ]
}

interface IMethodDescription {
  method: "description"
  arguments: [  ]
}

interface IMethodGetAnswer {
  method: "getAnswer"
  arguments: [ _roundId: bigint ]
}

interface IMethodGetRoundData {
  method: "getRoundData"
  arguments: [ _roundId: bigint ]
}

interface IMethodGetTimestamp {
  method: "getTimestamp"
  arguments: [ _roundId: bigint ]
}

interface IMethodLatestAnswer {
  method: "latestAnswer"
  arguments: [  ]
}

interface IMethodLatestRound {
  method: "latestRound"
  arguments: [  ]
}

interface IMethodLatestRoundData {
  method: "latestRoundData"
  arguments: [  ]
}

interface IMethodLatestTimestamp {
  method: "latestTimestamp"
  arguments: [  ]
}

interface IMethodOwner {
  method: "owner"
  arguments: [  ]
}

interface IMethodPhaseAggregators {
  method: "phaseAggregators"
  arguments: [ input0: number ]
}

interface IMethodPhaseId {
  method: "phaseId"
  arguments: [  ]
}

interface IMethodProposeAggregator {
  method: "proposeAggregator"
  arguments: [ _aggregator: TAddress ]
}

interface IMethodProposedAggregator {
  method: "proposedAggregator"
  arguments: [  ]
}

interface IMethodProposedGetRoundData {
  method: "proposedGetRoundData"
  arguments: [ _roundId: bigint ]
}

interface IMethodProposedLatestRoundData {
  method: "proposedLatestRoundData"
  arguments: [  ]
}

interface IMethodSetController {
  method: "setController"
  arguments: [ _accessController: TAddress ]
}

interface IMethodTransferOwnership {
  method: "transferOwnership"
  arguments: [ _to: TAddress ]
}

interface IMethodVersion {
  method: "version"
  arguments: [  ]
}

interface IMethods {
  acceptOwnership: IMethodAcceptOwnership
  accessController: IMethodAccessController
  aggregator: IMethodAggregator
  confirmAggregator: IMethodConfirmAggregator
  decimals: IMethodDecimals
  description: IMethodDescription
  getAnswer: IMethodGetAnswer
  getRoundData: IMethodGetRoundData
  getTimestamp: IMethodGetTimestamp
  latestAnswer: IMethodLatestAnswer
  latestRound: IMethodLatestRound
  latestRoundData: IMethodLatestRoundData
  latestTimestamp: IMethodLatestTimestamp
  owner: IMethodOwner
  phaseAggregators: IMethodPhaseAggregators
  phaseId: IMethodPhaseId
  proposeAggregator: IMethodProposeAggregator
  proposedAggregator: IMethodProposedAggregator
  proposedGetRoundData: IMethodProposedGetRoundData
  proposedLatestRoundData: IMethodProposedLatestRoundData
  setController: IMethodSetController
  transferOwnership: IMethodTransferOwnership
  version: IMethodVersion
  '*': { method: string, arguments: any[] } 
}





class ChainlinkOracleEthStorageReader extends ContractStorageReaderBase {
    constructor(
        public address: TAddress,
        public client: Web3Client,
        public explorer: IBlockChainExplorer,
    ) {
        super(address, client, explorer);

        this.$createHandler(this.$slots);
    }

    async owner(): Promise<TAddress> {
        return this.$storage.get(['owner', ]);
    }

    async pendingOwner(): Promise<TAddress> {
        return this.$storage.get(['pendingOwner', ]);
    }

    async currentPhase(): Promise<{ id: number, aggregator: TAddress }> {
        return this.$storage.get(['currentPhase', ]);
    }

    async proposedAggregator(): Promise<TAddress> {
        return this.$storage.get(['proposedAggregator', ]);
    }

    async phaseAggregators(key: number): Promise<TAddress> {
        return this.$storage.get(['phaseAggregators', key]);
    }

    async accessController(): Promise<TAddress> {
        return this.$storage.get(['accessController', ]);
    }

    $slots = [
    {
        "slot": 0,
        "position": 0,
        "name": "owner",
        "size": 160,
        "type": "address"
    },
    {
        "slot": 1,
        "position": 0,
        "name": "pendingOwner",
        "size": 160,
        "type": "address"
    },
    {
        "slot": 2,
        "position": 0,
        "name": "currentPhase",
        "size": 176,
        "type": "(uint16 id, address aggregator)"
    },
    {
        "slot": 3,
        "position": 0,
        "name": "proposedAggregator",
        "size": 160,
        "type": "address"
    },
    {
        "slot": 4,
        "position": 0,
        "name": "phaseAggregators",
        "size": null,
        "type": "mapping(uint16 => address)"
    },
    {
        "slot": 5,
        "position": 0,
        "name": "accessController",
        "size": 160,
        "type": "address"
    }
]

}



interface IChainlinkOracleEthTxCaller {
    acceptOwnership (sender: TSender, ): Promise<{ error?: Error & { data?: { type: string, params } }, result? }>
    confirmAggregator (sender: TSender, _aggregator: TAddress): Promise<{ error?: Error & { data?: { type: string, params } }, result? }>
    proposeAggregator (sender: TSender, _aggregator: TAddress): Promise<{ error?: Error & { data?: { type: string, params } }, result? }>
    setController (sender: TSender, _accessController: TAddress): Promise<{ error?: Error & { data?: { type: string, params } }, result? }>
    transferOwnership (sender: TSender, _to: TAddress): Promise<{ error?: Error & { data?: { type: string, params } }, result? }>
}


interface IChainlinkOracleEthTxData {
    acceptOwnership (sender: TSender, ): Promise<TEth.TxLike>
    confirmAggregator (sender: TSender, _aggregator: TAddress): Promise<TEth.TxLike>
    proposeAggregator (sender: TSender, _aggregator: TAddress): Promise<TEth.TxLike>
    setController (sender: TSender, _accessController: TAddress): Promise<TEth.TxLike>
    transferOwnership (sender: TSender, _to: TAddress): Promise<TEth.TxLike>
}


