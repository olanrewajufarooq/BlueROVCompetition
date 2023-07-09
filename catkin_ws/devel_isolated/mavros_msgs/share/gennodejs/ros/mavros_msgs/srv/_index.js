
"use strict";

let SetMavFrame = require('./SetMavFrame.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let FileTruncate = require('./FileTruncate.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let WaypointPush = require('./WaypointPush.js')
let FileWrite = require('./FileWrite.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let FileMakeDir = require('./FileMakeDir.js')
let CommandInt = require('./CommandInt.js')
let StreamRate = require('./StreamRate.js')
let SetMode = require('./SetMode.js')
let ParamPush = require('./ParamPush.js')
let LogRequestData = require('./LogRequestData.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let CommandLong = require('./CommandLong.js')
let FileRead = require('./FileRead.js')
let ParamGet = require('./ParamGet.js')
let FileRemove = require('./FileRemove.js')
let FileClose = require('./FileClose.js')
let FileChecksum = require('./FileChecksum.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let MountConfigure = require('./MountConfigure.js')
let LogRequestList = require('./LogRequestList.js')
let FileList = require('./FileList.js')
let CommandAck = require('./CommandAck.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let CommandBool = require('./CommandBool.js')
let ParamSet = require('./ParamSet.js')
let FileRename = require('./FileRename.js')
let CommandTOL = require('./CommandTOL.js')
let MessageInterval = require('./MessageInterval.js')
let FileOpen = require('./FileOpen.js')
let WaypointPull = require('./WaypointPull.js')
let ParamPull = require('./ParamPull.js')
let CommandHome = require('./CommandHome.js')
let WaypointClear = require('./WaypointClear.js')

module.exports = {
  SetMavFrame: SetMavFrame,
  FileRemoveDir: FileRemoveDir,
  FileTruncate: FileTruncate,
  CommandTriggerInterval: CommandTriggerInterval,
  CommandVtolTransition: CommandVtolTransition,
  WaypointPush: WaypointPush,
  FileWrite: FileWrite,
  WaypointSetCurrent: WaypointSetCurrent,
  FileMakeDir: FileMakeDir,
  CommandInt: CommandInt,
  StreamRate: StreamRate,
  SetMode: SetMode,
  ParamPush: ParamPush,
  LogRequestData: LogRequestData,
  CommandTriggerControl: CommandTriggerControl,
  CommandLong: CommandLong,
  FileRead: FileRead,
  ParamGet: ParamGet,
  FileRemove: FileRemove,
  FileClose: FileClose,
  FileChecksum: FileChecksum,
  LogRequestEnd: LogRequestEnd,
  MountConfigure: MountConfigure,
  LogRequestList: LogRequestList,
  FileList: FileList,
  CommandAck: CommandAck,
  VehicleInfoGet: VehicleInfoGet,
  CommandBool: CommandBool,
  ParamSet: ParamSet,
  FileRename: FileRename,
  CommandTOL: CommandTOL,
  MessageInterval: MessageInterval,
  FileOpen: FileOpen,
  WaypointPull: WaypointPull,
  ParamPull: ParamPull,
  CommandHome: CommandHome,
  WaypointClear: WaypointClear,
};
