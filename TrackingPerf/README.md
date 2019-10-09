# TrackingPerf


//recipe to download and install the code, here is an example for the CMSSW version 9_2_8

cmsrel CMSSW_9_2_8

cd CMSSW_9_2_8/src

cmsenv

git clone https://github.com/jandrea/TrackingPerf.git

scramv1 b -j4

// to excecute the code and produce the ntuple :

cd TrackingPerf/TrackingPerf/test

cmsRun TrackingPerf_cfg.py

// the TrackingPerf_cfg.py is a python configuration file, the tells CMSSW what to do
// it is constitued from several "modules", some of them loaded with the "process.load" command, so defined elsewhere
// and some modules are defined directly in this python file, such as "process.trackingPerf", which is the code producing the ntuple.

// a few information about the various modules in the python confiburation files :

  -  process.GlobalTag : load the calibration of the detector for the reconstruction. There are different calibrations for different kind of events : data or MC, for different version of CMSSW etc... When reading another sample, one has to make sure the correct globat tag is used. The list of global tags can be found here :
  
  https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions
  
  - process.source  : should contain the list of root files that the code will read. 
    * If the root files are on the gride, the file name and it paths should be preceded by 
        "root://cms-xrd-global.cern.ch/"
    * If the file is on a local disk, simply do 
        "file:/path/to/the/file/filename.root"

  - process.TFileService : define the name of the ouput root file, where the tree will be written,
  
  - process.mix, process.tpClusterProducer, process.quickTrackAssociatorByHits : are the modules which are  1) producting "TrackingParticle" collections from SimTracks (this is another format for simTracks information),  2) performing the TrackingParticle to reconstructed Tracks association and produce association maps.
  
  - process.trackingPerf : is the module that produce the ntuple from the reco tracks, the TrackingParticle maps. It also reads jets, primavy vertices and beam spot.
  
// process.trackingPerf is an EDAnalyzer module, which means that it is a use kind of code that reads CMSSW events and perform some analysis. The trackingPerf module is define in the following files 
  
TrackingPerf/TrackingPerf/plugins/TrackingPerf.cc

//Details are given as comments in the file directly.

  
  
  
