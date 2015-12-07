# PySNMP SMI module. Autogenerated from smidump -f python CISCO-TC
# by libsmi2pysnmp-0.1.3 at Sat Dec  5 22:31:20 2015,
# Python version sys.version_info(major=2, minor=7, micro=9, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ciscoModules, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
( Bits, Counter64, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class BulkConfigResult(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    
class Cisco2KVlanList(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)
    
class CiscoAlarmSeverity(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(4,6,1,7,2,3,5,)
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6), ("info", 7), )
    
class CiscoBridgeDomain(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,65535)
    
class CiscoCosList(Bits):
    namedValues = NamedValues(("cos0", 0), ("cos1", 1), ("cos2", 2), ("cos3", 3), ("cos4", 4), ("cos5", 5), ("cos6", 6), ("cos7", 7), )
    
class CiscoEntityIndexList(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)
    
class CiscoHTTPResponseStatusCode(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(100,599)
    
class CiscoInetAddressMask(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,128)
    
class CiscoInterfaceIndexList(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)
    
class CiscoIpProtocol(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,255)
    
class CiscoLocationClass(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(6,2,8,1,5,3,4,7,)
    namedValues = NamedValues(("chassis", 1), ("shelf", 2), ("slot", 3), ("subSlot", 4), ("port", 5), ("subPort", 6), ("channel", 7), ("subChannel", 8), )
    
class CiscoLocationSpecifier(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    
class CiscoMilliSeconds(Unsigned32):
    pass

class CiscoNetworkAddress(OctetString):
    pass

class CiscoNetworkProtocol(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(11,23,1,9,18,22,17,65535,4,21,6,20,19,13,25,8,2,14,12,3,5,24,10,7,16,15,)
    namedValues = NamedValues(("ip", 1), ("vines", 10), ("cons", 11), ("apollo", 12), ("stun", 13), ("novell", 14), ("qllc", 15), ("snapshot", 16), ("atmIlmi", 17), ("bstun", 18), ("x25pvc", 19), ("decnet", 2), ("ipv6", 20), ("cdm", 21), ("nbf", 22), ("bpxIgx", 23), ("clnsPfx", 24), ("http", 25), ("pup", 3), ("chaos", 4), ("xns", 5), ("x121", 6), ("unknown", 65535), ("appletalk", 7), ("clns", 8), ("lat", 9), )
    
class CiscoPbbServiceIdentifier(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,16777216)
    
class CiscoPort(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,65535)
    
class CiscoPortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,256)
    
class CiscoPortListRange(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(4,7,5,8,6,1,3,2,)
    namedValues = NamedValues(("oneto2k", 1), ("twoKto4K", 2), ("fourKto6K", 3), ("sixKto8K", 4), ("eightKto10K", 5), ("tenKto12K", 6), ("twelveKto14K", 7), ("fourteenKto16K", 8), )
    
class CiscoRowOperStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(3,2,1,4,)
    namedValues = NamedValues(("active", 1), ("activeDependencies", 2), ("inactiveDependency", 3), ("missingDependency", 4), )
    
class CiscoSnapShotAbsCounter32(Unsigned32):
    pass

class CiscoURLString(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)
    
class CiscoURLStringOrEmpty(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    
class CiscoVlanList(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,128)
    
class CiscoVrfName(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,32)
    
class ConfigIterator(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)
    
class CountryCode(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(2,2),)
    
class CountryCodeITU(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,255)
    
class CvE164Address(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,128)
    
class EntLogicalIndexOrZero(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class EntPhysicalIndexOrZero(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class IfOperStatusReason(Integer):
    subtypeSpec = Integer.subtypeSpec+ConstraintsUnion(SingleValueConstraint(158,228,39,108,196,99,216,249,30,151,266,93,209,21,184,44,19,136,16,118,156,119,104,67,45,225,35,23,210,10,109,54,180,84,142,155,257,227,175,147,246,56,75,173,6,149,27,13,22,65,105,60,82,18,205,236,145,11,157,218,234,204,128,152,106,229,251,66,120,211,223,213,59,72,14,139,48,146,239,254,40,5,182,81,188,169,89,233,123,240,242,192,177,117,238,98,68,36,76,198,171,110,8,215,230,222,49,134,95,232,111,250,207,25,241,187,101,51,194,3,69,203,15,127,244,176,248,), SingleValueConstraint(255,96,121,32,159,64,174,172,231,220,135,202,87,53,28,52,160,170,154,62,261,4,79,131,163,206,91,144,85,262,253,77,73,112,256,243,24,26,46,71,88,61,263,165,265,113,107,90,94,179,258,264,164,74,2,47,20,137,12,63,124,245,199,83,162,29,195,237,116,183,126,133,186,168,130,153,197,260,212,201,103,178,259,191,92,132,34,150,247,114,217,224,200,140,148,267,86,7,57,70,80,219,138,1,100,208,9,252,143,115,55,97,214,38,102,161,190,221,235,41,167,181,37,122,268,58,78,), SingleValueConstraint(33,141,166,226,189,42,185,31,129,125,17,43,193,50,))
    namedValues = NamedValues(("other", 1), ("initializing", 10), ("ohmsExtLoopbackTest", 100), ("invalidFabricBindExchange", 101), ("tovMismatch", 102), ("ficonNotEnabled", 103), ("ficonNoPortNumber", 104), ("ficonBeingEnabled", 105), ("ePortProhibited", 106), ("portGracefulShutdown", 107), ("trunkNotFullyActive", 108), ("fabricBindingSwitchWwnNotFound", 109), ("vsanInactive", 11), ("fabricBindingDomainInvalid", 110), ("fabricBindingDbMismatch", 111), ("fabricBindingNoRspFromPeer", 112), ("dpvmVsanSuspended", 113), ("dpvmVsanNotFound", 114), ("trackedPortDown", 115), ("ecSuspendedOnLoop", 116), ("isolateBundleMisCfg", 117), ("noPeerBundleSupport", 118), ("portBringupIsolation", 119), ("adminDown", 12), ("domainNotAllowedIsolated", 120), ("virtualIvrDomainOverlapIsolation", 121), ("outOfService", 122), ("portAuthFailed", 123), ("bundleStandby", 124), ("portConnectorTypeErr", 125), ("errorDisabledReInitLmtReached", 126), ("ficonDupPortNum", 127), ("localRcf", 128), ("twoSwitchesWithSameWWN", 129), ("channelAdminDown", 13), ("invalidOtherSidePrincEFPReqRecd", 130), ("domainOther", 131), ("elpFailureAllZeroPeerWWNRcvd", 132), ("preferredPathIsolation", 133), ("fcRedirectIsolation", 134), ("portActLicenseNotAvailable", 135), ("sdmIsolation", 136), ("fcidAllocationFailed", 137), ("externallyDisabled", 138), ("unavailableNPVUpstreamPort", 139), ("channelOperSuspended", 14), ("unavailableNPVPrefUpstreamPort", 140), ("sfpReadError", 141), ("stickyDownOnLinkFailure", 142), ("tooManyLinkFlapsErr", 143), ("unidirectionalUDLD", 144), ("txRxLoopUDLD", 145), ("neighborMismatchUDLD", 146), ("authzPending", 147), ("hotStdbyInBundle", 148), ("incompleteConfig", 149), ("channelConfigurationInProgress", 15), ("incompleteTunnelCfg", 150), ("hwProgrammingFailed", 151), ("tunnelDstUnreachable", 152), ("suspendByMtu", 153), ("sfpInvalid", 154), ("sfpAbsent", 155), ("portCapabilitiesUnknown", 156), ("channelErrDisabled", 157), ("vrfMismatch", 158), ("vrfForwardReferencing", 159), ("rcfInProgress", 16), ("dupTunnelConfigDetected", 160), ("primaryVLANDown", 161), ("vrfUnusable", 162), ("errDisableHandShkFailure", 163), ("errDisabledBPDUGuard", 164), ("dot1xSecViolationErrDisabled", 165), ("emptyEchoUDLD", 166), ("vfTaggingCapErr", 167), ("portDisabled", 168), ("tunnelModeNotConfigured", 169), ("elpFailureIsolation", 17), ("tunnelSrcNotConfigured", 170), ("tunnelDstNotConfigured", 171), ("tunnelUnableToResolveSrcIP", 172), ("tunnelUnableToResolveDstIP", 173), ("tunnelVrfDown", 174), ("sifAdminDown", 175), ("phyIntfDown", 176), ("ifSifLimitExceeded", 177), ("sifHoldDown", 178), ("noFcoe", 179), ("escFailureIsolation", 18), ("dcxCompatMismatch", 180), ("isolateBundleLimitExceeded", 181), ("sifNotBound", 182), ("errDisabledLacpMiscfg", 183), ("satFabricIfDown", 184), ("invalidSatFabricIf", 185), ("noRemoteChassis", 186), ("vicEnableNotReceived", 187), ("vicDisableReceived", 188), ("vlanVsanMappingNotEnabled", 189), ("domainOverlapIsolation", 19), ("stpNotFwdingInFcoeMappedVlan", 190), ("moduleOffline", 191), ("udldAggModeLinkFailure", 192), ("stpInconsVpcPeerDisabled", 193), ("setPortStateFailed", 194), ("suspendedByVpc", 195), ("vpcCfgInProgress", 196), ("vpcPeerLinkDown", 197), ("vpcNoRspFromPeer", 198), ("protoPortSuspend", 199), ("none", 2), ("domainAddrAssignFailureIsolation", 20), ("tunnelSrcDown", 200), ("cdpInfoUnavailable", 201), ("fexSfpInvalid", 202), ("errDisabledIpConflict", 203), ("fcotClkRateMismatch", 204), ("portGuardTrustSecViolation", 205), ("sdpTimeout", 206), ("satIncompatTopo", 207), ("waitForFlogi", 208), ("satNotConfigured", 209), ("domainOtherSideEportIsolation", 21), ("npivNotEnabledInUpstream", 210), ("vsanMismatchWithUpstreamSwPort", 211), ("portGuardBitErrRate", 212), ) + NamedValues(("portGuardSigLoss", 213), ("portGuardSyncLoss", 214), ("portGuardLinkReset", 215), ("portGuardCreditLoss", 216), ("ipQosMgrPolicyAppFailure", 217), ("pauseRateLimitErrDisabled", 218), ("lstGrpUplinkDown", 219), ("domainInvalidRcfReceived", 22), ("stickyDnLinkFailure", 220), ("routerMacFailure", 221), ("dcxMultipleMsapIds", 222), ("dcxHundredPdusRcvdNoAck", 223), ("enmSatIncompatibleUplink", 224), ("enmLoopDetected", 225), ("nonStickyExternallyDisabled", 226), ("subGroupIdNotAssigned", 227), ("vemUnlicensed", 228), ("profileNotFound", 229), ("domainManagerDisabled", 23), ("nonExistentVlan", 230), ("vlanInvalidType", 231), ("vlanDown", 232), ("vpcPeerUpgrade", 233), ("ipQosDcbxpCompatFailure", 234), ("nonCiscoHbaVfTag", 235), ("domainIdConfigMismatch", 236), ("sfpSpeedMismatch", 237), ("xcvrInitializing", 238), ("xcvrAbsent", 239), ("zoneMergeFailureIsolation", 24), ("xcvrInvalid", 240), ("vfcBindingInvalid", 241), ("vlanNotFcoeEnabled", 242), ("pvlanNativeVlanErr", 243), ("ethL2VlanDown", 244), ("ethIntfInvalidBinding", 245), ("pmonFailure", 246), ("l3NotReady", 247), ("speedMismatch", 248), ("flowControlMismatch", 249), ("vsanMismatchIsolation", 25), ("vdcMode", 250), ("suspendedDueToMinLinks", 251), ("enmPinFailLinkDown", 252), ("inactiveM1PortFpathActiveVlan", 253), ("parentPortDown", 254), ("moduleRemoved", 255), ("corePortMct", 256), ("nonCorePortMct", 257), ("ficonInorderNotActive", 258), ("invalidEncapsulation", 259), ("parentDown", 26), ("modemLineDeasserted", 260), ("ipSecHndshkInProgress", 261), ("sfpEthCompliantErr", 262), ("cellularModemUnattached", 263), ("outOfGlblRxBuffers", 264), ("sfpFcCompliantErr", 265), ("ethIntfNotLicensed", 266), ("domainIdsInvalid", 267), ("fabricNameInvalid", 268), ("srcPortNotBound", 27), ("interfaceRemoved", 28), ("fcotNotPresent", 29), ("hwFailure", 3), ("fcotVendorNotSupported", 30), ("incompatibleAdminMode", 31), ("incompatibleAdminSpeed", 32), ("suspendedByMode", 33), ("suspendedBySpeed", 34), ("suspendedByWWN", 35), ("domainMaxReTxFailure", 36), ("eppFailure", 37), ("portVsanMismatchIsolation", 38), ("loopbackIsolation", 39), ("loopbackDiagFailure", 4), ("upgradeInProgress", 40), ("incompatibleAdminRxBbCredit", 41), ("incompatibleAdminRxBufferSize", 42), ("portChannelMembersDown", 43), ("zoneRemoteNoRespIsolation", 44), ("firstPortUpAsEport", 45), ("firstPortNotUp", 46), ("peerFCIPPortClosedConnection", 47), ("peerFCIPPortResetConnection", 48), ("fcipPortMaxReTx", 49), ("errorDisabled", 5), ("fcipPortKeepAliveTimerExpire", 50), ("fcipPortPersistTimerExpire", 51), ("fcipPortSrcLinkDown", 52), ("fcipPortSrcAdminDown", 53), ("fcipPortAdminCfgChange", 54), ("fcipSrcPortRemoved", 55), ("fcipSrcModuleNotOnline", 56), ("invalidConfig", 57), ("portBindFailure", 58), ("portFabricBindFailure", 59), ("swFailure", 6), ("noCommonVsanIsolation", 60), ("ficonVsanDown", 61), ("invalidAttachment", 62), ("portBlocked", 63), ("incomAdminRxBbCreditPerBuf", 64), ("tooManyInvalidFlogis", 65), ("deniedDueToPortBinding", 66), ("elpFailureRevMismatch", 67), ("elpFailureClassFParamErr", 68), ("elpFailureClassNParamErr", 69), ("linkFailure", 7), ("elpFailureUnknownFlowCtlCode", 70), ("elpFailureInvalidFlowCtlParam", 71), ("elpFailureInvalidPortName", 72), ("elpFailureInvalidSwitchName", 73), ("elpFailureRatovEdtovMismatch", 74), ("elpFailureLoopbackDetected", 75), ("elpFailureInvalidTxBbCredit", 76), ("elpFailureInvalidPayloadSize", 77), ("bundleMisCfg", 78), ("bitErrRuntimeThreshExceeded", 79), ("offline", 8), ("linkFailLinkReset", 80), ("linkFailPortInitFail", 81), ("linkFailPortUnusable", 82), ("linkFailLossOfSignal", 83), ("linkFailLossOfSync", 84), ("linkFailNosRcvd", 85), ("linkFailOLSRcvd", 86), ) + NamedValues(("linkFailDebounceTimeout", 87), ("linkFailLrRcvd", 88), ("linkFailCreditLoss", 89), ("nonParticipating", 9), ("linkFailRxQOverflow", 90), ("linkFailTooManyInterrupts", 91), ("linkFailLipRcvdBb", 92), ("linkFailBbCreditLoss", 93), ("linkFailOpenPrimSignalTimeout", 94), ("linkFailOpenPrimSignalReturned", 95), ("linkFailLipF8Rcvd", 96), ("linkFailLineCardPortShutdown", 97), ("fcspAuthenfailure", 98), ("fcotChecksumError", 99), )
    
class InterfaceIndexOrZero(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class Layer2Cos(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,7)
    
class ListIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,2147483647)
    
class ListIndexOrZero(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,2147483647)
    
class MicroSeconds(Unsigned32):
    pass

class SAPType(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,254)
    
class TimeIntervalMin(Unsigned32):
    pass

class TimeIntervalSec(Unsigned32):
    pass

class CiscoAbsZeroBasedCounter32(Gauge32):
    pass

class PerfHighIntervalCount(Counter64):
    pass

class Unsigned64(Counter64):
    pass


# Objects

ciscoTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 1)).setRevisions(("2011-11-11 00:00","2011-06-17 00:00","2010-02-24 00:00","2009-06-18 00:00","2009-03-10 00:00","2009-02-26 00:00","2008-04-02 00:00","2007-02-15 00:00","2006-07-06 00:00","2006-04-13 00:00","2005-06-24 00:00","2005-06-16 00:00","2004-10-11 00:00","2004-06-08 00:00","2004-04-14 00:00","2002-12-18 00:00","2002-12-12 16:00","2002-12-02 00:00","2002-09-22 00:00","2002-09-17 00:00","2002-04-16 00:00","2001-07-07 00:00","2001-01-18 00:00","2000-11-21 00:00","1998-10-28 00:00","1997-03-13 00:00","1996-08-14 00:00","1996-07-08 00:00","1996-02-22 00:00","1995-06-07 00:00",))
if mibBuilder.loadTexts: ciscoTextualConventions.setOrganization("Cisco Systems, Inc.")
if mibBuilder.loadTexts: ciscoTextualConventions.setContactInfo("Cisco Systems\nCustomer Service\n\nPostal: 170 W Tasman Drive\nSan Jose, CA  95134\nUSA\n\nTel: +1 800 553-NETS\n\nE-mail: cs-snmp@cisco.com")
if mibBuilder.loadTexts: ciscoTextualConventions.setDescription("This module defines textual conventions used throughout\ncisco enterprise mibs.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-TC", PYSNMP_MODULE_ID=ciscoTextualConventions)

# Types
mibBuilder.exportSymbols("CISCO-TC", BulkConfigResult=BulkConfigResult, Cisco2KVlanList=Cisco2KVlanList, CiscoAlarmSeverity=CiscoAlarmSeverity, CiscoBridgeDomain=CiscoBridgeDomain, CiscoCosList=CiscoCosList, CiscoEntityIndexList=CiscoEntityIndexList, CiscoHTTPResponseStatusCode=CiscoHTTPResponseStatusCode, CiscoInetAddressMask=CiscoInetAddressMask, CiscoInterfaceIndexList=CiscoInterfaceIndexList, CiscoIpProtocol=CiscoIpProtocol, CiscoLocationClass=CiscoLocationClass, CiscoLocationSpecifier=CiscoLocationSpecifier, CiscoMilliSeconds=CiscoMilliSeconds, CiscoNetworkAddress=CiscoNetworkAddress, CiscoNetworkProtocol=CiscoNetworkProtocol, CiscoPbbServiceIdentifier=CiscoPbbServiceIdentifier, CiscoPort=CiscoPort, CiscoPortList=CiscoPortList, CiscoPortListRange=CiscoPortListRange, CiscoRowOperStatus=CiscoRowOperStatus, CiscoSnapShotAbsCounter32=CiscoSnapShotAbsCounter32, CiscoURLString=CiscoURLString, CiscoURLStringOrEmpty=CiscoURLStringOrEmpty, CiscoVlanList=CiscoVlanList, CiscoVrfName=CiscoVrfName, ConfigIterator=ConfigIterator, CountryCode=CountryCode, CountryCodeITU=CountryCodeITU, CvE164Address=CvE164Address, EntLogicalIndexOrZero=EntLogicalIndexOrZero, EntPhysicalIndexOrZero=EntPhysicalIndexOrZero, IfOperStatusReason=IfOperStatusReason, InterfaceIndexOrZero=InterfaceIndexOrZero, Layer2Cos=Layer2Cos, ListIndex=ListIndex, ListIndexOrZero=ListIndexOrZero, MicroSeconds=MicroSeconds, SAPType=SAPType, TimeIntervalMin=TimeIntervalMin, TimeIntervalSec=TimeIntervalSec, CiscoAbsZeroBasedCounter32=CiscoAbsZeroBasedCounter32, PerfHighIntervalCount=PerfHighIntervalCount, Unsigned64=Unsigned64)

# Objects
mibBuilder.exportSymbols("CISCO-TC", ciscoTextualConventions=ciscoTextualConventions)

