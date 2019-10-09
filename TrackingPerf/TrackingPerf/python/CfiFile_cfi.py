import FWCore.ParameterSet.Config as cms

demo = cms.EDAnalyzer('TrackingPerf'
     ,tracks = cms.untracked.InputTag('ctfWithMaterialTracks')
)
