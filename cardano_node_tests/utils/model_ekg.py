# generated by datamodel-codegen:
#   filename:  ekg.json
#   timestamp: 2021-03-10T11:38:36+00:00
from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field


class IohkMonitoringVersion(BaseModel):
    val: str
    type: str


class Int(BaseModel):
    val: int
    type: str


class NodeIsLeaderNum(BaseModel):
    int: Int


class Int1(BaseModel):
    val: int
    type: str


class BlockNum(BaseModel):
    int: Int1


class Int2(BaseModel):
    val: int
    type: str


class BlocksForgedNum(BaseModel):
    int: Int2


class Int3(BaseModel):
    val: int
    type: str


class Epoch(BaseModel):
    int: Int3


class Int4(BaseModel):
    val: int
    type: str


class NodeIsLeader(BaseModel):
    int: Int4


class Int5(BaseModel):
    val: int
    type: str


class NodeNotLeader(BaseModel):
    int: Int5


class Int6(BaseModel):
    val: int
    type: str


class Forged(BaseModel):
    int: Int6


class Int7(BaseModel):
    val: int
    type: str


class Adopted(BaseModel):
    int: Int7


class Int8(BaseModel):
    val: int
    type: str


class ForgeAboutToLead(BaseModel):
    int: Int8


class Forge(BaseModel):
    node_is_leader: NodeIsLeader = Field(..., alias="node-is-leader")
    node_not_leader: NodeNotLeader = Field(..., alias="node-not-leader")
    forged: Forged
    adopted: Adopted
    forge_about_to_lead: ForgeAboutToLead = Field(..., alias="forge-about-to-lead")


class Int9(BaseModel):
    val: int
    type: str


class CurrentKESPeriod(BaseModel):
    int: Int9


class Int10(BaseModel):
    val: int
    type: str


class MyBlocksUncoupled(BaseModel):
    int: Int10


class Int11(BaseModel):
    val: int
    type: str


class TxsProcessedNum(BaseModel):
    int: Int11


class Real(BaseModel):
    val: str
    type: str


class Density(BaseModel):
    real: Real


class Int12(BaseModel):
    val: int
    type: str


class NodeStartTime(BaseModel):
    int: Int12


class Int13(BaseModel):
    val: int
    type: str


class Resident(BaseModel):
    int: Int13


class Mem(BaseModel):
    resident: Resident


class Int14(BaseModel):
    val: int
    type: str


class OperationalCertificateStartKESPeriod(BaseModel):
    int: Int14


class Int15(BaseModel):
    val: int
    type: str


class OperationalCertificateExpiryKESPeriod(BaseModel):
    int: Int15


class Int16(BaseModel):
    val: int
    type: str


class RemainingKESPeriods(BaseModel):
    int: Int16


class Int17(BaseModel):
    val: int
    type: str


class TxsInMempool(BaseModel):
    int: Int17


class Int18(BaseModel):
    val: int
    type: str


class DelegMapSize(BaseModel):
    int: Int18


class Int19(BaseModel):
    val: int
    type: str


class UtxoSize(BaseModel):
    int: Int19


class Int20(BaseModel):
    val: int
    type: str


class Counter(BaseModel):
    int: Int20


class Header(BaseModel):
    counter: Counter


class Served(BaseModel):
    header: Header


class Int21(BaseModel):
    val: int
    type: str


class MempoolBytes(BaseModel):
    int: Int21


class Int22(BaseModel):
    val: int
    type: str


class GcMajorNum(BaseModel):
    int: Int22


class Int23(BaseModel):
    val: int
    type: str


class GcLiveBytes(BaseModel):
    int: Int23


class Int24(BaseModel):
    val: int
    type: str


class GcMinorNum(BaseModel):
    int: Int24


class Int25(BaseModel):
    val: int
    type: str


class Mutticks(BaseModel):
    int: Int25


class Int26(BaseModel):
    val: int
    type: str


class Gcticks(BaseModel):
    int: Int26


class RTS(BaseModel):
    gcMajorNum: GcMajorNum
    gcLiveBytes: GcLiveBytes
    gcMinorNum: GcMinorNum
    mutticks: Mutticks
    gcticks: Gcticks


class Int27(BaseModel):
    val: int
    type: str


class SlotInEpoch(BaseModel):
    int: Int27


class Int28(BaseModel):
    val: int
    type: str


