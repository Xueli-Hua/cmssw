import FWCore.ParameterSet.Config as cms

l1tStage2uGMTEmul = cms.EDAnalyzer(
    "L1TStage2uGMT",
    bmtfProducer = cms.InputTag("gmtStage2Digis", "BMTF"), # not used for emulator DQM
    omtfProducer = cms.InputTag("gmtStage2Digis", "OMTF"), # not used for emulator DQM
    emtfProducer = cms.InputTag("gmtStage2Digis", "EMTF"), # not used for emulator DQM
    muonProducer = cms.InputTag("valGmtStage2Digis", "Muon"),
    monitorDir = cms.untracked.string("L1T2016EMU/L1TdeStage2uGMT"),
    emulator = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
)

