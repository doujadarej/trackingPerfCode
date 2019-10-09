import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.Configuration.RecoLocalTracker_cff import *
from SimGeneral.TrackingAnalysis.simHitTPAssociation_cfi import *
from SimTracker.TrackerHitAssociation.tpClusterProducer_cfi import *
from SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi import *
from RecoTracker.TransientTrackingRecHit.TTRHBuilders_cff import *
from RecoLocalTracker.SiPixelRecHits.PixelCPEGeneric_cfi import *
from SimTracker.TrackAssociation.LhcParametersDefinerForTP_cfi import *


process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load('Configuration.StandardSequences.Services_cff')




process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring( 
#'step3.root'

'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/FA7DB3F4-CD31-E811-89CD-0242AC130002.root'
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/F099EF61-D631-E811-99C3-0242AC130002.root',
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/E293E72C-E131-E811-BA83-0242AC130002.root',
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/D47C1005-D831-E811-A5A4-0242AC130002.root',
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/A260A3F6-CE31-E811-91C4-0242AC130002.root',
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/94F57188-C931-E811-83A8-0242AC130002.root',
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/7E5399CA-D131-E811-9E42-0242AC130002.root',
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/72B19578-CB31-E811-A8A7-0242AC130002.root',
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/3CF2D6AB-D331-E811-863F-0242AC130002.root',
#'root://cms-xrd-global.cern.ch//store/relval/CMSSW_10_1_0_pre3/RelValTTbar_13UP18/GEN-SIM-RECO/PUpmx25ns_101X_upgrade2018_realistic_v3_cc7-v1/10000/36F5941B-CC31-E811-A6FE-0242AC130002.root'
 

    )
)


process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )




from CommonTools.RecoAlgos.trackingParticleRefSelector_cfi import trackingParticleRefSelector as _trackingParticleRefSelector
trackingParticlesIntime = _trackingParticleRefSelector.clone(
    signalOnly = False,
    intimeOnly = True,
    chargedOnly = False,
    tip = 1e5,
    lip = 1e5,
    minRapidity = -10,
    maxRapidity = 10,
    ptMin = 0,
)






process.trackingPerf = cms.EDAnalyzer('TrackingPerf',
      tracks               = cms.untracked.InputTag('generalTracks'),
      trackLabel           = cms.untracked.InputTag('generalTracks'),
      trackAssociator      = cms.untracked.InputTag('trackingParticleRecoTrackAsssociation'),
      beamSpot             = cms.untracked.InputTag('offlineBeamSpot'),
      parametersDefiner    = cms.string('LhcParametersDefinerForTP'),
      trackingParticles    = cms.untracked.InputTag('trackingParticlesIntime'),
      trackingParticlesRef = True
)


process.p = cms.Path(trackingParticlesIntime*simHitTPAssocProducer*tpClusterProducer*process.trackingPerf)