class SlotNum(BaseModel):
    int: Int28


class Int29(BaseModel):
    val: int
    type: str


class Cputicks(BaseModel):
    int: Int29


class Int30(BaseModel):
    val: int
    type: str


class Threads(BaseModel):
    int: Int30


class Stat(BaseModel):
    cputicks: Cputicks
    threads: Threads


class Metrics(BaseModel):
    nodeIsLeaderNum: NodeIsLeaderNum
    blockNum: BlockNum
    blocksForgedNum: BlocksForgedNum
    epoch: Epoch
    Forge: Forge
    currentKESPeriod: CurrentKESPeriod
    myBlocksUncoupled: MyBlocksUncoupled
    txsProcessedNum: TxsProcessedNum
    density: Density
    nodeStartTime: NodeStartTime
    Mem: Mem
    operationalCertificateStartKESPeriod: OperationalCertificateStartKESPeriod
    operationalCertificateExpiryKESPeriod: OperationalCertificateExpiryKESPeriod
    remainingKESPeriods: RemainingKESPeriods
    txsInMempool: TxsInMempool
    delegMapSize: DelegMapSize
    utxoSize: UtxoSize
    served: Served
    mempoolBytes: MempoolBytes
    RTS: RTS
    slotInEpoch: SlotInEpoch
    slotNum: SlotNum
    Stat: Stat


class Node(BaseModel):
    metrics: Metrics


class Cardano(BaseModel):
    node: Node


class ServerTimestampMs(BaseModel):
    val: int
    type: str


class Ekg(BaseModel):
    server_timestamp_ms: ServerTimestampMs


class BytesAllocated(BaseModel):
    val: int
    type: str


class MutatorCpuMs(BaseModel):
    val: int
    type: str


class GcWallMs(BaseModel):
    val: int
    type: str


class PeakMegabytesAllocated(BaseModel):
    val: int
    type: str


class ParTotBytesCopied(BaseModel):
    val: int
    type: str


class CumulativeBytesUsed(BaseModel):
    val: int
    type: str


class ParMaxBytesCopied(BaseModel):
    val: int
    type: str


class InitWallMs(BaseModel):
    val: int
    type: str


class MaxBytesUsed(BaseModel):
    val: int
    type: str


class BytesCopied(BaseModel):
    val: int
    type: str


class WallMs(BaseModel):
    val: int
    type: str


class CpuMs(BaseModel):
    val: int
    type: str


class CurrentBytesUsed(BaseModel):
    val: int
    type: str


class GcCpuMs(BaseModel):
    val: int
    type: str


class MutatorWallMs(BaseModel):
    val: int
    type: str


class ParAvgBytesCopied(BaseModel):
    val: int
    type: str


class NumGcs(BaseModel):
    val: int
    type: str


class CurrentBytesSlop(BaseModel):
    val: int
    type: str


class NumBytesUsageSamples(BaseModel):
    val: int
    type: str


class MaxBytesSlop(BaseModel):
    val: int
    type: str


class InitCpuMs(BaseModel):
    val: int
    type: str


class Gc(BaseModel):
    bytes_allocated: BytesAllocated
    mutator_cpu_ms: MutatorCpuMs
    gc_wall_ms: GcWallMs
    peak_megabytes_allocated: PeakMegabytesAllocated
    par_tot_bytes_copied: ParTotBytesCopied
    cumulative_bytes_used: CumulativeBytesUsed
    par_max_bytes_copied: ParMaxBytesCopied
    init_wall_ms: InitWallMs
    max_bytes_used: MaxBytesUsed
    bytes_copied: BytesCopied
    wall_ms: WallMs
    cpu_ms: CpuMs
    current_bytes_used: CurrentBytesUsed
    gc_cpu_ms: GcCpuMs
    mutator_wall_ms: MutatorWallMs
    par_avg_bytes_copied: ParAvgBytesCopied
    num_gcs: NumGcs
    current_bytes_slop: CurrentBytesSlop
    num_bytes_usage_samples: NumBytesUsageSamples
    max_bytes_slop: MaxBytesSlop
    init_cpu_ms: InitCpuMs


class Rts(BaseModel):
    gc: Gc


class Model(BaseModel):
    iohk_monitoring_version: IohkMonitoringVersion = Field(..., alias="iohk-monitoring version")
    cardano: Cardano
    ekg: Ekg
    rts: Rts
