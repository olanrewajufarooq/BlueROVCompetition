
"use strict";

let Param = require('./Param.js');
let RadioStatus = require('./RadioStatus.js');
let ESCStatus = require('./ESCStatus.js');
let GPSRTK = require('./GPSRTK.js');
let ManualControl = require('./ManualControl.js');
let RCIn = require('./RCIn.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let HilSensor = require('./HilSensor.js');
let TerrainReport = require('./TerrainReport.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let RCOut = require('./RCOut.js');
let VFR_HUD = require('./VFR_HUD.js');
let WaypointList = require('./WaypointList.js');
let ActuatorControl = require('./ActuatorControl.js');
let HilGPS = require('./HilGPS.js');
let GPSRAW = require('./GPSRAW.js');
let ExtendedState = require('./ExtendedState.js');
let Altitude = require('./Altitude.js');
let MountControl = require('./MountControl.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let BatteryStatus = require('./BatteryStatus.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let HilControls = require('./HilControls.js');
let DebugValue = require('./DebugValue.js');
let Vibration = require('./Vibration.js');
let HomePosition = require('./HomePosition.js');
let ParamValue = require('./ParamValue.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let LogData = require('./LogData.js');
let Tunnel = require('./Tunnel.js');
let Waypoint = require('./Waypoint.js');
let FileEntry = require('./FileEntry.js');
let Mavlink = require('./Mavlink.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let VehicleInfo = require('./VehicleInfo.js');
let PositionTarget = require('./PositionTarget.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let WaypointReached = require('./WaypointReached.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let CommandCode = require('./CommandCode.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let StatusText = require('./StatusText.js');
let LogEntry = require('./LogEntry.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let Trajectory = require('./Trajectory.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let Thrust = require('./Thrust.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let RTCM = require('./RTCM.js');
let ESCInfo = require('./ESCInfo.js');
let State = require('./State.js');
let RTKBaseline = require('./RTKBaseline.js');
let LandingTarget = require('./LandingTarget.js');
let GPSINPUT = require('./GPSINPUT.js');

module.exports = {
  Param: Param,
  RadioStatus: RadioStatus,
  ESCStatus: ESCStatus,
  GPSRTK: GPSRTK,
  ManualControl: ManualControl,
  RCIn: RCIn,
  AttitudeTarget: AttitudeTarget,
  HilSensor: HilSensor,
  TerrainReport: TerrainReport,
  OverrideRCIn: OverrideRCIn,
  NavControllerOutput: NavControllerOutput,
  HilStateQuaternion: HilStateQuaternion,
  OpticalFlowRad: OpticalFlowRad,
  CameraImageCaptured: CameraImageCaptured,
  ESCTelemetryItem: ESCTelemetryItem,
  RCOut: RCOut,
  VFR_HUD: VFR_HUD,
  WaypointList: WaypointList,
  ActuatorControl: ActuatorControl,
  HilGPS: HilGPS,
  GPSRAW: GPSRAW,
  ExtendedState: ExtendedState,
  Altitude: Altitude,
  MountControl: MountControl,
  ESCInfoItem: ESCInfoItem,
  BatteryStatus: BatteryStatus,
  ADSBVehicle: ADSBVehicle,
  HilControls: HilControls,
  DebugValue: DebugValue,
  Vibration: Vibration,
  HomePosition: HomePosition,
  ParamValue: ParamValue,
  CamIMUStamp: CamIMUStamp,
  LogData: LogData,
  Tunnel: Tunnel,
  Waypoint: Waypoint,
  FileEntry: FileEntry,
  Mavlink: Mavlink,
  HilActuatorControls: HilActuatorControls,
  CompanionProcessStatus: CompanionProcessStatus,
  VehicleInfo: VehicleInfo,
  PositionTarget: PositionTarget,
  WheelOdomStamped: WheelOdomStamped,
  TimesyncStatus: TimesyncStatus,
  WaypointReached: WaypointReached,
  OnboardComputerStatus: OnboardComputerStatus,
  GlobalPositionTarget: GlobalPositionTarget,
  CommandCode: CommandCode,
  PlayTuneV2: PlayTuneV2,
  StatusText: StatusText,
  LogEntry: LogEntry,
  ESCTelemetry: ESCTelemetry,
  Trajectory: Trajectory,
  EstimatorStatus: EstimatorStatus,
  Thrust: Thrust,
  MagnetometerReporter: MagnetometerReporter,
  ESCStatusItem: ESCStatusItem,
  RTCM: RTCM,
  ESCInfo: ESCInfo,
  State: State,
  RTKBaseline: RTKBaseline,
  LandingTarget: LandingTarget,
  GPSINPUT: GPSINPUT,
};
