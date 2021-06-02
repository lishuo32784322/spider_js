var CryptoJS = require("D:\\coder\\node\\node_modules\\crypto-js");
// var CryptoJS = require("crypto-js");

function thepaper(suuid, codeData) {
    var kdStr = {suuid: suuid, codeData: codeData}
    var iv = CryptoJS.lib.WordArray.random(128 / 8).toString(CryptoJS.enc.Hex);
    var kd = CryptoJS.enc.Utf8.parse(kdStr.codeData);
    md = CryptoJS.mode.ECB;
    var edt = CryptoJS.AES.encrypt(kdStr.codeData, kd, {
        iv: CryptoJS.enc.Hex.parse(iv),
        mode: md,
        padding: CryptoJS.pad.Pkcs7
    })
    var returnObj = {};
    returnObj.codeData = kdStr.codeData;
    returnObj.seeda = encodeURIComponent(edt);
    returnObj.suuid = kdStr.suuid;
    var checkValue = CryptoJS.MD5(kdStr.codeData + kdStr.suuid).toString();
    returnObj.sckval = checkValue;
    return returnObj
}
